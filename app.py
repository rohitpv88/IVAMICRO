from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to run the first script
@app.route('/run_first_script')
def run_first_script():
    # Run the first Python script
    subprocess.Popen(['python', 'first_script.py'])
    return redirect(url_for('index'))

# Route to run the second script
@app.route('/run_second_script')
def run_second_script():
    # Run the second Python script
    subprocess.Popen(['python', 'second_script.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
