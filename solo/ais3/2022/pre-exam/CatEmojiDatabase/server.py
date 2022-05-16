from flask import Flask, request, redirect, jsonify, send_file
import re
app = Flask(__name__)


@app.before_request
def fix_path():
    # trim all the whitespace from path
    trimmed = re.sub('\s+', '', request.path)
    if trimmed != request.path:
        return redirect(trimmed)
@app.route('/api/emoji/<unicode>')
def api(unicode):
    print("%s" % unicode)
    return unicode


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
