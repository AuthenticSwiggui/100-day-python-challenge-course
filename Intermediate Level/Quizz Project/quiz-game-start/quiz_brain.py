class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        for question in self.questions_list:
            print(f"{self.question_number + 1}. {question.text}")
            user_choice = self.validate_choice()


    def validate_choice(self) -> str:
        while True:
            choice = input("True or False?").lower()
            if choice in ["true", "false"]:
                return choice