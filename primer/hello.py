print(5+6)
"comment"
""" otro comment"""
condi = "3"
if condi == 3:
    print("si")
else:
    print("no")
print("Fuera del if")


def potatocost(potatoprice, amount, potatotype):
    cost = potatoprice*amount
    print(potatotype)
    return cost

print(potatocost(23, 3, 4.3))

filearray = [1,4,7,8]
print(filearray)

filetuple = (3,5,7)
print(filetuple)

filelist = [3,45,45,4,3]
fileset = set(filelist)
print(fileset)

print(type(fileset))

filedic = {"a":34542, "b":454545, "c":3699}
filedic["a"]

filedic["c"]

print(filedic)

with open("prueba.txt", 'w') as file:
    file.write("prueba with open")

list = list(range(5, 10, 1))
print(list)
[5, 6, 7, 8, 9]
for item in list:
    print(item)
    }

    File
    "<input>", line
    3
    }
    ^
    SyntaxError: invalid
    syntax
    for item in list:
        print(item)

    5
    6
    7
    8
    9
    for item in list:
        file.write(item)

    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    2, in < module >
            TypeError: write()
    argument
    must
    be
    str, not int

    list = list(range(5, 10, 1))
    with open("prueba.txt", 'a') as file:
        file.write("list")


    print(list)

    for item in list:
        print(item)

    5
    6
    7
    8
    9



