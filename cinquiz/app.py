from flask import Flask, render_template, request, session, redirect
from pathlib import Path
import json

app = Flask(__name__)

app_name = "Cinquiz"


@app.route("/")
def home():
    return render_template("index.html", app_name=app_name)


# TODO: Prevent quiz reset unless the user finishes or returns to the homepage
# GET: Displays the current question (one at a time) with a form
# POST: Submits an answer, updates progress, and loads the next question
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    file_location = Path("./questions.json")
    quiz_data = []
    questions = []
    answers = []
    correct_index = []
    question_counter = 0
    correct_answers = 0
    wrong_answers = 0

    # Load from questions.json, then load those as needed.
    if not file_location.is_file():
        raise IOError(
            "File cannot be loaded. Please makes sure it exists and contains question data."
        )

    with open(file_location, "r") as file:
        for line in file:
            quiz_data.append(json.loads(line))

    def load_question(question_num: int) -> None:
        index_format = quiz_data[question_num - 1]

        questions.append(index_format[0])
        answers.append(index_format[1]["options"])
        correct_index.append(index_format[2]["correct_option_index"])

    # load_question(1)
    # load_question(2)
    # load_question(3)
    # load_question(4)
    # load_question(5)

    context = {
        "app_name": app_name,
        "title": "Quiz",
        "questions": questions,
        "answers": answers,
    }

    if request.method == "POST":
        # TODO: Display one question per page (select data from array/question.json
        # to serve dynamically - based on how many questions have been answered?)
        # TODO: Store submitted answer(s) in Flask's session
        # TODO: If refreshed, resumes at the current question
        # TODO: Move to the next question automatically on submission
        # TODO: Questions must be answered in sequence
        user_answer = request.form.get("answers")
        # TODO: Get index of correct answer and compare to user_answer
        if user_answer == answers[1]["answer"]:
            correct_answers += 1
            question_counter += 1
            print("Correct answers: " + str(correct_answers))
        elif user_answer is None:
            print("No answer selected.")
        else:
            wrong_answers += 1
            question_counter += 1
            print("Wrong Answers: " + str(wrong_answers))
        # TODO: If the user completes all questions, redirect to /results

    return render_template("quiz.html", **context)


# Displays the user's total score + detailed review
# Users can't skip ahead or visit /results early
@app.route("/results")
def results():
    # Show - total score, each question's: question, user's answer, visual indicator (check or X) if correct and the correct answer
    context = {"app_name": app_name, "user_score": 5}
    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
