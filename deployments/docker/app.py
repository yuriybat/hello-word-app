from flask import Flask,  jsonify 
import os 
app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello I am a developer my name is Yuriy B',
        'environment': os.environ.get('ENVIRONMENT'),
        'owner': 'yuriybat',
        'namespace': os.environ.get('NAMESPACE')
    })


@app.route('/yuriybat')
def yuriybat():
    return jsonify({
        'message': 'This is Yuriy B page!!'
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)