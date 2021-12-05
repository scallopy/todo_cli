import sys
import datetime


# help function
def help():
    help_message = """Usage : -
        $ ./todo add "todo item" # Add a new todo
        $ ./todo ls              # Show remaining todos
        $ ./todo del NUMBER      # Delete a todo
        $ ./todo done NUMBER     # Compleate a todo
        $ ./todo help            # Show usage
        $ ./todo report          # Statistics
        """
    print(help_message)


# function to add item in todo list
def add(todo_item):
    with open('todo.txt', 'a') as f:
        f.write(todo_item)
        f.write("\n")
    print("Added todo: \"{}\"".format(todo_item))


# Function to print the todo list items
def ls():
    todos = read_todo_from_file()
    inx = len(todos)
    content = []
    for todo in reversed(todos):
        cont = [("[{}] {}\n".format(inx, todo)), inx]
        inx -= 1
        content.append(cont)
    for item in content:
        print(item[0])


# Function to complete a todo
def done(no):
    try:
        todos = read_todo_from_file()
        no = int(no) - 1
        f = open('done.txt', 'a')
        st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + todos[no]

        f.write(st)
        f.close()

        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i != todos[no]:
                    f.write(i)
            f.truncate()
        print("Market todo #{} as done.".format(no+1))

    except Exception:
        print("Error: todo #{} does not exist.".format(no+1))


# Function to show report/statistics of todo list
def report():
    todos = read_todo_from_file()
    try:
        completed = []
        don = {}
        cont = ""
        with open('done.txt', 'r') as nf:
            c = 0
            for line in nf:
                c = c + 1
                don.update({c: line})

            cont += (
                '{} Pending : {} Compleated : {}'
                .format(str(datetime.datetime.today()).split()[0],
                        len(todos), len(don))
            )
        for value in don.values():
            completed.append(value)

        content = {
            "cont": cont,
            "completed": completed
        }
        print(content["cont"])

    except Exception:
        print("There are not completed todos!")


# delete
def deL(no):
    try:
        no = int(no) - 1
        todos = read_todo_from_file()

        # utility function defined in main
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i != todos[no]:
                    f.write(i)
            f.truncate()
        print("Deleted todo #{}".format(no+1))

    except Exception:

        print("Error: todo #{} does not exist. Nothing deleted.".format(no+1))


# Main function and utility function
def read_todo_from_file():
    todos = []
    try:
        with open('todo.txt', 'r') as f:
            for line in f:
                line.strip('\n')
                todos.append(line)
        return todos
    except Exception:
        print("There are no pending todos!")


# Main program
if __name__ == '__main__':
    args = sys.argv

    if len(args) <= 1:
        help()
    else:
        try:
            args = sys.argv

            if (args[1] == 'del'):
                args[1] = 'deL'

            if (args[1] == 'add' and len(args[2:]) == 0):
                sys.stdout.write(
                    "Error: Missing todo string. Nothing added!".encode('utf8')
                )
            elif (args[1] == 'done' and len(args[2:]) == 0):
                sys.stdout.write(
                    "Error: Missing NUMBER for deleting todo.".encode('utf8')
                )
            elif (args[1] == 'deL' and len(args[2:]) == 0):
                sys.stdout.write(
                    "Error: Missing NUMBER for deleting todo.".encode('utf8')
                )
            else:
                globals()[args[1]](*args[2:])

        except KeyError:
            help()
