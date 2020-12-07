from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['CORS_ORIGINS'] = ['*']
app.config['CORS_HEADERS'] = 'Content-Type'

clouds = []
cloud_index = 0


@app.route('/point_cloud')
def point_cloud():
    global cloud_index
    cloud_index += 1
    response = jsonify({'data': clouds[cloud_index % len(clouds)]})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/')
def index():
    global cloud_index
    cloud_index = 0
    return render_template('index.html')


def setup():
    global clouds
    for filename in ('data-1.txt', 'data-2.txt'):
        with open(filename, 'r') as fd:
            b64 = fd.readline()
            while b64:
                clouds.append(b64)
                b64 = fd.readline()


if __name__ == '__main__':
    setup()
    app.run(host='0.0.0.0')
