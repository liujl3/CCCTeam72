from flask import Flask
from flask import jsonify
from flask import render_template
app = Flask(__name__)

# Views
@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'
    # return render_template("team72-web/dist/index.html")

# APIs
# /api/count?
#   type=date/state/city?
# /api/dot
# /api/map

if __name__ == '__main__':
    app.run()