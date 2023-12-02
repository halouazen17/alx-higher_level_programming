#!/usr/bin/python3
def no_c(my_string):
    alx = ""
    for i in range(len(my_string)):
        if (my_string[i] != "c" and my_string[i] != "C"):
            alx += my_string[i]
    return alx
