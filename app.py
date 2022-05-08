from flask import Flask, send_file

app = Flask(__name__)

@app.route('/<path:path>')
def get_image(path):
    image_path = '/home/anhz/Desktop/project' + '/data/image/{}'.format(path)

    return send_file(image_path, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=7000)