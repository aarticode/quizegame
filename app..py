#Quize question answer

print ("Quize game")
print ("-----------------")
print ("want start")
start= input ("if yes,press 'y':")
if (start=='y'):
    print("what is the shortcut key of cut?")
    print("A.) Ctrl +C")
    print("B.) Ctrl +X")
    print("C.) Ctrl +V")
    print("D.) Ctrl +P")
    ans = input("write your answer | A,B,C,D:")
    if (ans=="B"):
        print ("carrect answer")
    else:
        print ("incorrect answer")
else:
    print("Game closed")