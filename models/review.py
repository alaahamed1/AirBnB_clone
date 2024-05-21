#!/bin/usr/python3
"""
	Review identification Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
	"""
		Represent Review Object inheriting BaseModel

		ARGUMENTS:
		----------
		place_id (string): id of place that's being reviewed,
			it will be the Place.id
		user_id (string): id of the user who wrote the review,
			it will be the User.id
		text: the review given
	"""

	place_id = ""
	user_id = ""
	text = ""
