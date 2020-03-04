import unittest 
import user

class TestUser(unittest.TestCase):

  def setUp(self):
      self.test_user = user
  
  def test_say_hello(self):
    """vamos a testear el metodo say hello"""
    hello = self.test_user.say_hello('Andres')
    self.assertEqual('Hello ANDRES' , hello)
  
  def test_say_goodbye(self):
    """vamos a testear el metodo say goodbye"""
    goodbye = self.test_user.say_goodbye('DIEGO')
    self.assertEqual('Goodbye diego' , goodbye)


if __name__ == "__main__":
    unittest.main()