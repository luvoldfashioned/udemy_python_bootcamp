from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text = question_text, q_answer = question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():             #if quiz still has questions remanining
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")
