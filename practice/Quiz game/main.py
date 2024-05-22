question=open("question.txt","r")
answer=open("q_answer.txt","r")
qus=list(question.readlines())
ans=list(answer.readlines())

for i in range(0,len(qus),2):
    print(qus[i])
    print(qus[i+1])

    user=(input("Enter your OPTION: "))
    user=user.upper()
    if (user+"\n")==ans[i]:
        print("CONGRATS!!! You gave correct answer..................\n")
    else:
        print("SORRY!!! You gave wrong answer..................\n")
    

question.close()
answer.close()


