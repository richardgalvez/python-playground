from datetime import datetime
import json

class NoteManager:

  def create_note(self, title: str, content: str) -> None:
    """
    Saves a new note with a title, content, and timestamp. Titles must be unique.
    """
    details = {
        "title": title,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    note = json.dumps(details)
    title_exists = False

    if len(title) <= 0 or len(title) <= 0:
      raise ValueError("Title or Content provided cannot be empty.")

    # Check for existing note based on inital JSON formatting + title, set flag to True if so.
    file = open("notes.json")
    for i in file:
      if i[11:11 + len(title)] == title:
        title_exists = True
    file.close()

    # Based on flag, raise error if already exists or proceed to create the new note.
    if title_exists == True:
      raise ValueError("This is the title of a note that already exists, please use a unique title name.")
    else:
      file = open("notes.json", "a")
      file.write(note)
      file.write("\n")
      file.close()

      print("Added new note: " + note)


  def get_note(self, title: str) -> dict:
    """
    Returns a note's details by its title.
    """
    desired_note = ""

    file = open("notes.json")
    for i in file:
      if i[11:11 + len(title)] == title:
        desired_note = i
    file.close()

    if len(desired_note) == 0:
      raise KeyError("Note cannot be found as it does not exist.")
    elif len(desired_note) >= 1:
      return print(desired_note)


  def delete_note(self, title: str) -> None:
    """
    Removes a note from storage based on its title.
    """
    line_count = 0
    desired_note = ""
    note_deleted = False

    # Read operation: Search for note to be deleted based on title
    with open("notes.json") as file:
      for i in file:
        line_count += 1
        if i[11:11 + len(title)] == title:
          print("Found match to be deleted: " + i)
          # Logic to delete - it would have to remove/zero out the string and write result to the file
          desired_note = i
    print(line_count)

    # Write operation: Overwrite the note found based on line number to "" (empty),
    # with open("notes.json", "w") as file:

    # TODO: Implement validation to raise KeyError when trying to delete notes that don't exist.
    if (desired_note != title) and (note_deleted == False):
      raise KeyError("Note cannot be deleted as it does not exist.")
    elif note_deleted == True:
      # print("Note deleted successfully.")
      print("Note will get deleted flag is True.")


  def list_notes(self) -> list[str]:
    """
    Lists the titles of all existing notes.
    """
    note_titles = []

    # Load notes line by line from JSON format into dict format, pick out "title" key only from each, then append to final array for display.
    file = open("notes.json")
    for i in file:
      line = i
      line_dict = json.loads(line)
      title_key = line_dict["title"]
      note_titles.append(title_key)
    file.close()

    print(note_titles)


nm = NoteManager()

# nm.create_note("Go food shopping", "Buy items from grocery list at the supermarket.")
# nm.get_note("Go food shopping")

# nm.create_note("Develop new mini-app", "Practice programming and software development.")
# nm.get_note("Develop new mini-app")

# nm.get_note("Eat breakfast")  # Doesn't exist - should raise error.

# nm.create_note("Meeting Notes", "Walked through upcoming project deadlines.")
# nm.get_note("Meeting Notes")

# nm.list_notes()

# nm.delete_note("Eat breakfast") # Doesn't exist - should raise error.

nm.delete_note("Meeting Notes")
nm.get_note("Meeting Notes")  # Raises KeyError
