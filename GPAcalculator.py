def calculate_cumulative_gpa(total_subjects):
    total_credits = 0
    total_grade_points = 0
    subject_names = []
    for i in range(total_subjects):
        subject_name = input("Enter the name of subject {}: ".format(i+1))
        subject_names.append(subject_name)
        current_score = float(input("Enter your current score for {}: ".format(subject_name)))
        total_score = 100  
        credit = int(input("Enter the credits for {}: ".format(subject_name)))
        estimated_gpa = estimate_gpa(i+1, current_score, total_score)
        total_credits += credit
        total_grade_points += estimated_gpa * credit
    gpa = total_grade_points / total_credits if total_credits > 0 else 0
    return gpa, get_grade(estimated_gpa), subject_names

def calculate_english_gpa():
    subject_name = "English"
    current_score = float(input("Enter your current score for {}: ".format(subject_name)))
    total_score = 500  
    credit = 3  # Credits for English
    estimated_gpa = estimate_gpa(1, current_score, total_score)
    return estimated_gpa, get_grade(estimated_gpa), subject_name

def get_grade(estimated_gpa):
    if estimated_gpa == 4.0:
        return 'A'
    elif estimated_gpa == 3.7:
        return 'A-'
    elif estimated_gpa == 3.3:
        return 'B+'
    elif estimated_gpa == 3.0:
        return 'B'
    elif estimated_gpa == 2.7:
        return 'B-'
    elif estimated_gpa == 2.3:
        return 'C+'
    elif estimated_gpa == 2.0:
        return 'C'
    elif estimated_gpa == 1.7:
        return 'C-'
    elif estimated_gpa == 1.3:
        return 'D+'
    elif estimated_gpa == 1.0:
        return 'D'
    elif estimated_gpa == 0.0:
        return 'F'
    else:
        return 'W'

def estimate_gpa(subject, current_score, total_score):
    grade_points = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}
    score_percentage = current_score / total_score if total_score > 0 else 0
    if score_percentage >= 0.8:
        return grade_points['A'] * (total_score / 100)
    elif score_percentage >= 0.78:
        return grade_points['A-'] * (total_score / 100)
    elif score_percentage >= 0.73:
        return grade_points['B+'] * (total_score / 100)
    elif score_percentage >= 0.70:
        return grade_points['B'] * (total_score / 100)
    elif score_percentage >= 0.68:
        return grade_points['B-'] * (total_score / 100)
    elif score_percentage >= 0.63:
        return grade_points['C+'] * (total_score / 100)
    elif score_percentage >= 0.6:
        return grade_points['C'] * (total_score / 100)
    elif score_percentage >= 0.58:
        return grade_points['C-'] * (total_score / 100)
    elif score_percentage >= 0.5:
        return grade_points['D'] * (total_score / 100)
    elif score_percentage <= 0.49:
        return grade_points['F'] * (total_score / 100)
    else:
        return grade_points['W']


total_subjects = int(input("Enter the total number of subjects: "))
gpa, grade, subject_names = calculate_cumulative_gpa(total_subjects)
print("Your GPA is: {} ({:.2f})".format(grade, gpa))
print("Your subjects are: {}".format(', '.join(subject_names)))

