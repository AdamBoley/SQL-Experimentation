from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# declarative base is a class


# link SQL Alchemy to local database:
db = create_engine('postgresql:///chinook')

base = declarative_base()
# base grabs the metadata of the database and creates a subclass
# this is basically piggybacking off of the pre-defined ORM class

# create a class based model for the Artist table:
class ArtistTable(base):  # note use of PascalCase to name the class
    # (base) means that ArtistTable is subclass of the base class
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class AlbumTable(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))
    # The Foreign Key references the ArtistTable above, using the tablename of Artist and the attribute(?) of ArtistId


# create a class-based model for the Track table:
class TrackTable(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# create a new session of the database
# this replaces the part where we connect to the database
# create a new imstance of sessionmaker, and point it to the engine, which is the variable db
# sessionmaker is a class as well
# Session creates a new instance of the sessionmaker class

Session = sessionmaker(db)

# opens an actual session by calling the Session subclass from above
session = Session()

# creating the database using the declarative_base subclass
base.metadata.create_all(db)

# Query 1 - fetch all results from the Artist table:
# artists = session.query(ArtistTable)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")
    # print(artist)
    # Unlike with other methods, print(artist) doesn't produce useful data

# This format, with the | pipe symbol is used to separate each result into the format of number | artist

# Query 2 - fetch name column from Artist table:
# artists = session.query(ArtistTable)
# for artist in artists:
#     print(artist.Name)
# Here, we are removing artist.ArtistId, because it is not needed for this query
# We are actively tailoring our request to get the data we want

# Query 3 - fetch Queen from Artist table:
# artist = session.query(ArtistTable).filter_by(Name="Queen").first()
# # This is similar to the use of the SQL WHERE command
# # the .first() method is a bit of defensive programming, ensuring we only get the first valid result, in case there is more than one entry with the name of Queen 

# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - fetch the row with ArtistId of 51 (also Queen):
# artist = session.query(ArtistTable).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - Fetch all albums with an ArtistId of 51:
# albums = session.query(AlbumTable).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - fetch all tracks composed by Queen:
tracks = session.query(TrackTable).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
# The parameters are vertically stacked to make this query PEP8 compliant


