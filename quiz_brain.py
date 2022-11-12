class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}:{current_question.question} (True/False)?:")
        self.check_answer(response, current_question.answer)

    def check_answer(self, response, correct_answer):
        if response.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong answer")

        print(f"Right Answer is {correct_answer}.\nYour Score is {self.score}/{self.question_number}.\n")
        # print(f"Your Score is {self.score}/{self.question_number}.")
