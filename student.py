import sys

def student_details(name, age):
    return f"{name} is {age} years old."

if __name__ == "__main__":
    name = sys.argv[1]
    age = sys.argv[2]

    print(student_details(name, age))
