#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:
	"""
	Base class for all models in the Airbnb clone application.
	"""

	def __init__(self, *args, **kwargs):
		"""
		Initializes a new BaseModel instance.
		Args:
			*args: Additional arguments passed to the constructor.
			**kwargs: Keyword arguments used to set instance attributes.
		"""

		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
		if kwargs:
			for key, val in kwargs.items():
				if key != '__class__':
					if key == "created_at" or key == "updated_at":
						setattr(
								self,
								key,
								datetime.strptime(
									val,
									'%Y-%m-%dT%H:%M:%S.%f')
								)
					else:
						setattr(self, key, val)
		else:
			storage.new(self)
	def __str__(self):
		"""Return a string representation of the class"""

		return "[{:s}] ({:s}) {:s}".format(
				self.__class__.__name__,
				self.id,
				str(self.__dict__)
			)

	def save(self):
		"""
		Updates the updated_at attribute with the current datetime and saves
		the object to the storage engine.
		"""
		self.updated_at = datetime.now()
		storage.save()

	def to_dict(self):
		"""
		Returns a dictionary containing all instance attributes of the object.

		The dictionary includes the following:
			- __class__: The class name of the object.
			- All other attributes are included with their corresponding values.
			- created_at and updated_at are converted to ISO format strings.
		"""
		rep = {
				"__class__": self.__class__.__name__,
				"created_at": self.created_at.isoformat(),
				"updated_at": self.updated_at.isoformat()
				}
		dict_copy = self.__dict__.copy()
		dict_copy.update(rep)
		return dict_copy
