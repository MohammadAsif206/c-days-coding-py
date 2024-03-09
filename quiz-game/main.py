# TODO: Create a class
from data import question_data
from question_modal import Question
from quiz_brain import QuizBrain

print(len(question_data))
question_bank = []
for i in range(len(question_data)):
    dic = question_data[i]
    q_a = Question(dic["text"], dic["answer"])
    question_bank.append(q_a)

quiz = QuizBrain(question_bank)
while quiz.still_has_next():
    quiz.get_current_question()
print(f"You have completed the Quiz, your final score was {quiz.score}/{quiz.question_number}")
