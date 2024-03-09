class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def get_current_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f" Q{self.question_number}: {current_q.text} (True/False?)")
        self.check_answer(user_answer, current_q.answer)

    def actual_answer(self):
        current_a = self.question_list[self.question_number]
        return current_a.answer

    def still_has_next(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            print("You got it right! ")
            self.score += 1

        else:
            print("You did not answer it correctly.")
        print(f"You answered {user_answer}, the actual answer is {actual_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
