import pandas as pd

data = {
    "Student_ID": list(range(1, 31)),
    "Name": [
        "Rahul", "Priya", "Arjun", "Sneha", "Kiran",
        "Anjali", "Rohan", "Divya", "Vikram", "Kavya",
        "Aditya", "Neha", "Suresh", "Pooja", "Naveen",
        "Swathi", "Ajay", "Bhavya", "Manoj", "Keerthi",
        "Sanjay", "Deepika", "Harsha", "Lakshmi", "Ravi",
        "Srilatha", "Teja", "Nandini", "Mahesh", "Sirisha"
    ],
    "Age": [
        20, 21, 19, 20, 22, 21, 20, 19, 22, 20,
        21, 19, 23, 20, 22, 21, 20, 19, 23, 21,
        22, 20, 19, 21, 22, 20, 23, 19, 21, 20
    ],
    "Course": [
        "Python", "Java", "Python", "Java", "C++",
        "Python", "C++", "Java", "Python", "C++",
        "Java", "Python", "C++", "Java", "Python",
        "C++", "Java", "Python", "C++", "Java",
        "Python", "C++", "Java", "Python", "C++",
        "Java", "Python", "C++", "Java", "Python"
    ],
    "Marks": [
        85, 78, 92, 88, 67, 95, 73, 81, 76, 89,
        84, 91, 65, 79, 87, 82, 74, 96, 69, 86,
        77, 90, 83, 94, 71, 80, 88, 75, 82, 93
    ]
}

df = pd.DataFrame(data)

print(df)