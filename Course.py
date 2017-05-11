class InvalidCategoryException(Exception):
    '''Raise the error if the category is not in the Course'''
    pass


class TaskNumberNotExist(Exception):
    '''Raise the error if the task number in a category is out of range'''
    pass


class InvalidMovementError(Exception):
    '''
    Raise the error when either add a existing task or change a non-existing
    task
    '''
    pass


class Course():
    '''A class representing the general information for course'''

    def __init__(self, name):
        '''
        (Course, str, float, float) -> NoneType
        Initiate the Course class by initializing the name of the course and an
        empty gradebook and percentage
        '''

        self._name = name
        self._gradebook = {}
        self._percentage = {}

    def __str__(self):
        '''
        (Course) -> str
        Return a string representation of the course which shows the course
        name and the current grade of the course
        '''

        grade = str(self.get_grade())
        return 'Your current grade for ' + self._name + ' is ' + grade

    def add_category(self, category_name, category_percentage):
        '''
        (Course, str, float) -> NoneType
        Given the name and percentage of a category, add the category name to
        the gradebook and category list and the percentage to the percentage
        list
        REQ: category_percentage <= 1
        '''

        # Create a new dictionary in gradebook
        self._gradebook[category_name] = {}
        # Add the percentage to with the percentage name
        self._percentage[category_name] = category_percentage

    def add_grade(self, category_name, grade, num_task):
        '''
        (Course, str, float, int) -> NoneType
        Given the name of a category, the grade and the number of a task in
        a category, add the grade into the corresponding category
        REQ: category_name in self._gradebook
        REQ: 0 <= grade <= 100
        '''

        # If the category exists
        if category_name in self._gradebook:
            # If the number of task already exist
            if num_task in self._gradebook[category_name]:
                # Raise the invalid movement error
                raise InvalidMovementError()
            # If the number of task does not exist
            else:
                # Add the grade with task number under that category
                self._gradebook[category_name][num_task] = grade
        # If the category does not exist raise an error
        else:
            raise InvalidCategoryException()

    def add_task(self, category_name, num_task):
        '''
        (Course, str, int) -> NoneType
        '''

        if category_name in self._gradebook:
            self.add_grade(category_name, None, num_task)
        else:
            raise InvalidCategoryException()

    def add_next_grade(self, category_name, grade):
        '''
        (Course, str, float) -> NoneType
        Given the name of a category and the grade of a task, add the grade
        into the category in next number of task
        REQ: category_name in self._gradebook
        REQ: 0 <= grade <= 100
        '''

        # Get the current task number in the category
        current_task_num = self.get_num_task(category_name)
        # Add the new task into the category
        self.add_grade(category_name, grade, current_task_num + 1)

    def delete_grade(self, category_name, num_task):
        '''
        (Course, str, int) -> NoneType
        Given the name of a category and the number of task to delete, delete
        the grade of the task in the corresponding number in the category
        REQ: category_name in self._gradebook
        REQ: num_task in self._gradebook[category_name]
        '''

        # If the category exists
        if category_name in self._gradebook:
            # If the task number exists
            if num_task in self._gradebook[category_name]:
                # Pop the task out to delete
                self._gradebook[category_name].pop(num_task)
            # If not exists
            else:
                # Raise the exception
                raise TaskNumberNotExist()
        # Raise an error if the category does not exist
        else:
            raise InvalidCategoryException()

    def change_grade(self, category_name, grade, num_task):
        '''
        (Course, str, float, int) -> NoneType
        Given the name of a category, the grade and the number of a task in
        a category, change the grade of the corresponding number in the
        specific category
        REQ: category_name in self._gradebook
        REQ: 0 <= grade <= 100
        REQ: num_task in self._gradebook[category_name]
        '''

        # If the category exists
        if category_name in self._gradebook:
            # If the task already exists
            if num_task in self._gradebook[category_name]:
                # Directly change the grade
                self._gradebook[category_name][num_task] = grade
            # If the task does not exist
            else:
                # Raise an invalid movement error
                raise TaskNumberNotExist()
        # If the category does not exist, raise an error
        else:
            raise InvalidCategoryException()

    def get_task_grade(self, category_name, task_num):
        '''
        (Course, str, int) -> float or None
        Given the category name and the number of a task of a course, return
        the grade of the task
        REQ: category_name in self._gradebook
        REQ: task_num in self._gradebook[category_name]
        '''

        # If the category exists
        if category_name in self._gradebook:
            # If the number of task exists
            if task_num in self._gradebook[category_name]:
                # Return the grade in the task
                return self._gradebook[category_name][task_num]
            # If the number does not exist
            else:
                # Raise the invalid movement error
                raise TaskNumberNotExist()
        # If the category does not exist
        else:
            # Raise the exception
            raise InvalidCategoryException()

    def get_category_grade(self, category_name):
        '''
        (Course, str) -> float or NoneType
        Given the category name of a course, return a float that is the average
        score of the category, if the category has not task, return -1
        instead
        REQ: category_name in self._gradebook
        '''

        # Initialize the total grade and number of task
        grade_sum = 0
        num_task = 0
        if category_name in self._gradebook:
            # Go through each task of the category
            for each_task in self._gradebook[category_name]:
                # Get the score of the task
                task_score = self.get_task_grade(category_name, each_task)
                # If the grade is not equal to None
                if task_score is not None:
                    # Add the grade into the total
                    grade_sum += self._gradebook[category_name][each_task]
                    num_task += 1
            # If there is no grade so far
            if num_task == 0:
                # Set the result to -1
                result = -1
            # If there is at least some task graded
            else:
                result = grade_sum/num_task
        # If the category does not exist
        else:
            raise InvalidCategoryException()
        return result

    def get_grade(self):
        '''
        (Course) -> float
        Return the total grade of all the category existed in the Course, if
        the category has no task, do not count the category percentage into the
        total percentage
        '''

        # Initiate the total score and total percentage
        total_score = 0
        total_percentage = 0
        # Loop through each category to get the grade
        for each_category in self._gradebook:
            # Get the category percentage and calculate the grade
            category_percentage = self.get_percentage(each_category)
            category_grade = self.get_category_grade(each_category)
            # If the category grade is not valid (not equal to -1)
            if category_grade != -1:
                total_score += category_grade * category_percentage
                total_percentage += category_percentage
        # If the percentage is not zero
        if total_percentage != 0:
            # Round the grade to two decimal space and get the total grade
            result = round(total_score/total_percentage, 2)
        # If the total percentage is zero
        else:
            # Set the result to zero
            result = 0.0
        # Return the result
        return result

    def get_percentage(self, category_name):
        '''
        (Course, str) -> float
        Given a course and a category name in the course, return the percentage
        of the course
        REQ: category_name in self._gradebook
        '''

        if category_name in self._percentage:
            return self._percentage[category_name]
        else:
            raise InvalidCategoryException()

    def get_num_task(self, category_name):
        '''
        (Course, str) -> int
        Given a category from the course, return the number of task the course
        have now
        REQ: category_name in self._gradebook
        '''

        if category_name in self._gradebook:
            return len(self._gradebook[category_name])
        else:
            raise InvalidCategoryException()

    def get_category(self):
        '''
        (Course) -> list of str
        Return a list that includes all the category in the course
        '''

        # Initialize a list for return
        category_list = []
        # Loop through each category in the gradebook
        for each_category in self._gradebook:
            # Add the category in the list
            category_list.append(each_category)
        # Return the list
        return category_list

    def get_total_percentage(self):
        '''
        (Course) -> float
        Return the sum of percentage of all categories in Course 
        '''

        return sum(self._percentage.values())
