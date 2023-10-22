import functions
import time

now = time.strftime("%a, %b %d, %Y %H:%M:%S")
print("The time is: ")
print(now)
while True:
    print("")
    decision = input("Type add, show, edit, complete or exit: ")
    # strip method strips away the space
    decision = decision.strip()
    if decision.startswith("add"):
        # the \n is added so that a new line is added. U can see the new line only if u print a string along wiht that string but since it's added to input, it wont show but it will show in todos.txt
        # the print function and writelines function can recognize the \n and not show it but other things take it in raw form. for example, the todos would contain ["todos\n", "todos2\n"] but
        # when printed, print recognizes it and prints it in seperate lines

        todo = decision[4:]

        # the program opens the text files and reads all the items there and adds it to the varaible todos as a list
        # also close files after ur done accessing it as diff segments of the code might interact in diff ways and mess up the file and its just a safe way

        # if the file isn't in the root directory if this app, just go to windows, find the file, find its adress on the top where its like "users\downlaods\new_file". Copy and pase that and ur good
        # dont forget to add a r before the "" because windows might recognize some special characters and do commands. For example, it might recognize \n and do zesty stuff. So, in order to ignore
        # the special characters, we add r
        todos = functions.get_todos()

        # readlines gives output in a list with multiple elemenets while file.read just gives output as strings

        todos.append(todo + "\n")

        # the open object is used to OPEN and access text files or any files and the
        # second parameter takes in w(write) or r(read) to decide what to do with that file
        # file = open("files/todos.txt", "w")
        # # writelines is a method for file objects and takes in lists as arguments
        #
        # # write will just add stuff to the document if u have several write statements without closing but if u  close it and do another write statement, it will re write the entire thign
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

        # you can also use just file.write(str) to add strs to the txt document
        #fi
        # the problem is that every time we run this, the text le gets cleared and re written and we lose the old data and thus, instead of just defining a empty list in the start, we will read the txt file
        # and then create a list from that and use

    # | is for strings but im not sure
    elif decision.startswith("show"):
        # you can also run for loops with strings except that it would be iterated over every character in a
        # string the enumerate function takes in list as input and gives out 2 outputs and thus we need to
        # variables in the for loop the first variable takes in the index of the value given by enumerate while
        # the second variable has the element in the list

        # file = open("files/todos.txt", "r")

        #with function has a default value of read mode so we dont have to include "r"
            # just using read will read the text file with a cursor and will stop at the end and if u try reading again, it wont work. The fix is to close and re open the file OR do readlines(NOT SURE ABT THIS ONE)
        todos = functions.get_todos()

            # file.close isnt needed when ur used with to open files becuase after the with operation runs, it automatically closes
            # file.close()

        # apart from the \n in the todos, the print line is adding an extra break line so we are stripping away the \n part ONLY WHILE PRINTING AND THE \N is still in docs.txt
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)

        # another way to do for loop is with list comprehension where the entire for loop can happen in 1 line
        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

        # this is another way to do the same thing without ennumerate function
        # for item in todos:
        #     index = todos.index(item)
        #     print(f"{index+1}.{item}")

    # case "edit":
    #     number = int(input("Please enter the number of the list that you would like to edit: "))
    #     number = number - 1
    #     todos[number] = new_todo
    #     print("")

    elif decision.startswith("edit"):
        try:
            number = decision[5:]
            number = int(number)
            number -= 1

            new_todo = input("Please enter the new todo: ")
            todos = functions.get_todos()
            todos[number] = new_todo + "\n"


            # open function in write mode creates "todos.txt" in the given location IF it doesnt exist but if it does, it just continues to work on it
            functions.write_todos(todos)
            print("")

            # file_read = open("files/todos.txt", "r")
            # todos = file_read.readlines()
            # todos[number] = new_todo + "\n"
            # file_read.close()
            #
            # file_write = open("files/todos.txt", "w")
            # present_todos = file_write.writelines(todos)
            # file_write.close()
            # print("")s

        except ValueError:
            print("Your command was invalid! Please try again!")
            #continue just starts another cycle of the loop (NOT SURE)
            continue

    elif decision.startswith("exit"):
        break

    elif decision.startswith("complete"):

        #we get an error when we try to complete a task that is not in the list and we get an index error
        try:
            number = decision[9:]
            number = int(number)
            number -= 1

            todos = functions.get_todos()
            stripped_todo = todos[number].strip("\n")
            print(f' "{stripped_todo}" was removed!')
            todos.pop(number)

            functions.write_todos(todos)
        except IndexError:
            print("The task that you are trying to complete doesn't exist! ")
            continue

    elif decision.startswith("clear"):
        todos = functions.get_todos()

        todos = []

        functions.write_todos(todos)
    # for any other input given by user, just use case along with a random variable and it functions as an conditional for every input that is not in the match case above
    else:
        print("Incorrect command")

    # # or is for other stuff
    # if decision == "add" or  decision == "show":
    #     print("it works")

print("Bye! ")
