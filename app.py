from flask import Flask
from endpoints import endpoints
import logger

app = Flask(__name__)

app.register_blueprint(endpoints)

if __name__ == "__main__":
    logger.log(app)
    app.run(debug=True)