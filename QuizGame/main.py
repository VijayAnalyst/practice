from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_bank = []
for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    new_question = Question(q_text = question_text, q_answer = question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)


while quiz.still_has_questions():
    quiz.next_question()

if quiz.still_has_questions() == False:
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}.") 