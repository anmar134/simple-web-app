import os
from flask import Flask
application = Flask(__name__)

@application.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    application.run()
