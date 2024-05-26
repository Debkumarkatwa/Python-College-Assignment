question=open("question.txt","r")
answer=open("q_answer.txt","r")
qus=list(question.readlines())
ans=list(answer.readlines())

a=0
for i in range(1,len(qus),2):
    print(qus[i-1])
    print(qus[i])

    user=(input("Enter your OPTION: "))
    user=user.upper()
    if (user+"\n")==ans[a]:
        print("CONGRATS!!! You gave correct answer..................\n")
    else:
        print("SORRY!!! You gave wrong answer..................\n")
    

question.close()
answer.close()


