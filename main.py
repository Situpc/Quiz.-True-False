from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    text = questions["text"]
    answer = questions["answer"]
    question = Question(text, answer)
    question_bank.append(question)


user_questions = QuizBrain(question_bank)

while user_questions.still_has_questions():
    user_questions.next_question()

print("You've completed the quiz.")
print(f"You final score was: {user_questions.score} out of {user_questions.question_number}")