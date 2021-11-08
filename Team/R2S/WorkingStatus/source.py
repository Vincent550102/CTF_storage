from os import getenv, urandom
from flask import Flask, send_file, request, Response, redirect, session, url_for, render_template
import jwt, json, requests

accounts = {
    'guest': 'guest',
    'admin': getenv('ADMIN_PASSWORD') or 'admin'
}

flag = getenv('FLAG')
site_key = getenv('HCAPTCHA_SITE_KEY')

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY') or urandom(16)

@app.route('/')
def index():
    user = session.get('user')
    signed = request.args.get('signed')
    return render_template('index.html', user=user, signed=signed)

@app.route('/source')
def source():
    return send_file(__file__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        if username not in accounts:
            accounts[username] = password
        if accounts[username] == password:
            session['user'] = username
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/sign')
def sign():
    status = request.args.get('status', '')
    callback = request.args.get('callback', '')
    user = session.get('user', 'unknown')
    data = { 'status': status, 'user': user }
    signed = jwt.encode(data, app.secret_key, algorithm="HS256")
    return cb(callback, signed)

@app.route('/verify')
def verify():
    signed = request.args.get('signed','')
    callback = request.args.get('callback')
    try:
        data = jwt.decode(signed, app.secret_key, algorithms='HS256')
        if data['status'] == 'flag' and data['user'] == 'admin':
            data['flag'] = flag
    except:
        data = {'error':'jwt decode error'}
    return cb(callback, data)

@app.route('/report', methods=['GET','POST'])
def report():
    result = ''
    if request.method == 'POST':
        data = {
            'url': request.form.get('url'),
            'token': request.form.get('h-captcha-response'),
        }
        try:
            r = requests.get('http://bot', params=data)
            result = r.json()['result']
        except:
            result = 'Bot is down, please contact to admin.'
    return render_template('report.html', site_key=site_key, result=result)

def cb(callback, data):
    return Response(f'{callback}({json.dumps(data)})', mimetype='text/javascript')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)
