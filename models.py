from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
# TODO: Move this to its own file & set up an actual database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Inspection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    aircraft_id = db.Column(db.String)
    imaging_time = db.Column(db.DateTime)
    approval_status = db.Column(db.Integer)
    ai_confidence = db.Column(db.Float)

    # Identifier method
    def __repr__(self):
        return 'Inspection #%r' % self.id
