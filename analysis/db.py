from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import sql
import subprocess


class DB:
    def __init__(self):
        print("Instantiating DB class...")
        load_dotenv()
        self.params = {
            "DB_NAME": os.getenv("DB_NAME"),
            "DB_PORT": os.getenv("DB_PORT"),
            "DB_USER": os.getenv("DB_USER"),
            "DB_PW": os.getenv("DB_PW"),
            "DB_HOST": os.getenv("DB_HOST"),
        }

    def connect(self):
        print("Setting up database conncection...")
        self.connection = psycopg2.connect(
            database=self.params.get('DB_NAME'),
            user=self.params.get('DB_USER'),
            password=self.params.get('DB_PW'),
            host=self.params.get('DB_HOST'),
            port=self.params.get('DB_PORT'),
        )

        self.connection.autocommit = (
            True  # Enable autocommit to allow dropping database
        )
        cursor = self.connection.cursor()

        try:
            cursor.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
            print("PostGIS extension enabled.")
        except Exception as e:
            print(f"Error enabling PostGIS: {e}")

        cursor.close()

    def close(self):
        if self.connection:
            print("Closing database connection...")
            self.connection.close()

    def prepare_datasets_table(self, table_name):
        cursor = self.connection.cursor()
        print(f"Dropping {table_name} table if exists...")
        cursor.execute(f"""DROP TABLE IF EXISTS "{table_name}";""")
        print(f"Creating new {table_name} table with id, and resource geometry...")
        cursor.execute(
            f"""
                CREATE TABLE "{table_name}" (
                    id SERIAL PRIMARY KEY,
                    wkb_geometry GEOMETRY (geometry, 4326)
                )
            """
        )
        cursor.close()

    def derive_census_tracts_from_datasets(self, resource_table_names):
        cursor = self.connection.cursor()
        select_clause = ' UNION '.join([
            f"""SELECT DISTINCT c.GEOID10
                FROM "{name}" d
                JOIN census_tracts c
                ON st_intersects(d.wkb_geometry, c.wkb_geometry)"""
              for name in resource_table_names
              ])
        query = f"""
            {select_clause}
            ORDER BY GEOID10
        """
        try:
            print(f"Deriving administrative boundary ID and joining to {resource_table_names} table on st_intersects...")
            # Execute the query
            cursor.execute(query)
            # Fetch all results as a list of tuples
            results = cursor.fetchall()
            # Extract only the GEOID10 values into a flat list
            geoid_list = [row[0] for row in results]
            return geoid_list
        except Exception as e:
            print(f"Error deriving administrative boundary: {e}")
            return []
        finally:
            cursor.close()

    def import_census_tracts(self):
        print('Importing administrative boundary...')
        subprocess.run(
            [
                "ogr2ogr",
                "-f",
                "PostgreSQL",
                f"PG:host={self.params.get('DB_HOST')} user={self.params.get('DB_USER')} dbname={self.params.get('DB_NAME')} password={self.params.get('DB_PW')} port={self.params.get('DB_PORT')}",
                "working_files/Census_Tracts_2010.geojson",
                "-nln",
                "census_tracts",
                "-t_srs", "EPSG:4326",
                "-overwrite"
            ]
        )

    def import_dataset(self, path, table_name):
        print(f"Importing resource layer info into {table_name} table...")
        subprocess.run(
            [
                "ogr2ogr",
                "-f",
                "PostgreSQL",
                f"PG:host={self.params.get('DB_HOST')} user={self.params.get('DB_USER')} dbname={self.params.get('DB_NAME')} password={self.params.get('DB_PW')} port={self.params.get('DB_PORT')}",
                path,
                "-nlt", "PROMOTE_TO_MULTI",
                "-nln", table_name
            ]
        )

