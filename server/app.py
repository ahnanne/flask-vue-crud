from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# 동적 라우팅
@app.route('/ping/<name>', methods=['GET'])
def ping_pong_name(name):
    print(request)
    return jsonify('User: {}'.format(name))


if __name__ == '__main__':
    app.run()