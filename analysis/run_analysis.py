import psycopg2

DB_NAME="postgres"
DB_PORT=5433
DB_USER="docker"
DB_PW="docker"
DB_HOST="localhost"

# connection establishment
conn = psycopg2.connect(
database=DB_NAME,
	user=DB_USER,
	password=DB_PW,
	host=DB_HOST,
	port=DB_PORT
)
cursor = conn.cursor()

# Query dataset by census_tract

select_statement = '''
	SELECT c.GEOID10, p.OBJECTID, ST_AsText(ST_GeomFromWKB(p.wkb_geometry))
    FROM street_poles p
	JOIN census_tracts c
    ON st_within(p.wkb_geometry, c.wkb_geometry)
    ORDER BY c.GEOID10
'''

SQL_for_file_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(select_statement)

#import to csv for viewing
csv_file = open('test.csv', 'w')

cursor.copy_expert(SQL_for_file_output, csv_file)

# Closing the connection
cursor.close()
conn.close()
