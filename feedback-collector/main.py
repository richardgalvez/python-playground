from datetime import datetime
import json

class FeedbackCollector:

    def submit_feedback(self, user: str, rating: int, comments: str = "") -> None:
        """
        Submits feedback with a username, 1-5 start rating, and optional comments.
        """
        timestamp = datetime.now().isoformat()
        feedback_details = {
                "title": user,
                "rating": rating,
                "comments": comments,
                "timestamp": timestamp
        }
        feedback_item = json.dumps(feedback_details) + "\n"

        if (len(user) <= 0):
            raise ValueError("The username is not defined (empty string).")
        elif (rating < 1) or (rating > 5):
            raise ValueError("Rating is invalid (not between 1 and 5).")
        else:
            # TODO: On first run, initialize feedback.json file if it does not exist.
            # If feedback.json cannot be found/ does not exist: create file

            with open('feedback.json', 'a') as file:
                file.write(feedback_item)

            print("Feedback added to file.")

    # TODO: Define helper function/method for the below's similar functionality related to reading the file (_gather_feedback).
        # TODO: Raise IOError if the file is corrupted or cannot be loaded (in use?).


    def get_feedback_summary(self) -> dict:
        """
        Returns summary data:
        - total submissions
        - average rating
        - count per rating level (1-5)
        """
        # This may need to be in JSON dict format.
        total = 0
        average_rating: 0.0
        ratings_breakdown = []
        # TODO: Get data from the helper function and put in the required format (dict).

    def list_feedback(self, min_rating: int = 1) -> list[dict]:
        """
        Returns all feedback entries with rating >= min_rating.
        """
        # TODO: Raise ValueError if:
        # min_rating is invalid


##### TESTING SECTION #####

fc = FeedbackCollector()

fc.submit_feedback("alicej", 5, "Loved the service!")
fc.submit_feedback("bobk", 3)

# fc.get_feedback_summary()
# Returns:
# {
#   "total": 2,
#   "average_rating": 4.0
#   "ratings_breakdown": {"5": 1, "4": 0, "3": 1, "2": 0, "1": 0 }
# }

# fc.list_feedback(4)
# Returns only entries with rating 4 or 5.

### ERROR TESTING ###

# fc.submit_feedback("", 5)           # Expected: ValueError 1 - username is an empty string
# fc.submit_feedback("perryp", 0)     # Expected: ValueError 2 - rating number is below 1
# fc.submit_feedback("heinzd", 20)    # Expected: ValueError 2 - rating number is above 5
# fc.submit_feedback("", 69)            # Expected: ValueError 1 and 2 (if either one is fixed) - username is an empty string, rating number is above 5
