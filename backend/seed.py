#!/usr/bin/env python3

from app import app
from models import db, Gallery, Music, User, UserGallery, UserMusic

with app.app_context():

    print("Deleting data...")

    Gallery.query.delete()
    Music.query.delete()
    User.query.delete()
    UserGallery.query.delete()
    UserMusic.query.delete()


    print("Creating users...")

    CheddarBob69 = User(fname="Robert", lname="Cheddar", email="CheddarBob@gmail.com", dob=2000, username="CheddarBob69", password="password123")
    MaryJane420 = User(fname="Jane", lname="Doe", email="JaneDoe@gmail.com", dob=2000, username="MaryJane420", password="password123")
    BigJohn69 = User(fname="John", lname="Doe", email="JohnDoe@gmail.com", dob=2000, username="BigJohn69", password="password123")
    users = [CheddarBob69, MaryJane420, BigJohn69]


    print("Creating Galleries...")

    Mona_Lisa = Gallery(title="Mona Lisa",
                        artist="Leonardo da Vinci",
                        release_year=1517,
                        image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.italian-renaissance-art.com%2Fimages%2FLeonardo-Mona-Lisa.jpg&f=1&nofb=1&ipt=3e4fcbbd3b49fe570b1585af0633049095a293eda8b158a3d7f172ed9172a309&ipo=images",
                        medium="Oil on poplar panel",
                        genre="Renaissance",
                        link="https://www.example.com")
    Starry_Night = Gallery(title="Starry Night",
                          artist="Van Gogh",
                          release_year=1889,
                          image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fuploads3.wikiart.org%2F00142%2Fimages%2Fvincent-van-gogh%2Fthe-starry-night.jpg&f=1&nofb=1&ipt=74562267039b6e20e543e6fdd962d81a4e3b11255b8ed5bbd4648f63456c296d&ipo=images",
                          medium="Oil on canvas",                    
                          genre="Post-Impressionism",
                          link="https://www.example.com")
    Girl_With_Pearl_Earring = Gallery(title="Girl With a Peal Earring",
                                      artist="Johannes Vermeer",
                                      release_year=1665,
                                      image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp7298625.jpg&f=1&nofb=1&ipt=936e958d8cc4f58f0204b0c705645bc20f5cb7e08ac5fb772016c3c9f483ccc4&ipo=images",
                                      medium="Oil on canvas",     
                                      genre="Dutch Golden Age",
                                      link="http://www.example.com")
    galleries = [Mona_Lisa, Starry_Night, Girl_With_Pearl_Earring]


    print("Creating Music...")

    Toxicity = Music(title="Toxicity",
                        artist="System of a Down",
                        release_year=2001,
                        image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.26ajcRlSvz6rGXPb2PwEkwHaHa%26pid%3DApi&f=1&ipt=ebd62f3da0fd5d75495f490d7e6810bf09343d43b869708843724ea33c6dbf3e&ipo=images",
                        genre="Rock",
                        link="https://www.example.com")
    Nevermind = Music(title="Nevermind",
                          artist="Nirvana",
                          release_year=1991,
                          image="https://images-na.ssl-images-amazon.com/images/I/61quAjwYMtS._SX522_.jpg",                   
                          genre="Rock",
                          link="https://www.example.com")
    Vespertine = Music(title="Vespertine",
                                      artist="Bjork",
                                      release_year=2001,
                                      image="https://images.genius.com/b15640bb327be7a233301bdea8f2939a.1000x1000x1.png",     
                                      genre="Pop",
                                      link="http://www.example.com")
    music = [Toxicity, Nevermind, Vespertine]


    print("Creating UserGallery...")

    pr1 = UserGallery(user_object=CheddarBob69, gallery_object=Mona_Lisa, price=1_000_000)
    pr2 = UserGallery(user_object=MaryJane420, gallery_object=Starry_Night, price=1_000_000)
    pr3 = UserGallery(user_object=BigJohn69, gallery_object=Girl_With_Pearl_Earring, price=1_000_000)
    userGallery = [pr1, pr2, pr3]
    db.session.add_all(users)
    db.session.add_all(galleries)
    db.session.add_all(userGallery)
    db.session.commit()


    print("Creating UserMusic...")

    pr4 = UserMusic(user_object=CheddarBob69, music_object=Toxicity, price=15)
    pr5 = UserMusic(user_object=MaryJane420, music_object=Nevermind, price=15)
    pr6 = UserMusic(user_object=BigJohn69, music_object=Vespertine, price=15)
    userMusic = [pr4, pr5, pr6]
    db.session.add_all(users)
    db.session.add_all(music)
    db.session.add_all(userMusic)
    db.session.commit()


    print("Seeding done!")
