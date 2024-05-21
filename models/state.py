#!/bin/usr/python3
""" State Identification Module """

from models.base_model import BaseModel


class State(BaseModel):
	"""Represent State Object interting BaseModel

		ARGUMENTS:
		name: state name
	"""

	name = ""
