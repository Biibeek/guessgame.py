print("welcome to my computer quiz!!!")
response=input("Do you want to participate??? ")
if response.lower()!="yes":
    quit()
print("ok let's get started!")
score=0
ans=input("what does cpu stand for? ")
if ans.lower()=="central processing unit":
    print("correct")
    score +=1
else:
    print("incorect answer")

ans=input("what does AI stand for? ")
if ans.lower()=="artificial intelligence":
    print("correct")
    score +=1
else:
    print("incorect answer")

ans=input("what does RAM stand for? ")
if ans.lower()=="random access memory":
    print("correct")
    score +=1
else:
    print("incorect answer")

print(f"your score is {score}")