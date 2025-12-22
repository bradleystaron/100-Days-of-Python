# This file contains the QuizBrain class which manages the quiz logic for the quiz game.

# Class to manage the quiz logic
class QuizBrain:
    
    # Initialize with a list of questions
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # Method to ask the next question in the list
    def next_question(self):
        current_question = self.question_list[self.question_number] # Get current question
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)

    # Method to check if there are still questions left
    def still_has_questions(self):
        return self.question_number < len(self.question_list) # Return True if more questions are available
    
    # Method to check the user's answer against the correct answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
