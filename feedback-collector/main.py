from datetime import datetime
from pathlib import Path
import json


class FeedbackCollector:
    def submit_feedback(self, user: str, rating: int, comments: str = "") -> None:
        """
        Submits feedback with a username, 1-5 start rating, and optional comments.
        """
        file_location = Path("./feedback.json")
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
            if not file_location.is_file():
                print("File does not exist, creating now.")
                with open(file_location, "w") as newfile:
                    newfile.write(feedback_item)
            else:
                with open(file_location, "a") as file:
                    file.write(feedback_item)

            print("Feedback added to file.")

    def _gather_feedback(self) -> list[dict]:
        feedback_list = []
        file_location = Path("./feedback.json")

        if not file_location.is_file():
            raise IOError(
                "File cannot be loaded, please make sure it exists and add feedback."
            )

        with open(file_location, "r") as file:
            for line in file:
                feedback_list.append(json.loads(line))

        return feedback_list

    def get_feedback_summary(self) -> dict:
        """
        Returns summary data:
        - total submissions
        - average rating
        - count per rating level (1-5)
        """
        feedback_list = self._gather_feedback()
        total_submissions = len(feedback_list)
        rating_sum = 0
        average_rating = 0
        five_star = 0
        four_star = 0
        three_star = 0
        two_star = 0
        one_star = 0

        for item in range(total_submissions):
            rating_number = feedback_list[item]["rating"]
            rating_sum += rating_number
            if rating_number == 5:
                five_star += 1
            elif rating_number == 4:
                four_star += 1
            elif rating_number == 3:
                three_star += 1
            elif rating_number == 2:
                two_star += 1
            elif rating_number == 1:
                one_star += 1

        average_rating = rating_sum / total_submissions

        # Create structures for feedback summary.
        ratings_breakdown = {
            "5": five_star,
            "4": four_star,
            "3": three_star,
            "2": two_star,
            "1": one_star,
        }

        feedback_summary = {
            "total": total_submissions,
            "average_rating": round(average_rating, 2),
            "ratings_breakdown": ratings_breakdown,
        }

        print(feedback_summary)
        return feedback_summary

    def list_feedback(self, min_rating: int = 1) -> list[dict]:
        """
        Returns all feedback entries with rating >= min_rating.
        """
        feedback_list = self._gather_feedback()
        rated_feedback = []

        if (min_rating < 1) or (min_rating > 5):
            raise ValueError("Provided rating number is invalid (not between 1 and 5).")
        else:
            for item in range(len(feedback_list)):
                rating_number = feedback_list[item]["rating"]
                if rating_number >= min_rating:
                    rated_feedback.append(feedback_list[item])

        print(rated_feedback)
        return rated_feedback


##### TESTING SECTION #####

fc = FeedbackCollector()

# fc.submit_feedback("alicej", 5, "Loved the service!")
# fc.submit_feedback("bobk", 3)
# fc.submit_feedback("cooperf", 2, "Not the greatest experience.")
# fc.submit_feedback("davidg", 4)
# fc.submit_feedback("bridgetq", 4, "Pretty good service.")
# fc.submit_feedback("brucew", 1, "Awful service.")
# fc.submit_feedback("perryp", 5, "Wow, amazing service!")
# fc.submit_feedback("heinzd", 4, "Good service, but could be better.")
# fc.submit_feedback("fionag", 3, "Alright, not enough snacks...")
# fc.submit_feedback("frankr", 1, "It's trash!")
# fc.submit_feedback("juant", 2)
# fc.submit_feedback("estherm", 4)
# fc.submit_feedback("marias", 1, "Not good...")
# fc.submit_feedback("winniec", 5, "This is my new spot!")
# fc.submit_feedback("zackb", 3, "Service needs improvement, the rest is fine.")
# fc.submit_feedback("yolandae", 5)
# fc.submit_feedback("malcomy", 4, "Nice place.")
# fc.submit_feedback("ronw", 1)
# fc.submit_feedback("loisl", 1, "Avoid at all costs!")
# fc.submit_feedback("oscarj", 5, "Felt like a king!")
# fc.submit_feedback("ulyssesk", 2, "They need a lot more training...")

fc.get_feedback_summary()  # Returns dict with summary data or raises IOError if the file does not exist.

# fc.list_feedback(4)                   # Returns summary data: {'total': 21, 'average_rating': 3.1, 'ratings_breakdown': {'5': 5, '4': 5, '3': 3, '2': 3, '1': 5}}

### ERROR TESTING ###

# fc.submit_feedback("", 5)             # Expected: ValueError 1 - username is an empty string
# fc.submit_feedback("perryp", 0)       # Expected: ValueError 2 - rating number is below 1
# fc.submit_feedback("heinzd", 20)      # Expected: ValueError 2 - rating number is above 5
# fc.submit_feedback("", 69)            # Expected: ValueError 1 and 2 (if either one is fixed) - username is an empty string, rating number is above 5
# fc.list_feedback(100)                 # Expected: ValueError 3 - rating is not between 1 and 5
