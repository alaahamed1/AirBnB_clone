#!/bin/usr/python3
""" Amenity Identification Module """

from models.base_model import BaseModel


class Amenity(BaseModel):
	"""Represent an Amenity Object inheriting BaseModel

		ARGUMENTS:
		name (string): amenity name
	"""

	name = ""
