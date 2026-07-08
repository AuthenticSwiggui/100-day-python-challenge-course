from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

try:
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_answer = Question(question_text, question_answer)
        question_bank.append(new_answer)

    quiz = QuizBrain(question_bank)
    quiz.next_question()
    
    print("You had finished the game!")
    print(f"Your final score is: {quiz.score} / {quiz.question_number}")
    
except KeyboardInterrupt:
    exit()