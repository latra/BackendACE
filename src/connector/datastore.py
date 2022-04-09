from google.cloud import datastore
from google.oauth2.service_account import Credentials

from exceptions import QuestionNotFoundException
import logging
import random
class DatastoreConnector:
    def __init__(self, credentials: Credentials = Credentials.from_service_account_file("credentials.json")):
        self.datastore_client = datastore.Client(credentials=credentials)
        
    def get_question(self, question_id: int):
        key = self.datastore_client.key('questions', question_id)
        return self.datastore_client.get(key)

    def get_random_question(self):
        query = self.datastore_client.query(kind='questions')
        query.keys_only()
        return self.datastore_client.get(random.choice(list(query.fetch())).key)


    def add_question_record(self, question_id: int, category_id: int, user_id: str, answered_correctly: bool):
        pass