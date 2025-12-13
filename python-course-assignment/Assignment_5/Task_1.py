students = {
    'Alice':98,
    'Bob':87,
    'Niks':46,
    'Nicholas':89,
}
name = input("Enter name here :- ").capitalize()
if(name in students):
    print(f"{name}'s Marks : {students[name]}")
else:
    print(f"Student Not Found")