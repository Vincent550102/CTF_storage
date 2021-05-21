from flask import Flask, Response, request
import pickle, base64, traceback
Response.default_mimetype = 'text/plain'
app = Flask(__name__)
@app.route("/")
def index():
    data = request.values.get('data')
    if data is not None:
        try:
            data = base64.b64decode(data)
            data = pickle.loads(data)
            print(data)
            if data and not data:
                return open('/flag').read()
            return str(data)
        except:
            return traceback.format_exc()
    return open(__file__).read()

app.run()
