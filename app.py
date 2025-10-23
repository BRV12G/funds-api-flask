from . import app, db
from flask import request, make_response
from .models import Users, Funds
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    firstName = data.get("firstName")
    lastName = data.get("lastName")
    password = data.get("password")

    if firstName and lastName and email and password:
        user = Users.query.filter_by(email=email).first() #Queries the database for an existing user with the same email.
        if user:
            return make_response(
                {"message": "Please log In, user already exists"},
                200
            )
        user = Users(
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=generate_password_hash(password)

        )
        db.session.add(user)
        db.session.commit()
        return make_response(
            {"message": "user created"}, 201
        )
    return make_response(
        {"message": "unable to create User"}, 500
    )


