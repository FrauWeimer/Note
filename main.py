import sqlite3

class NotesApp:
    def __init__(self):
        self.conn = sqlite3.connect('notes.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS todo_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT,
                completed INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def create_note(self, title, content):
        self.cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        self.conn.commit()
        print("Note created.")

    def create_todo_item(self, task):
        self.cursor.execute('INSERT INTO todo_list (task) VALUES (?)', (task,))
        self.conn.commit()
        print("Task added to the to-do list.")

    def display_notes(self):
        self.cursor.execute('SELECT * FROM notes')
        notes = self.cursor.fetchall()
        print("Notes:")
        for note in notes:
            print(f"- {note[1]}: {note[2]}")

    def display_todo_list(self):
        self.cursor.execute('SELECT * FROM todo_list')
        todo_list = self.cursor.fetchall()
        print("To-Do List:")
        for item in todo_list:
            status = "[X]" if item[2] == 1 else "[ ]"
            print(f"{item[0]}. {status} {item[1]}")

    def complete_todo_item(self, item_id):
        self.cursor.execute('UPDATE todo_list SET completed = 1 WHERE id = ?', (item_id,))
        self.conn.commit()
        print("Task marked as completed.")

    def run(self):
        while True:
            print("\nSelect an action:")
            print("1. Create a note")
            print("2. Create a task in the to-do list")
            print("3. Display notes")
            print("4. Display to-do list")
            print("5. Mark a task as completed")
            print("6. Exit")

            choice = input("Enter the action number: ")

            if choice == "1":
                title = input("Enter the note title: ")
                content = input("Enter the note content: ")
                self.create_note(title, content)
            elif choice == "2":
                task = input("Enter the task for the to-do list: ")
                self.create_todo_item(task)
            elif choice == "3":
                self.display_notes()
            elif choice == "4":
                self.display_todo_list()
            elif choice == "5":
                item_id = input("Enter the task number to mark as completed: ")
                self.complete_todo_item(item_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the application
app = NotesApp()
app.run()
