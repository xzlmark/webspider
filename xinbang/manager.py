from flask import Flask
from flask_script import Manager
from APP.views import blue

app = Flask(__name__)

app.register_blueprint(blueprint=blue)

manager = Manager(app=app)


if __name__ == '__main__':
    manager.run()
