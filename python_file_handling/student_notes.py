while True:

    note = input("Enter a note: ")

    with open("notes.txt", "a") as f:
        f.write(note + "\n")

    choice = input("Add another note? (yes/no): ")

    if choice == "no":
        break

print("Notes saved successfully")