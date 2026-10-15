notes = [12, 5, 18, 15, 9]
notes.remove(max(notes))
notes.remove(min(notes))
moyenne = sum(notes) / len(notes)
print(moyenne)