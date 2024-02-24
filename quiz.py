import requests
import random

class Quiz:
    def __init__(self, api_url):
        self.api_url = api_url
        self.questions = self.fetch_questions()
        self.score = 0

    def fetch_questions(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()['results']
        else:
            print("Failed to fetch questions from the API.")
            return []

    def display_question(self, question):
        print(f"Question: {question['question']}")
        user_answer = input("Your answer: ")
        correct_answer = question['correct_answer']
        if user_answer.lower() == correct_answer.lower():
            self.score += 5
            print("Correct! You earned 5 points.")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}")

    def run_quiz(self):
        try:
            random.shuffle(self.questions)
            num_questions = len(self.questions)
            i = 0
            while True:
                i += 1
                print(f"Question {i}:")
                self.display_question(self.questions[i % num_questions])
                stop = input("Type 'q' to stop the quiz, or press Enter to continue: ")
                if stop.lower() == 'q':
                    break
        except KeyboardInterrupt:
            print("\nQuiz interrupted. Exiting...")
        print(f"Quiz completed! Your final score is: {self.score}")

if __name__ == "__main__":
    api_url = "https://opentdb.com/api.php?amount=5&type=multiple"
    quiz = Quiz(api_url)
    quiz.run_quiz()