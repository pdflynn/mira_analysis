from flask import Flask, render_template, url_for
app = Flask(__name__)

# Home Page
@app.route('/')
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