from flask import Flask, render_template, url_for
# from models import app
# Neil's branch, attempting commit
app = Flask(__name__)

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
@app.route('/analyze')
def mira_analyze():
    return render_template('analyze.html')