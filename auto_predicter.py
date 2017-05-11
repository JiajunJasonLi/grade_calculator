from calculation import *
from Course import *


def create_course():
    '''
    () -> Course
    Use the function to create a course by inputting the file in a specific
    format that recordes your grade for the course
    '''

    # Select the file to import
    file_name = input('tell me the name of the file to import: ')
    # Use the helper function to initialize the course
    course = create_course_helper(file_name)
    # Return the new course
    return course


def create_course_helper(file_name):
    '''
    (str) -> Course
    Given the name of a file that includes all grades in a course, read the
    file and return the course by creating all the category and enter the grade
    REQ: file should be in the specific format
    '''

    # Open the file and create the course
    file = open(file_name, 'r')
    course = Course(file_name[:-4])
    for each_line in file:
        # split the file by the space
        line_element = each_line.split()
        # Get the first element in the file
        category_name = line_element[0]
        # Get the percentage of the category
        category_percentage = float(line_element[1])
        # Add the new category
        course.add_category(category_name, category_percentage)
        # Add the grade into the course
        for index in range(2, len(line_element)):
            course.add_grade(category_name, float(line_element[index]),
                             index - 1)
    # Close the file
    file.close()
    # Return the new course
    return course


def prediction(input_course):
    '''
    (Course) -> str
    Given a course and input of total number of all categories in the course,
    and the expected grade, return a string showing how much grade you need to
    achieve to get your expected grade. If you can achieve the goal, the output
    will give the grade of tasks you need to achieve in all category. If you
    cannot achieve the goal, the output will give you the highest/lowest
    possible grade
    REQ: 0 <= input expected_grade <= 100
    '''

    # Initialize an empty string to return
    return_str = ''
    # Go through the missing task of all the categories
    for each_category in input_course.get_category():
        # Ask user to input the total num of task
        num_task = int(input('How many tasks do you have for ' +
                             each_category + ': '))
        # Get the current number of task in that category
        current_num = input_course.get_num_task(each_category)
        # Add the missing num of task into the course
        for num_index in range(current_num, num_task):
            input_course.add_task(each_category, num_index + 1)
    # Ask for the expected grade
    expected_grade = float(input('What grade do you what to get at last: '))
    # Use the function to get the result
    result = predict_grade(input_course, expected_grade)
    # If the return result is a dict
    if isinstance(result, dict):
        # Get the grade for every predicted category
        for category in result:
            return_str += 'You need to get ' + str(result[category]) +\
                ' for every remaining tasks in ' + category + '\n'
    # If the return result is a float
    elif isinstance(result, float):
        # If the result is higher than the expected grade
        if result > expected_grade:
            # Output the lowest possible grade
            return_str += 'You already achieve your goal\nYour lowest' +\
                ' possible grade is ' + str(result)
        else:
            # Output the highest possible grade of the course
            return_str += 'You cannot get your expected grade\nThe highest' +\
                ' possible grade is ' + str(result)
    # Return the result
    return return_str

if __name__ == '__main__':
    # Create the Course
    # Feel Free to add, change or delete grade in MATA23.txt
    MATA23 = create_course_helper('MATA23.txt')
    # For correct calculation, input:
    # quiz -> 5, term_test -> 1, final -> 1 and any grade from 0 - 100 you want
    # get
    print(prediction(MATA23))
