from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/main')
def main():
    return "Main Page", 200

@app.route('/2x-code')
def success():
    return "Success", 200

@app.route('/4x-code')
def not_found():
    return "Not Found", 404

@app.route('/5x-code')
def server_error():
    return "Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
