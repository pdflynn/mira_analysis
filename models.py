from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# TODO: Change the Strings to DATETIME
# Inspection matches the database table "Inspection" and
# represents an "object" form of each inspection thanks to
# SQLAlchemy. 
class Inspection(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.String)
    deadline = db.Column(db.String)
    aircraft_id = db.Column(db.String)
    imaging_time = db.Column(db.String)
    approval_status = db.Column(db.Integer)
    ai_confidence = db.Column(db.Float)

    # Getter for the id of the inspection
    def get_id(self):
        return self.id

    # Identifier method
    def __repr__(self):
        return 'Inspection #%r' % self.id

    # Changes the approval status of this inspection
    # from its current status to approved
    def approve_inspection(self):
        if self.approval_status != 1:
            self.approval_status = 1

    # Changes the approval status of this inspection
    # from its current status to denied.
    def deny_inspection(self):
        if self.approval_status != 2:
            self.approval_status = 2
