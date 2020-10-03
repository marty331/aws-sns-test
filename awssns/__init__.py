import os
import time
import uuid
import json

from flask import Flask, request
from awssns.messages import Message


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'awssns.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        print(f"instance {app.instance_path}")
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/test-sns', methods=(['POST']))
    def sns_test():
        if request.method == 'POST':
            message = request.args.get('message')
            data = dict(
                    messagePayload=message,
                    eventId=uuid.uuid4().hex,
                    messageCreatedAt=int(time.time()),
                )
            sns_message = Message(json.dumps(data)).route()
            return "Test SNS"

    return app
