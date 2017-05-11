from Course import *


def get_missing_num(course, category):
    '''
    (Course, str) -> int
    Given a Course and one of the category name from the course, return the
    number of task that need is missing equal to None
    REQ: category in course.get_category()
    '''

    # Initialize the number to return
    missing_task = 0
    # Loop through each task in the category
    for task_num in range(1, course.get_num_task(category) + 1):
        # If the task is None
        if course.get_task_grade(category, task_num) is None:
            # Add the number by 1
            missing_task += 1
    # Return the number of missing task
    return missing_task


def predict_grade(course, expected_grade):
    '''
    (Course, float) -> dict of {str: float} or float
    Given a course and the expected grade of the course, return a dictionary
    that indicates the estimated grade of each tasks in each category that has
    imcomplete tasks. If it cannot meet the expected grade, return the highest
    or lowest grade the person can have in the course
    REQ: 0 <= expected_grade <= 100
    '''

    # Test whether the course has total percentage of 1
    '''Missing Code'''
    # Initialize the float for a complete grade
    complete_grade = 0.0
    complete_percentage = 0
    # Create a dictionary to get grade to calculate
    imcomplete_category = {}
    for each_category in course.get_category():
        num_missing_task = get_missing_num(course, each_category)
        # If the category has no missing task
        if num_missing_task == 0:
            # Get the percentage of the category
            category_percentage = course.get_percentage(each_category)
            # Add the grade to complete grade
            complete_grade += course.get_category_grade(each_category) *\
                category_percentage
            # Add the percentage to the complete percentage
            complete_percentage += category_percentage
        # If the category has some missing tasks
        else:
            imcomplete_category[each_category] = num_missing_task
    # Test whether the complete category is 1
    ''' Missing Code'''
    # Calculate the how much more grade need to be achieved
    grade_gap = expected_grade - complete_grade
    # Use the helper
    get_result = predict_grade_helper(course, imcomplete_category, grade_gap,
                                      1 - complete_percentage)
    # If the helper's result is a float
    if isinstance(get_result, float):
        # Add the complete grade into the result
        result = complete_grade + get_result
    # If the helper's result is a dict
    elif isinstance(get_result, dict):
        # Set the get result as the result to return
        result = get_result
    # Return the result
    return result


def predict_grade_helper(input_course, imcomplete_category, grade_diff,
                         remaining_percentage):
    '''
    (Course, dict of {str: int}, float, float) -> dict of {str: float} or float
    Given a input course, a dictionary that have the name of imcomplete
    category with its number of missing task, the sum of percentage of all
    imcomplete categories and the difference in grade, return a dictionary
    that indicates the estimated grade of each tasks in each category that has
    imcomplete tasks. If the grade difference cannot be filled, return a float
    that reflect change in grade by calculated by maximizing or minimizing
    the grade of tasks
    REQ: remaining_percentage < 1.0
    '''

    # Initialize a dictionary to get the category grade
    expected_result = {}
    # Get the average expected grade each category need to achieve
    expected_category_grade = grade_diff / remaining_percentage
    # Initialize a dict to check the potential invalid estimated grade
    invalid_list = {}
    # Calculate the total percentage grade each category need to have
    for each_category in imcomplete_category:
        # Get the total number of task in the category
        total_task = input_course.get_num_task(each_category)
        # Get the current grade of the category
        current_grade = input_course.get_category_grade(each_category)
        # Get the number of missing task in the category
        num_missing_task = imcomplete_category[each_category]
        # Get the total expected grade by time the expected grade with the
        # total number of task in that category
        total_expected_grade = expected_category_grade * total_task
        # Get the number of current grade of existing task
        current_grade = (total_task - num_missing_task) * current_grade
        # Calculate the estimated category grade by first getting the
        # difference in total grade and dividing it by the number of missing
        # task
        estimated_grade = (total_expected_grade - current_grade) /\
            num_missing_task
        # If the estimated grade is higher than 100
        if estimated_grade > 100:
            # Calculate the complete grade by letting all imcomplete tasks to
            # be 100
            possible_grade = 100 * num_missing_task + current_grade
            # Put the possible grade times its percentage to the invalid list
            invalid_list[each_category] = possible_grade *\
                input_course.get_percentage(each_category)/ total_task
            # Put the estimated grade as 100 into the result
            expected_result[each_category] = 100
        # If the estimated grade is less than 0
        elif estimated_grade < 0:
            # Calculate the complete grade by letting all imcomplete tasks to
            # be 0
            possible_grade = 0 * num_missing_task + current_grade
            # Put the possible grade times its percentage to the invalid list
            invalid_list[each_category] = possible_grade *\
                input_course.get_percentage(each_category)/ total_task
            # Put the estimated grade as 0 into the result
            expected_result[each_category] = 0
        # If the grade is within right range
        else:
            # Put the estimated grade into the dictionary
            expected_result[each_category] = round(estimated_grade, 2)
    # Check if there is any invalid grade
    # If there is no invlid grade
    if len(invalid_list) == 0:
        # Set the expected result as the result to return
        result = expected_result
    # If all categories are invalid
    elif len(invalid_list) == len(expected_result):
        # Get the sum together
        result = sum(invalid_list.values())
    # If only some of the categories are invalid
    else:
        # Initilize used percentage and total grade
        used_percentage = 0.0
        new_complete_grade = 0.0
        for each_category in invalid_list:
            # Sum up the percentage and grade
            used_percentage += input_course.get_percentage(each_category)
            new_complete_grade += invalid_list[each_category]
            # Pop the category from imcomplete category
            imcomplete_category.pop(each_category)
        # Use the recursion to get the new estimated grade for valid category
        updated_result = predict_grade_helper(input_course, 
                                              imcomplete_category,
                                              grade_diff - new_complete_grade,
                                              remaining_percentage -
                                              used_percentage)
        # If the updated result is a dict
        if isinstance(updated_result, dict):
            # Update the category to the result
            expected_result.update(updated_result)
            result = expected_result
        # If the updated result is a float
        elif isinstance(updated_result, float):
            # Sum up all the estimated sum together that reflect the change in
            # total grade
            result = sum(invalid_list.values() + updated_result)
    # Return the result
    return result

if __name__ == '__main__':
    sample = Course('sample')
    sample.add_category('1', 0.7)
    sample.add_category('2', 0.3)
    sample.add_next_grade('1', 80)
    sample.add_next_grade('2', 80)
    sample.add_task('2', 2)
    a = predict_grade(sample, 40)
    print(a)