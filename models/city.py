#!/bin/usr/python3
""" City Identification Module """

from models.base_model import BaseModel


class City(BaseModel):
	"""Represent City Object inheriting BaseModel

		ARGUMENTS:
		state_id (string): defines the id of state "state.id"
		name (string): city name
	"""

	state_id = ""
	name = ""
