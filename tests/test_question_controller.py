import unittest
from google.oauth2 import service_account


class TestQuestionController(unittest.TestCase):
    def test_get_random(self):
        from src.controller.question import get_random_question
        assert get_random_question() != None
    
    def test_verify_answer(self):
        from src.controller.question import verify_answer
        assert verify_answer(4594061889503232, 'max_concurrent_requests')
        assert not verify_answer(4596523341971456, 'patata')
       

if __name__ == '__main__':
    unittest.main()