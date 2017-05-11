from Course import *


if __name__ == '__main__':
    # This is the manipulative operation of the grade in MATA23.txt file
    MATA23 = Course('MATA23')
    # Create the categories
    MATA23.add_category('quiz', 0.2)
    MATA23.add_category('final', 0.45)
    MATA23.add_category('term_test', 0.35)
    # Add the grade in different categories
    MATA23.add_next_grade('quiz', 90)
    MATA23.add_next_grade('quiz', 90)
    MATA23.add_next_grade('quiz', 95)
    MATA23.add_next_grade('quiz', 100)
    MATA23.add_next_grade('quiz', 100)
    MATA23.add_grade('term_test', 90, 1)
    # If not all the categories have grade, we are still able to get the total
    # grade
    print(MATA23)
    MATA23.add_grade('final', 70, 1)
    print(MATA23)
