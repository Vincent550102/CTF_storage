from flask import Flask, send_file, request, Response, redirect, session, url_for, render_template
app = Flask(__name__)
app.secret_key = 'yes'

@app.route('/')
def index():
    session['test'] = "test123"
    return 'test'



app.run(debug=True)
