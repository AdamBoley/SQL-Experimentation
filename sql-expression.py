from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)


# executing instructions from localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for the Artist table:
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)
# the use of primary_key=True indicates that this column name is the table's primary key

# create variable for the Album tabke:
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)
# ForeignKey takes one parameter - the Primary Key column of the table that it points to
# this links the two Tables together

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float),
)
# MediaTypeId is technically another Foreign Key, but that isn't relevant here, since we are not defining every table in the database


# connect to chinook database:
with db.connect() as connection:

    # Query 1 - fetch all results from the Artist table:
    # select_query = artist_table.select()
    # selects the table to be queried, and defines query parameters

    # Query 2 - fetch name column from Artist table:
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])
    # this is how particular columns are printed
    # multiple columns may be supplied in that list
    # the .c notation identifies a specific column

    # Query 3 - fetch Queen from Artist table:
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")
    # uses the .where command to supply the value from the name column that should be selected for    

    # Query 4 - fetch the row with ArtistId of 51 (also Queen):
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)
    # returns the same result as above, but searches by ArtistId instead

    # Query 5 - Fetch all albums with an ArtistId of 51:
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - fetch all tracks composed by Queen:
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    # select_query is defined outside the excute command

    for result in results:
        print(result)
