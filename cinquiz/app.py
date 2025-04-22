from flask import Flask, render_template, request, session, redirect, url_for

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


# Welcome screen with a 'Start Quiz' button
# -> POST or redirect to /quiz
@app.route("/")
def home():
    quiz_name = "Cinquiz"
    return render_template("index.html", name=quiz_name)


# GET: Displays the current question (one at a time) with a form
# POST: Submits an answer, updates progress, and loads the next question
# @app.route("/quiz", methods=['GET','POST'])

# Displays the user's total score + detailed review
# @app.route("/results")
# Show - total score, each question's: question, user's answer, visual indicator (check or X) if correct and the correct answer
