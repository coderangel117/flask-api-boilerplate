from flask_jwt_extended import JWTManager
from api import create_app

app = create_app()
jwt = JWTManager(app)


@app.before_request
def verify_token():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
