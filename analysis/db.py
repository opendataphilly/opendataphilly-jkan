from dotenv import load_dotenv
import os
import subprocess
import sqlite3 as sql


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
        self.connection = sql.connect(
            "analysis.db"
        )
        self.connection.execute("PRAGMA journal_mode=WAL;")
        self.connection.enable_load_extension(True)
        self.connection.execute("SELECT load_extension('mod_spatialite');")

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
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    geom GEOMETRY
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
                ON ST_Intersects(d.geom, c.geom)"""
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
                "SQLite",
                "analysis.db",
                "working_files/Census_Tracts_2010.geojson",
                "-nln",
                "census_tracts",
                "-t_srs", "EPSG:4326",
                "-overwrite",
                "-dsco", "SPATIALITE=YES",
                "-lco", "GEOMETRY_NAME=geom"
            ]
        )

    def import_dataset(self, path, table_name):
        print(f"Importing resource layer info into {table_name} table...")
        subprocess.run(
            [
                "ogr2ogr",
                "-f",
                "SQLite",
                "analysis.db",
                path,
                "-nlt", "PROMOTE_TO_MULTI",
                "-nln", table_name,
                "-dsco", "SPATIALITE=YES",
                "-lco", "GEOMETRY_NAME=geom"
            ]
        )

