# danny branch
from flask import Flask, render_template, url_for
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

# Analysis Page
@app.route('/analyze', methods=['GET', 'POST'])
def mira_analyze():
    test_data = Inspection.query.all()
    print(test_data)

    return render_template('analyze.html', data=test_data)