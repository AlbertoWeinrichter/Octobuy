import multiprocessing
import os

bind = "0.0.0.0:{flask_port}".format(flask_port=os.environ["FLASK_PORT"])

workers = multiprocessing.cpu_count() * 2 + 1
max_requests = 1000
