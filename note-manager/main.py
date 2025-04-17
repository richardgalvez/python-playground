from datetime import datetime
import json

class NoteManager:

  def create_note(self, title: str, content: str) -> None:
    """
    Saves a new note with a title, content, and timestamp. Titles must be unique.
    """

    if len(title) <= 0 or len(title) <= 0:
      raise ValueError("Title or Content provided cannot be empty.")

    details = {
        "title": title,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }

    note = json.dumps(details)

    # TODO: Implement validation for unique titles.
    # Scan file for 'title': title in the current notes.json

    # if not found:
    file = open("notes.json", "a")
    file.write(note)
    file.write("\n")
    file.close()

    print_out = open("notes.json")
    print(print_out.read())
    print_out.close()

  def get_note(self, title: str) -> dict:
    """
    Returns a note's details by its title.
    """
    # Read notes.json (needs to find the correct line by title most likely?)
    # Maybe read line by line until thei matching string is found? Then stop
    file = open("notes.json")
    print(file.read())
    # print line by line, but only ready each string up to len('{"title":') + len(title)
    file.close()
    # Load the correct variable into:
    # json.loads(title) or use variable with json.loads(x)
    # TODO: Implement validation to raise KeyError when trying to get notes that don't exist.
    # Return title["content"] / x["content"]


  def delete_note(self, title: str) -> None:
    """
    Removes a note from storage based on its title.
    """
    # TODO: Implement validation to raise KeyError when trying to delete notes that don't exist.

  def list_notes(self) -> list[str]:
    """
    Lists the titles of all existing notes.
    """
    # Similar to get_note, just read the notes.json file and scan for the titles.


nm = NoteManager()

# nm.create_note("Go food shopping", "Buy items from grocery list at the supermarket.")
nm.get_note("Go food shopping")

# nm.create_note("Meeting Notes", "Walked through upcoming project deadlines.")
# nm.get_note("Meeting Notes")
# Returns: {'title': 'Meeting Notes', 'content': 'Walked through upcoming project deadlines.', 'timestamp': '2025-04-17T18:25:43'.}

# nm.list_notes()
# Returns: ['Meeting Notes']

# nm.delete_note("Meeting Notes")
# nm.get_note("Meeting Notes")  # Raises KeyError
