class FeedbackCollector:

    def submit_feedback(self, user: str, rating: int, comments: str = "") -> None:
        """
        Submits feedback with a username, 1-5 start rating, and optional comments.
        """

    def get_feedback_summary(self) -> dict:
        """
        Returns summary data:
        - total submissions
        - average rating
        - count per rating level (1-5)
        """

    def list_feedback(self, min_rating: int = 1) -> list[dict]:
        """
        Returns all feedback entries with rating >= min_rating.
        """


fc = FeedbackCollector()

fc.submit_feedback("alicej", 5, "Loved the service!")
fc.submit_feedback("bobk", 3)

fc.get_feedback_summary()
# Returns:
# {
#   "total": 2,
#   "average_rating": 4.0
#   "ratings_breakdown": {"5": 1, "4": 0, "3": 1, "2": 0, "1": 0 }
# }

fc.list_feedback(4)
# Returns only entries with rating 4 or 5.
