import pickle as pk
dic={}

file=open("student_data.bat","wb")

while True:
    print("\n0. End dictionary")
    key=input("Enter Student Name::")
    if key in dic:
        print("Student Name is already in dictionary")
    elif key=="0":
        break
    else:
        value=input("Enter Student Marks::")
        dic[key]=value
        print(f"{key}'s data added to dictionary")
        
pk.dump(dic,file)
file=open("student_data.bat","rb")
data=pk.load(file)
print(data)

