"""
How about building a simple To-Do List application using Python? This project would allow you to apply your knowledge of loops, lists, dictionaries, classes, functions, and error handling. Here's a basic outline of what you could include in your To-Do List project:

1. **User Interface**: You can create a command-line interface where users can interact with the To-Do List application. You can use Python's `input()` function to get user input.

2. **Add Task**: Allow users to add tasks to their to-do list. When a user adds a task, it should be stored in a list or dictionary.

3. **View Tasks**: Users should be able to view all the tasks currently in their to-do list.

4. **Mark Task as Completed**: Allow users to mark tasks as completed. You could implement this by removing the task from the to-do list or marking it as completed in some way.

5. **Save and Load Tasks**: Implement functionality to save the to-do list to a file so that users can access their tasks even after closing the application. You can use file handling operations like `open()` to save and load tasks from a text file.

6. **Error Handling**: Implement error handling to handle cases like invalid input from the user or file I/O errors.

This project will allow you to practice many fundamental concepts of Python programming and help reinforce what you've learned in our conversations. Plus, it's a practical application that you can use to manage your tasks!
"""


listoftasks={}

def main():
    task=input(" write task here")
    importance=input(" priority from 1-5")
    listoftasks[task]=importance
    f=open("listofthings.txt",'w')
    f.write(f"{task}:{importance}")
    
    

def view(listoftasks):
    for key,value in listoftasks.items():
        print (key,value)

def complete(task):
    e=" this task does not exist"
    try:
        if task in listoftasks:
            listoftasks[task]="complete"
    except Exception as e:
        print(e)
    














if __name__ == '__main__':
    main()
    view(listoftasks)
