class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list


    def next_question(self) -> None:
        for question in self.questions_list:
            print(f"{self.question_number + 1}. {question.text}")
            user_choice = self.validate_choice()
            self.check_answer(user_answer=user_choice, correct_answer=question.answer)
            self.question_number += 1

    def validate_choice(self) -> str:
        while True:
            choice = input("True or False? ").lower()
            if choice in ["true", "false"]:
                return choice
            if choice == "t":
                return "true"
            if choice == "f":
                return "false"
        
    def check_answer(self, user_answer, correct_answer) -> int:
        if user_answer == correct_answer.lower():
            print("Correct answer!")
            self.score += 1
        else:
            print("Wrong Answer!")
        print(f"The answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number + 1}")
        
    def get_scores(self) -> tuple[int, int]: 
        return self.score, len(self.questions_list)

    def still_has_questions(self) -> bool:
        return self.question_number > len(self.questions_list)