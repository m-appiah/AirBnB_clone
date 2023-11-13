"""Unittest Module fr the Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up an instance of Review for reuse in test methods."""
        self.review = Review(
                place_id="123",
                user_id="456",
                text="A great place to stay!"
                )

    def test_review_instance(self):
        """Test if an instance of Review is created correctly."""
        review = self.review
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        """
        Test if attributes are set properly when creating a Review instance.
        """
        review = self.review
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "A great place to stay!")

    def test_review_to_dict(self):
        """Test the to_dict method of Review."""
        review = self.review
        review_dict = review.to_dict()

        self.assertEqual(review_dict['place_id'], "123")
        self.assertEqual(review_dict['user_id'], "456")
        self.assertEqual(review_dict['text'], "A great place to stay!")
        self.assertEqual(review_dict['__class__'], "Review")

    def test_review_str(self):
        """Test the __str__ method of Review."""
        review = self.review
        review_str = str(review)

        self.assertIn('Review', review_str)
        self.assertIn(review.id, review_str)
        self.assertIn('A great place to stay!', review_str)


if __name__ == '__main__':
    unittest.main()
