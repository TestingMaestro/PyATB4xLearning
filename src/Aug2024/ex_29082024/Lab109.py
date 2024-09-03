# Dictionary

my_dict = {
    "name": "Yash",
    "gmailId": "yash@gmail.com",
    "gender": "Male",
    "age": 30
}

# Accessing the elements from dictionary

name = my_dict["name"]
age = my_dict["age"]
print(name, age)

# Accessing the elements via get()

email = my_dict.get("gmailId")
gender = my_dict.get("gender")
print(email)
print(gender)
print(id(gender))

# Dictionary is mutable in nature---> add, update and removes values

# updating or changing existing values [Immutable keys - mutable values]
my_dict["gmailId"] = "sou@parnika.com"
my_dict["name"] = "Souparnika"
my_dict["gender"] = "Female"

print(my_dict)

print(id(gender))

student_info1 = {
    "name": "Yash",
    "gmailId": "yash@gmail.com",
    "gender": "Male",
    "age": 30,
    "address": {
        "home_address": "KA",
        "current_address": "NL"
    }
}

student_info2 = {
    "name": "Sou",
    "gmailId": "sou@gmail.com",
    "gender": "Female",
    "age": 28,
    "address": {
        "home_address": "KA",
        "current_address": "NL"
    }
}

print(student_info1, student_info2)

student_list = [student_info1, student_info2]  # List format
print(student_list)

student_info1.update(name="Bomb")
print(student_info1)
