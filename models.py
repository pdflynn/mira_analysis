from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# TODO: Change the Strings to DATETIME
class Inspection(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.String)
    deadline = db.Column(db.String)
    aircraft_id = db.Column(db.String)
    imaging_time = db.Column(db.String)
    approval_status = db.Column(db.Integer)
    ai_confidence = db.Column(db.Float)

    def get_id(self):
        return self.id

    # Identifier method
    def __repr__(self):
        return 'Inspection #%r' % self.id
