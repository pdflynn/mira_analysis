# neil branch
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Inspection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mira_dev.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    print(inspection_id)
    inspections = Inspection.query.all()
    inspection = "didn't update"
    for ins in inspections:
        if int(ins.get_id()) == int(inspection_id):
            inspection = ins
    print(inspection)

    return render_template('inspection_result.html', inspection=inspection)

# Analysis Page
@app.route('/analyze', methods=['GET', 'POST'])
def mira_analyze():
    test_data = Inspection.query.all()

    return render_template('analyze.html', data=test_data)