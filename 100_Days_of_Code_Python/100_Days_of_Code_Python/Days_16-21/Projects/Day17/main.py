from question_model import Question 
from data import question_data
from quiz_brain import QuizBrain

# Create question bank from question_data
questions_bank = []

# For each item in question_data, create a Question object and add it to questions_bank
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    question = Question(question_text, question_answer)
    questions_bank.append(question)

# Initialize QuizBrain with the question bank
quiz = QuizBrain(questions_bank)

# Start the quiz
while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")