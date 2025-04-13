"""This module implements the QuizBrain class, which manages the flow of a true/false quiz."""

class QuizBrain:
    '''Manages the quiz flow, including presenting questions, 
    checking answers, and keeping track of the score.'''

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        '''checks if there are more questions and returns True or False'''
        return len(self.question_list) > self.question_number


    def next_question(self):
        '''proceed to the questions and get the user input'''
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} {'True/False'}: ").title()
        self.check_answer(user_answer, question.answer)


    def check_answer(self, user_answer, correct_answer):
        '''get the user answer, correct answer and if correct prints the score'''
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"Your current score: {self.score}/{self.question_number}")
        print('\n')
