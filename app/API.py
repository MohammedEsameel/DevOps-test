import flask
from faker import Faker
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import Gauge
from prometheus_client import Histogram
from prometheus_client import start_http_server, Summary

g = Gauge('my_inprogress_requests', 'Description of gauge')
g.inc()      # Increment by 1
g.dec(10)    # Decrement by given value
g.set(4.2)   # Set to a given value

h = Histogram('request_latency_seconds', 'Description of histogram')
h.observe(4.7)    # Observe 4.7 (seconds in this case)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


fake = Faker()
def get_input():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year(),
    }

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route('/', methods=['GET'])

def home():
    return get_input()
app.run()



