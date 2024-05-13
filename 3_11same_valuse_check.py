def count_same_values(values, my_dict):
    c=0
    for i in my_dict.values():
        if i==values:
            c+=1
        
    if c>0:
        print(f"The value '{values}' exists in the dictionary for {c} keys.")
    else:
        print(f"The value '{values}' does not exist in the dictionary.")

my_dict = {'name': 'john', 'age': 25, 'city': 'New York','nick_name': "john"}
values=input("Enter the value to check: ")

count_same_values(values, my_dict)