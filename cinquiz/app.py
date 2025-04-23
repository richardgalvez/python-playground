from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

# -- Quiz Data
# Use a list of 5 fixed trivia questions, each have:
# question_text: str
# options: list of 4 answer strings
# correct_option_index: int (0-based index for the correct answer)
# TODO: Try via Python first, then use the questions.json file

# -- Core Logic:
# One question per page
# When an answer is selected and submitted, store in Flask's session
# Move to the next question automatically on submission
# If the user completes all questions, redirect to /results

# -- Input validation & Flow:
# Questions must be answered in sequence
# Users can't skip ahead or visit /results early
# If they refresh during the quiz, resumes at the current question
# Prevent quiz reset unless the user finishes or returns to the homepage

# Each view should be rendered using an HTML template with Jinja2

app_name = "Cinquiz"


# Welcome screen with a 'Start Quiz' button
# -> POST or redirect to /quiz
@app.route("/")
def home():
    return render_template("index.html", app_name=app_name)


questions = [
    {"question": "What is the capital of New York?"},
    # {"question": "Who is the main character of Kung Fu Panda?", "answer": "Po"},
    # {"question": "Where is the United States located?", "answer": "North America"},
    # {"question": "How fast can bees fly on average?", "answer": "50 MPH"},
    # {"question": "What year was YouTube created?", "answer": "2005"},
]

answers = [
    {"answer": "New Delhi"},
    {"answer": "Albany"},
    {"answer": "Austin"},
    {"answer": "Little Rock"},
]


# GET: Displays the current question (one at a time) with a form
# POST: Submits an answer, updates progress, and loads the next question
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    question_counter = 0
    correct_answers = 0
    wrong_answers = 0

    # Count how many questions have been answered
    # TODO: Questions shown need to have 4 answers, each with their own radio buttons
    context = {
        "app_name": app_name,
        "title": "Quiz",
        "questions": questions,
        "answers": answers,
    }
    return render_template("quiz.html", **context)


# Displays the user's total score + detailed review
@app.route("/results")
def results():
    # Show - total score, each question's: question, user's answer, visual indicator (check or X) if correct and the correct answer
    context = {"app_name": app_name, "user_score": 5}
    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
