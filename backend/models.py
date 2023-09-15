from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Gallery(db.Model, SerializerMixin):
    __tablename__ = 'gallery_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    release_year = db.Column(db.Integer)
    image = db.Column(db.String)
    medium = db.Column(db.String)
    genre = db.Column(db.String)
    link = db.Column(db.String)

    user_gallery = db.relationship("UserGallery", back_populates = "gallery_object", cascade = "all, delete-orphan")

    serialize_rules = ("-user_gallery.gallery_object",)

    def __repr__(self):
        return f'<Gallery {self.title}, {self.artist}, {self.release_year}, {self.image}, {self.medium}, {self.genre}, {self.link} >'

class Music(db.Model, SerializerMixin):
    __tablename__ = 'music_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    release_year = db.Column(db.Integer)
    image = db.Column(db.String)
    genre = db.Column(db.String)
    link = db.Column(db.String)

    user_music = db.relationship("UserMusic", back_populates = "music_object", cascade = "all, delete-orphan")

    serialize_rules = ("-user_music.music_object",)

    def __repr__(self):
        return f'<Gallery {self.title}, {self.artist}, {self.release_year}, {self.image}, {self.genre}, {self.link} >'


class User(db.Model, SerializerMixin):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    dob = db.Column(db.Integer)
    username = db.Column(db.String)
    password = db.Column(db.String)

    # user_gallery = db.relationship("UserGallery", back_populates = "gallery_object", cascade = "all, delete-orphan")
    # user_music = db.relationship("UserMusic", back_populates = "music_object", cascade = "all, delete-orphan")
    user_gallery = db.relationship("UserGallery", back_populates = "user_object", cascade = "all, delete-orphan")
    user_music = db.relationship("UserMusic", back_populates = "user_object", cascade = "all, delete-orphan")

    serialize_rules = ("-user_gallery.user_object", "-user_music.user_object",)

    def __repr__(self):
        return f'<User {self.fname}, {self.lname}, {self.email}, {self.dob}, {self.username}, {self.password}>'


class UserGallery(db.Model, SerializerMixin):
    __tablename__ = 'user_gallery_table'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    gallery_id = db.Column(db.Integer, db.ForeignKey("gallery_table.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"))

    gallery_object = db.relationship("Gallery", back_populates = "user_gallery")
    user_object = db.relationship("User", back_populates = "user_gallery")

    serialize_rules = ("-gallery_object.user_gallery", "-user_object.user_gallery",)

    @validates("price")
    def validate_price(self, key, price):
        if price < 1 or price > 1_000_000_000:
            raise ValueError("invalid price")
        return price
    
    def __repr__(self):
        return f'<UserGallery ${self.price}>'
    
class UserMusic(db.Model, SerializerMixin):
    __tablename__ = 'user_music_table'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    music_id = db.Column(db.Integer, db.ForeignKey("music_table.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"))

    music_object = db.relationship("Music", back_populates = "user_music")
    user_object = db.relationship("User", back_populates = "user_music")

    serialize_rules = ("-music_object.user_music", "-user_object.user_music",)

    @validates("price")
    def validate_price(self, key, price):
        if price < 1 or price > 1_000_000_000:
            raise ValueError("invalid price")
        return price
    
    def __repr__(self):
        return f'<UserMusic ${self.price}>'
