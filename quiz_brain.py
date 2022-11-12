class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}:{current_question.question} (True/False)?:")
        if response == current_question.answer:
            self.score += 1
        print(f"Your Score is {self.score}.")
