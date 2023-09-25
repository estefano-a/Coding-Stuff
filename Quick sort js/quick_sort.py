def calculate_student_profile(student):
    score = 0

    for subject in student["subjectsOfInterest"]:
        score += 1

    for course, grade in zip(student["previousCoursesTaken"], student["grades"]):
        if grade == "A":
            score += 2
        elif grade == "B":
            score += 1

    return score
#This function calculates what difficulty is correct for the students.  Unfortunately I ran into issues trying to calculate difficulties, and I struggled to fix them, so this function is not used.

def recommend_courses(student):
    student_profile_score = calculate_student_profile(student)

    recommended_courses = []

    for course in courses:
        common_subjects = set(course["subjectsCovered"]) & set(
            student["subjectsOfInterest"])
        if common_subjects and student_profile_score >= len(common_subjects):
            recommended_courses.append(course)

    return recommended_courses
#This function finds which courses fit for which students.  I noticed that it sometimes recommends courses that students have already previously took, but I struggled to fix that issue.

students = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "subjectsOfInterest": ["Math", "Science"],
        "previousCoursesTaken": ["Algebra 101", "Biology 101"],
        "grades": ["A", "B"],
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "subjectsOfInterest": ["History", "English"],
        "previousCoursesTaken": ["World History 101", "English Literature"],
        "grades": ["B", "A"],
    },
    {
        "id": 3,
        "name": "Carol White",
        "subjectsOfInterest": ["Programming", "Math"],
        "previousCoursesTaken": ["Python 101", "Calculus 101"],
        "grades": ["a", "A"],
    },
    {
        "id": 4,
        "name": "Dave Brown",
        "subjectsOfInterest": ["Science", "Programming"],
        "previousCoursesTaken": ["Chemsitry 101", "Java 101"],
        "grades": ["C", "B"],
    },
    {
        "id": 5,
        "name": "Emily Davis",
        "subjectsOfInterest": ["Math", "Programming"],
        "previousCoursesTaken": ["Algebra 101", "Python 101"],
        "grades": ["A", "A"],
    },
    {
        "id": 6,
        "name": "Frank Green",
        "subjectsOfInterest": ["English", "History"],
        "previousCoursesTaken": ["English Literature", "US History"],
        "grades": ["B", "C"],
    },
    {
        "id": 7,
        "name": "Grace Wilson",
        "subjectsOfInterest": ["History", "Programming"],
        "previousCoursesTaken": ["World History 101", "HTML & CSS"],
        "grades": ["A", "A"],
    },
    {
        "id": 8,
        "name": "Henry Lewis",
        "subjectsOfInterest": ["Science", "Math"],
        "previousCoursesTaken": ["Physics 101", "Calculus 101"],
        "grades": ["C", "B"],
    },
    {
        "id": 9,
        "name": "Irene Clark",
        "subjectsOfInterest": ["Programming", "English"],
        "previousCoursesTaken": ["Java 101", "English Literature"],
        "grades": ["B", "A"],
    },
    {
        "id": 10,
        "name": "Jack Lee",
        "subjectsOfInterest": ["English", "Science"],
        "previousCoursesTaken": ["English Grammar", "Biology 101"],
        "grades": ["C", "B"],
    },

]
#This is a list of all the students and their associated data

courses = [
    {
        "name": "Physics 101",
        "subjectsCovered": ["Science", "Math"],
        "difficulty": "Intermediate",
    },
    {
        "name": "English Grammar",
        "subjectsCovered": ["English"],
        "difficulty": "Intermediate",
    },
    {
        "name": "English Literature",
        "subjectsCovered": ["English"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "Algebra 101",
        "subjectsCovered": ["Math"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "Biology 101",
        "subjectsCovered": ["Science"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "World History 101",
        "subjectsCovered": ["History"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "Python 101",
        "subjectsCovered": ["Programming"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "Chemistry 101",
        "subjectsCovered": ["Math", "Science"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "Calculus 101",
        "subjectsCovered": ["Math"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "Java 101",
        "subjectsCovered": ["Programming"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "HTML & CSS",
        "subjectsCovered": ["Programming"],
        "difficulty": ["Intermediate"],
    },
    {
        "name": "US History",
        "subjectsCovered": ["History"],
        "difficulty": ["Intermediate"],
    },
]
#This is a list of all the courses and their associated data

recommendations = {}

#This loops through each student and finds courses that match their data
for student in students:
    student_recommendations = recommend_courses(student)
    recommendations[student["name"]] = student_recommendations

#This prints each student's recommended courses
for student_name, student_recommendations in recommendations.items():
    print(f"Recommended Courses for {student_name}:")
    if student_recommendations:
        for course in student_recommendations:
            print(f"- {course['name']}")
