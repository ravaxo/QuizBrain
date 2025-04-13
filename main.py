'''This module call the class and make the game run'''

from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Questions(data['text'], data['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!!!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")
