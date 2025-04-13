''' Take inputs from the question_data and create objects'''

class Questions:
    '''This module defines the Question class,
    representing a quiz question with its text and answer.'''
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
