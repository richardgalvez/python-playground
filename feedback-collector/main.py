from datetime import datetime
from pathlib import Path
import json


class FeedbackCollector:
    def submit_feedback(self, user: str, rating: int, comments: str = "") -> None:
        """
        Submits feedback with a username, 1-5 start rating, and optional comments.
        """
        timestamp = datetime.now().isoformat()
        feedback_details = {
            "user": user,
            "rating": rating,
            "comments": comments,
            "timestamp": timestamp,
        }
        feedback_item = json.dumps(feedback_details) + "\n"

        if len(user) <= 0:
            raise ValueError("The username is not defined (empty string).")
        elif (rating < 1) or (rating > 5):
            raise ValueError("Rating is invalid (not between 1 and 5).")
        else:
            file_location = Path("./feedback.json")
            if not file_location.is_file():
                print("File does not exist, creating now.")
                with open("feedback.json", "w") as newfile:
                    newfile.write(feedback_item)
            else:
                with open("feedback.json", "a") as file:
                    file.write(feedback_item)

            print("Feedback added to file.")

    def _gather_feedback(self) -> list[dict]:
        feedback_list = []
        with open("feedback.json", "r") as file:
            for line in file:
                feedback_list.append(json.loads(line))

        return feedback_list
        # TODO: Raise IOError if the file is corrupted or cannot be loaded (in use?).

    def get_feedback_summary(self) -> dict:
        """
        Returns summary data:
        - total submissions
        - average rating
        - count per rating level (1-5)
        """
        # TODO: Get data from helper function.
        feedback_list = self._gather_feedback()

        print(feedback_list[0]["user"])
        # TODO: Calculate total amount of submissions (amount of lines).

        # TODO: Calculate the average rating.
        # Return rating number of a submission.
        # Return rating numbers of all submissions.
        # Add values to a variable and divide by the total amount of submissions.

        # TODO: Return data for ratings_breakdown
        # Calculate the amount if ratings for each rating level (1-5).
        # Get amount of ratings for 5 star submission.
        # Get the amount of ratiings for the rest of the levels.

    def list_feedback(self, min_rating: int = 1) -> list[dict]:
        """
        Returns all feedback entries with rating >= min_rating.
        """
        # TODO: Gather ratings data from the helper function.
        # TODO: Raise ValueError if:
        # min_rating is invalid


##### TESTING SECTION #####

fc = FeedbackCollector()

fc.submit_feedback("alicej", 5, "Loved the service!")
fc.submit_feedback("bobk", 3)
fc.submit_feedback("cooperf", 2, "Not the greatest experience.")
fc.submit_feedback("davidg", 4)
fc.submit_feedback("brucew", 1, "Awful service.")

fc.get_feedback_summary()
# Returns:
# {
#   "total": 2,
#   "average_rating": 4.0
#   "ratings_breakdown": {"5": 1, "4": 0, "3": 1, "2": 0, "1": 0 }
# }

# fc.list_feedback(4)                   # Returns only entries with rating 4 or 5.

### ERROR TESTING ###

# fc.submit_feedback("", 5)             # Expected: ValueError 1 - username is an empty string
# fc.submit_feedback("perryp", 0)       # Expected: ValueError 2 - rating number is below 1
# fc.submit_feedback("heinzd", 20)      # Expected: ValueError 2 - rating number is above 5
# fc.submit_feedback("", 69)            # Expected: ValueError 1 and 2 (if either one is fixed) - username is an empty string, rating number is above 5
