#!/bin/usr/python3
""" Testing Module for Review class """

from models.review import Review
import unittest
import os

class TestReview(unittest.TestCase):
	"""Testing class for Review class."""
	def tearDown(self):
		file_path = "file.json"

		if os.path.exists(file_path):
			os.remove(file_path)

	def test_create_review_with_valid_arguments(self):
		"""
			Review object can be created with valid place_id,
			user_id, and text arguments.
		"""
		review = Review(place_id="123", user_id="456", text="Great place")
		self.assertEqual(review.place_id, "123")
		self.assertEqual(review.user_id, "456")
		self.assertEqual(review.text, "Great place")

	def test_save_review_successfully(self):
		"""
			Review object can be saved successfully.
		"""
		review = Review(place_id="123", user_id="456", text="Great place")
		review.save()
		self.assertIsNotNone(review.updated_at)

	def test_to_dict_method_returns_correct_dictionary_representation(self):
		"""
			to_dict() method returns a dictionary
			representation of the Review object with correct
			keys and values
		"""
		review = Review(place_id="123", user_id="456", text="Great place")
		review_dict = review.to_dict()
		self.assertEqual(review_dict["__class__"], "Review")
		self.assertEqual(review_dict["place_id"], "123")
		self.assertEqual(review_dict["user_id"], "456")
		self.assertEqual(review_dict["text"], "Great place")

if __name__ == "__main__":
	unittest.main()
