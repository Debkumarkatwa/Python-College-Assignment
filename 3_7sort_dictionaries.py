d = {
    "five": 5,
    "one": 1,
    "two": 2,
    "seven": 7,
    "four": 4,
    "eight": 8,
    "six": 6,
    "three": 3
}
def sort_dict(a):
    return a[1]

new_d=sorted(d.items(), key=sort_dict)
print(new_d)