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

      print("New note added.")


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
      print(desired_note)
      return desired_note


  def delete_note(self, title: str) -> None:
    """
    Removes a note from storage based on its title.
    """
    line_count = 0
    found_title = ""

    # Search for note to be deleted based on title
    infile = open("notes.json", "r").readlines()
    for i in infile:
      line_count += 1
      if i[11:11 + len(title)] == title:
        found_title = i[11:11 + len(title)]
        break
    
    # Detect if note exists, and if so, proceed to "delete" by overwriting notes.json file with all lines except the note that was specified by its title.
    if (found_title != title):
      raise KeyError("Note cannot be deleted as it does not exist.")
    else:
      with open("notes.json", "w") as outfile:
        for index, line in enumerate(infile):
          if index != line_count - 1:
            outfile.write(line)

      print("Note deleted.")


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
    return note_titles


### Testing Section ###

nm = NoteManager()

# nm.create_note("Go food shopping", "Buy items from grocery list at the supermarket.")
# nm.get_note("Go food shopping")

# nm.create_note("Develop new mini-app", "Practice programming and software development.")
# nm.get_note("Develop new mini-app")

# nm.create_note("Clean up backyard", "Put equipment away spread out across the backyard.")
# nm.get_note("Clean up backyard")

# nm.create_note("Cook dinner", "Season meats, prepare veggies, and cook to serve dinner.")
# nm.get_note("Cook dinner")

# nm.create_note("Meeting Notes", "Walked through upcoming project deadlines.")
# nm.get_note("Meeting Notes")

nm.list_notes()

# nm.delete_note("Develop new mini-app")
# nm.delete_note("Meeting Notes")

# nm.list_notes() # List all notes after recent deletion.

# nm.create_note("", "asdf") # At least 1 empty value - should raise ValueError.
# nm.get_note("Eat breakfast")  # Doesn't exist - should raise KeyError.
# nm.delete_note("Eat breakfast") # Doesn't exist - should raise KeyError.
# nm.get_note("Meeting Notes")  # Doesn't exist after deletion - should raise KeyError.
