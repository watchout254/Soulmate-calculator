print("\t\t\t\tWelcome to Love Calculator!!!")
your = input("Enter your name please: ")
their = input("Enter his/her name kindly: ")

#concatenate the names
mates = your+their
#change to lower case
destiny = mates.lower()

#after concatenation, the name will be searched in the following to see how many times each letter appears
t = destiny.count('t')
r = destiny.count('r')
u = destiny.count('u')
e = destiny.count('e')
#add the variables since they are integers
true = t+r+u+e

l = destiny.count('l')
o = destiny.count('o')
v = destiny.count('v')
e = destiny.count('e')
#add the variables since they are integers
love = l+o+v+e

#concatenate the two above and convert to string since they are int
loveScore = int(str(true) + str(love))

#set the conditions using if statement
if loveScore < 10 or loveScore >90:
    print(f"Your love score is {loveScore}% and you will be like Romeo and Juliet")

elif loveScore >= 40 and loveScore<=50:
    print(f"Your love score is {loveScore}% and you are great together")

else:
    print(f"Your love score is {loveScore}%")

print("Thank you for trusting us! Come one acome all")
