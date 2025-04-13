from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Questions(data['text'], data['answer']))

quiz = QuizBrain(question_bank)

quiz.next_question()
