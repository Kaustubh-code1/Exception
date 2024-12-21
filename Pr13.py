# Hi there!!!
try:
    x,y =eval(input("Hi, this is K.Kaustubh.(not Veer). Please enter age and current year separated by comma. "))
    bornyear=y-x
    print("You were born in",bornyear)
    if x%2==0:
        print("Age is even")
    else:
        print("Age is odd")
    if bornyear%4==0:
        print("Birth year is leap year.")
    else:
        print("")

#except x>y:
#    print("Enter correct info") #???
except SyntaxError:
    print("Separate by comma")
except NameError:
    print("Enter only numbers")
else:
    print("  ")
finally:
    print("^ ** ^")