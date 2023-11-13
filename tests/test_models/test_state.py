import unittest
from models.state import State  # Adjust the import path as needed


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up an instance of State for reuse in test methods."""
        self.state = State(name="California")

    def test_state_instance(self):
        """Test if an instance of State is created correctly."""
        state = self.state
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        """
        Test if attributes are set properly when creating a State instance.
        """
        state = self.state
        self.assertEqual(state.name, "California")

    def test_state_to_dict(self):
        """Test the to_dict method of State."""
        state = self.state
        state_dict = state.to_dict()

        self.assertEqual(state_dict['name'], "California")
        self.assertEqual(state_dict['__class__'], "State")

    def test_state_str(self):
        """Test the __str__ method of State."""
        state = self.state
        state_str = str(state)

        self.assertIn('State', state_str)
        self.assertIn(state.id, state_str)
        self.assertIn('California', state_str)


if __name__ == '__main__':
    unittest.main()
