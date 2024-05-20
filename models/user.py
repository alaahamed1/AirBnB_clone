#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class representing a User in the Airbnb clone application.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
