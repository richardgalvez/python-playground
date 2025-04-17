class NoteManager:

  def create_note(self, title: str, content: str) -> None:
    """
    Saves a new note with a title, content, and timestamp. Titles must be unique.
    """

    G

    # Raise ValueError if title or content is empty

  def get_note(self, title: str) -> dict:
    """
    Returns a note's details by its title.
    """

  def delete_note(self, title: str) -> None:
    """
    Removes a note from storage based on its title.
    """

  def list_notes(self) -> list(str):
    """
    Lists the titles of all existing notes.
    """


nm = NoteManager()

nm.create_note("Meeting Notes", "Walked through upcoming project deadlines.")
nm.get_note("Meeting Notes")
# Returns: {'title': 'Meeting Notes', 'content': 'Walked through upcoming project deadlines.', 'timestamp': '2025-04-17T18:25:43'.}

nm.list_notes()
# Returns: ['Meeting Notes']

nm.delete_note("Meeting Notes")
nm.get_note("Meeting Notes")  # Raises KeyError
