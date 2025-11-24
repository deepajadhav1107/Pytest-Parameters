from student import student_details

def test_student_details():
    result = student_details("Rahul", 20)
    assert result == "Rahul is 20 years old."
