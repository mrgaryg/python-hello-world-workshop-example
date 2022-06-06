From flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world:
    return 'Hello from VMware Tanzu!'


if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
