import unittest
from google.oauth2 import service_account


class TestDatastoreConnector(unittest.TestCase):
    def test_get_query(self):
        from connector.datastore import DatastoreConnector
        from exceptions import QuestionNotFoundException
        from google.cloud.datastore import Entity

        credentials = service_account.Credentials.from_service_account_file("credentials.json")

        datastore_connector = DatastoreConnector(credentials)
        assert datastore_connector.get_question(4561338969882624) != None
        assert datastore_connector.get_question(1234546789237844) == None
    
    def test_random_question(self):
        from connector.datastore import DatastoreConnector
        from exceptions import QuestionNotFoundException
        from google.cloud.datastore import Entity

        credentials = service_account.Credentials.from_service_account_file("credentials.json")

        datastore_connector = DatastoreConnector(credentials)
        assert datastore_connector.get_random_question() != None

if __name__ == '__main__':
    unittest.main()