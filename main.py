import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("guess the number:"))
    
    if(a>n):
        print("lower the number")
        guesses +=1
    elif(a<n):
        print("higher num plzzz")
        guesses +=1
print(f"you have guesses the correct number {n} in {guesses} attempt")