"""Models and database functions for Dating Project."""

from flask_sqlalchemy import SQLAlchemy


# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library.

db = SQLAlchemy()

##############################################################################
# Model definitions


class User(db.Model):
    """User of dating website."""

    __tablename__ = "users"


    user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    fname   = db.Column(db.String(25), nullable = False)
    lname   = db.Column(db.String(25), nullable = False)
    email   = db.Column(db.String(100), nullable = False)
    password= db.Column(db.String(25), nullable= False)
    age     = db.Column(db.Integer, nullable = False)
    gender= db.Column(db.String(1), nullable = False)
    city    = db.Column(db.String(25), nullable = False)
    state =db.Column(db.String(25), nullable = False)
    contact_no = db.Column(db.String(10), nullable = False)
    occupation = db.Column(db.String(25), nullable=False)
    yourself = db.Column(db.String(200), nullable=True)
######### Define Relationship ############

    hobbies = db.relationship(Hobbie)
    likes = db.relationship(Like)
    dislikes = db.relationship(Dislike)
    images = db.relationship(Image)

    def __repr__(self):

        """ Provide helpful representation when printed """
        us = f"""<Human user_id = {self.user_id} 
                        fname = {self.fname}
                        lname = {self.lname}
                        email = {self.email}
                        password = {self.password}
                        age = {self.age}
                        gender = {self.gender}
                        city={self.city}
                        state={self.state}
                        contact_no={self.contact_no}>"""
        return us

class Hobbie(db.Model):
    """Hobbie model of dating website"""

    __tablename__ = "hobbies"

    hobbie_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    hobbie_name = db.Column(db.String(25), nullable = False)
#relationship
    users = db.relationship(User)

    def __repr__(self):

        """ Provide helpful representation when printed """
        hb = f"""<Human  hobbie_id ={self.hobbie_id}
                        user_id ={self.user_id} 
                        hobbie_name={self.hobbie_name}>"""
        return hb

class Like(db.Model):
    """like model of dating website"""

    __tablename__ = "likes"


    like_id= db.Column(db.Integer, autoincrement = True, primary_key = True) 
    likes_user = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    liked_user = db.Column(db.Integer, db.ForeignKey('users.user_id'))

#relationship
    users = db.relationship(User)

    def __repr__(self):

        """ Provide helpful representation when printed """
        lk = f"""<Human  like_id ={self.like_id}
                        likes_user ={self.likes_user} 
                        liked_user={self.liked_user}>"""
        return lk

class Dislike(db.Model):
    """dislike model of dating website"""

    __tablename__ = "dislikes"


    dislike_id= db.Column(db.Integer, autoincrement = True, primary_key = True) 
    dislikes = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    disliked = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#relationship
    users = db.relationship(User)

    def __repr__(self):

        """ Provide helpful representation when printed """
        dl = f"""<Human  dislike_id ={self.dislike_id}
                        dislikes ={self.dislikes} 
                        disliked={self.disliked}>"""
        return dl

class Image(db.Model):
    """image model"""

    __tablename__="images"

    image_id = db.Column(db.Integer, autoincrement = True, primary_key = True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    url = db.Column(db.String(200), nullable=False)
    
#relationship
    users = db.relationship(User)

    def __repr__(self):

        """ Provide helpful representation when printed """
        im = f"""<Human  image_id ={self.image_id}
                        user_id ={self.user_id} 
                        url={self.url}>"""
        return im

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dating'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    #from server import app
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to DB.")