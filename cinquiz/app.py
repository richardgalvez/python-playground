from flask import Flask, render_template, request, session, redirect
from pathlib import Path
import json

app = Flask(__name__)

app_name = "Cinquiz"

app.secret_key = "CINQUIZ_SECRET_KEY"


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
    question_counter = 1
    correct_answers = 0
    wrong_answers = 0
    quiz_complete = False

    context = {
        "app_name": app_name,
        "title": "Quiz",
        "questions": questions,
        "answers": answers,
    }

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

        # Clear question already loaded.
        questions.clear()
        answers.clear()
        correct_index.clear()

        questions.append(index_format[0])
        answers.append(index_format[1]["options"])
        correct_index.append(index_format[2]["correct_option_index"])

    load_question(question_counter)

    if request.method == "POST":
        # TODO: Display one question per page (select data from array/question.json
        # to serve dynamically - based on how many questions have been answered?)
        # TODO: Store submitted answer(s) in Flask's session
        # TODO: If refreshed, resumes at the current question
        # TODO: Move to the next question automatically on submission
        user_answer = request.form.get("answer")
        session["answer"] = request.form["answer"]
        correct_index_option = answers[0][correct_index[0]]

        question_counter += 1
        session["question_number"] = question_counter

        print(session)
        print(question_counter)
        print(user_answer)

        # Get user's answer and compare to the correct option's designated index number.
        if user_answer == correct_index_option:
            correct_answers += 1
            print("Correct answers: " + str(correct_answers))
            load_question(question_counter)
        elif user_answer is None:
            print("No answer selected.")
        elif user_answer != correct_index_option:
            wrong_answers += 1
            print("Wrong Answers: " + str(wrong_answers))
            load_question(question_counter)
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
