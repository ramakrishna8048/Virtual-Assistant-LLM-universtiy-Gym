from flask import Flask

app=Flask(__name__)

@app.route('/hours')
def hours():
    return "Rec center opening Timings are 7AM to 11PM"

@app.route('/classes')
def classes():
    return "Available classes: Yoga, Zumba, CrossFit."
    