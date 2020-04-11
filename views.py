# danny branch
from flask import Flask, render_template, url_for
from models import Inspection
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mira_dev.db'

db = SQLAlchemy(app)

# Home Page
@app.route('/',)
def mira_home():
    return render_template('home.html')

# Command & Control Page
@app.route('/command')
def mira_command():
    return render_template('command.html')


# Results Page
@app.route('/results')
def mira_results():
    return render_template('results.html')

# Unique page per inspection
@app.route('/results/inspection/<inspection_id>')
def mira_inspection_result(inspection_id):
    # Grabs all of the inspections from the Inspection table.
    # Note: This is probably an inefficient way to do this and
    # could be improved.
    inspections = Inspection.query.all()

    # Initialize "inspection" with a null pointer, and then once
    # we find the inspection in the inspections table that matches
    # the ID that was passed to this function, send it through to 
    # the front end with render_template. From there, it can be 
    # accessed via Jinja.
    inspection = None
    for ins in inspections:
        if int(ins.get_id()) == int(inspection_id):
            inspection = ins

    return render_template('inspection_result.html', inspection=inspection)

# Analysis Page
@app.route('/analyze', methods=['GET', 'POST'])
def mira_analyze():
    test_data = Inspection.query.all()

    return render_template('analyze.html', data=test_data)