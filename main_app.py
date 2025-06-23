from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/new_user')
def new_user():

    subprocess.run(["python", "get_faces_from_camera_tkinter.py"])
    subprocess.run(["python", "features_extraction_to_csv.py"])

    return redirect(url_for('home'))

@app.route('/take_attendance')
def take_attendance():

    subprocess.run(["python", "attendance_taker.py"])
    return redirect(url_for('home'))


@app.route('/view_attendance')
def view_attendance():
    return redirect("http://127.0.0.1:5001/")

if __name__ == '__main__':
    app.run(debug=True)
