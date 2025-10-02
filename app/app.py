# app/app.py
from flask import Flask, render_template, jsonify
from prometheus_flask_exporter import PrometheusMetrics

# Create a single metrics object for the whole process
metrics = PrometheusMetrics.for_app_factory()
# Register static info ONCE against that metrics object
metrics.info('app_info', 'Portfolio service info', version='0.1.0')

def create_app():
    app = Flask(__name__)
    # Initialize metrics for this app instance (no duplicate registration)
    metrics.init_app(app)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/healthz')
    def healthz():
        return jsonify(status='ok'), 200

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)