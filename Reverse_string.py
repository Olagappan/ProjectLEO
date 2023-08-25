"""Write a program to reverse an integer in Python."""
string = input("please enter the name of the string:")
rev = ""
if  string.isdigit():
        print("Please enter the string rather than numbers")
else:
    for i in range(len(string)-1,-1,-1):
        rev = rev + string[i]
    print(rev)


