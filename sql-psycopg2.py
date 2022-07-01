import psycopg2


# connect psycopg2 to Chinook database:
connection = psycopg2.connect(database="chinook")
# in addition to database, we can supply other connection values
# these would be host, username, password, etc
# which would be useful for an actual working project database

# build a cursor object of the database
cursor = connection.cursor()
# a cursor object is a data structure, like a set, list or dictionary
# database queries will become part of this cursor object
# this means that the cursor object can be iterated over

# Query 1 - fetch all results from the Artist table:
# cursor.execute('SELECT * FROM "Artist"')
# note how similar the psycopg2 commands are to standard SQL commands
# Single quotes must be used to wrap queries

# Query 2 - fetch name column from Artist table:
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - fetch Queen from Artist table:
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# %s is the Python string placeholder, and Queen is placed in square brackets
# this indicates that it is a list
# this list can hold multiple placeholders
# this is useful if the query needs to be detailed
# Because we are fetching only one row of the table, the fetchone command can be used

# Query 4 - fetch the row with ArtistId of 51 (also Queen):
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Fetch all albums with an ArtistId of 51:
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - fetch all tracks composed by Queen:
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - fetch all tracks composed by Metallica:
# First, find the ArtistId of Metallica:
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Metallica"])
# We see that Metallica has an ArtistId of 50
# Then, fetch all tracks by Metallica:
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Metallica"])
# returns several tuples containing the values from the relevant rows
# Find just the tracks:
# cursor.execute('SELECT "Name" FROM "Track" WHERE "Composer" = %s', ["Metallica"])
# returns track names

# fetch the results:
results = cursor.fetchall()
# the fetchall method is used when we want to fetch multiple records
# fetchall will return a tuple in brackets

# fetch a single result:
# results = cursor.fetchone()
# fetchone will return the raw values from one row of the table
# each value will be printed on separate lines in the console
# if used for queries where multiple rows would be returned, will return the first row's values on separate lines


# close the database connection:
connection.close()
# this is much like working with a file - open it, do something then close it

# print results from cursor object:
for result in results:
    print(result)
