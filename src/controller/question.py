from src.connector.datastore import DatastoreConnector
class Question:
    def __init__(self, question_id, question_text, answer_text, options, category_id = None):
        self.question_id = question_id
        self.question_text = question_text
        self.question_category = category_id
        self.answer_text = answer_text
        self.options = options
    
def get_random_question():
    question = DatastoreConnector().get_random_question()
    return Question(question_id=question.key.id, question_text=question['title'], answer_text=question['answer'], options=question['options'])

def verify_answer(question_id, answer):
    question = DatastoreConnector().get_question(question_id)
    return question['answer'] == answer
