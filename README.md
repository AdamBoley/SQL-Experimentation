

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.


Install Chinook database:
`wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql`

Set Postgres environment variable:
`set_pg`

Start Postgres CLI:
`psql`

To view all databases:
`\l`

By default, Chinook comes with 3 databases - postgres, template0, template1

Create new database:
`CREATE DATABASE chinook;`
CREATE DATABASE is a command, chinook is the new database's name


Switch between databases:
`\c <database name>`
i.e:
`\c postgres` or `\c chinook`

\c is the connect command

Initialise Chinook_PostgreSql.sql file that was added by the first `wget` command:
`\i Chinook_PostgreSql.sql`

To quit the Postres shell:
`\q`

To restart the Postgres shell and connect to a specific database:
`psql -d <database name>`
i.e.:
`psql -d chinook`

Check that all tables and data were added with the install command:
`\dt`

From this, we can see that Chinnok includes 11 tables - Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack and Track

Basic SQL commands:

Retrieve all data from the Artist table:
`SELECT * FROM "ARTIST";`

This will list the entirety of the Artist table

To exit from this view:
`q` 

Retrieve the Name column from the Artist table:
`SELECT "Name" FROM "Artist";`

Search for a particular row within the Name column of the Artist table:
`SELECT * FROM "Artist" WHERE "Name" = 'Queen';`

This command would produce the same result:
`SELECT * FROM "Artist" WHERE "ArtistId" = 51;`

This is because both ArtistId of 51 and Name of Queen are on the same row

Find all of Queen's albums:
`SELECT * FROM "Albums" WHERE "ArtistId" = 51`
This works because the Albums table includes the ArtistId column
ArtistId in the Albums table is a Foreign Key, since it is also the Primary Key of the Artists table

FInd all of Queen's Tracks:
`SELECT * FROM "Track" WHERE "Composer" = 'Queen';`

Transcribe the output of an SQL query to a CSV file:
`\copy (SELECT * FROM "Track" WHERE "Composer" = 'Queen') TO 'test.csv' WITH CSV DELIMITER ',' HEADER;`

Create a json file:
`\o test.json`

Transcribe output of a query to that JSON file:
`SELECT json_agg(t) FROM (SELECT * FROM "Track" WHERE "Composer" = 'Queen') t`

Note that these last two must be run one after another. I think that `\o test.json` both creates and selects the file to be transcribed into. 
Without this, the transcribe command fails, even if it is valid and properly constructed


### Python

Install the psycopg2 database adapter:
`pip3 install psycopg2`

create a Python file to hold SQL queries:
`touch sql-psycopg2`

Set the postgres environment variable:
`set_pg`

Run the python file:
`python3 sql-psycopg2`


### SQl Alchemy

Install SQL Alchemy:
`pip3 install SQLAlchemy`

Create new file for the SQL Alchemy expression language:
`touch sql-expression.py`

Set the postgres environment variable:
`set_pg`

Find column names (also called column headers):
`SELECT * FROM "Artist" WHERE false`
We can see that the Artist table has two columns - ArtistId and Name

Find column headers for the Album and Track tables:
`SELECT * FROM "Album" WHERE false`
`SELECT * FROM "Track" WHERE false`

Run the commands:
`python3 sql-expression.py`



### SQL Alchemy ORM

New file for exploring the SQL Alchemy ORM methods:
`touch sql-orm.py`

Set the postgres environment variable:
`set_pg`

Run the file:
`python3 sql-orm.py`


### CRUD

New file for CRUD methods:
`touch sql-crud.py`

Set the postgres environment variable:
`set_pg`

Run the file:
`python3 sql-crud.py`




