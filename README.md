# grade calculator and predictor

Link: https://github.com/JiajunJasonLi/grade-calculator

Thanks for taking a look at my project of grade calculator and predictor.

This is a project called grade calculator and predictor made by Python.

It can help a user to record all the grade in a course and to predict the grade he needs to get in the remaining tasks in oreder to get the grade he expects.


The project includes four parts of python codes:

1. Course.py\
The Course file contains a class for user to create a course.\
For initialization, the user needs to enter the name of the course.\
It includes some methods that help the user to manipulate the course:
1) add_category(category_name, percentage):\
This method asks user to enter the name and percentage of a category to create that category.
2) add_grade(category_name, grade, num_task):\
This method asks user to enter the name of category, the grade and the number of the task to add the grade into the category.
3) add_next_grade(category_name, grade):\
This method asks user to enter the name of a category, the grade of a task to add the grade into that category.\
Please note that it does not need the number of the task because this method will assume the task will be the next.
4) get_category_grade(category_name):\
This method asks user to enter the name of a category so that it can return the average grade of all tasks in that category.\
If a category has no graded task, it will return -1.
5) get_grade():\
This method will return the total grade of the course.\
If a category has no graded task, it will not be included in the calculation.
6) get_num_task(category_name):\
This method asks user to enter the name of a category so that it can return the total number of task in that category.
7) get_category():\
This method will give user a list of category name in the course.

Some methods are omitted because they are mainly used for other code.

2. implement_course.py\
The file is an example of how to use the methods provided in Course.py to implement a course object.\
The example given in the file is from the MATA23.txt in the project.

3. calculation.py\
The file can help user predict how much grade a student need to achieve for the remaining tasks in each category.

In the function predict_course(course, expected_grade), user needs to provide a course object and final grade he expects to get for predicting the grade. However, all ungraded task should be created with a notation None. User can use add_task(category_name, task_num) to add a None grade, task_num-th task in a category to fill in all ungraded tasks.

The algorithm of the code is first of all, it will find out which category is complete and which is not. If a category is complete, we get its percentage and its category grade, calculate mutiplation of the grade and percentage to get what is the grade in the course. If a category is imcomplete, we will put it in a dictionary with the number of ungraded task the category has.

Sum up all complete grade, and based on the expected_grade, we can know how much more the user needs to get from other imcomplete category. Suppose the difference in grade is called grade_diff, and we can know the remaining percentage of all imcomplete category.\
We let grade_diff/remaining_percentage = expected_category_grade, which is the category grade all remaining categories need to achieve. Then we use expected_category_grade times the total number of task in the category to get the total expected grade. Meanwhile we can get current total grade by multipling current_category with current number of graded task in the category.\
As a result, we will know the difference of current total grade and expected total grade, which is the total grade of the sum of all missing tasks. Then divided by the number of missing task we will get the average grade of the missing task in that category that the user needs to get.\
Then, we need to do the check whether expected grade is valid (within the range from 0 to 100). If all the grades are valid, we can directly return the result. If all grades are invalid, we will calculate the change in total grade by setting the expected grade to 0 or 100. If only some of the grades are invalid, we will calculate the change in total grade by setting the grade at invalid category to 0 or 100 and calculate the new estimated grade for those valid category.

4. auto_predicter.py\
The file includes two parts of codes.
1) Auto entering\
The first part provides user a convenient way to enter all information of a Course into the code.\
The user can use either create_course or create_course_helper(file_name) to for auto entering the information.\
In create_course(), user will be asked to input the name of the text file to create the course.\
In create_course_helper(), user can directly enter the name of the text file for creating the course.\
There is a specific formating requirement of the input_file, as follow:\
Each line of the text should be like:\
The first element is the name of the category, the second element is the percentage, and the rest should be the grade of tasks in the category. All elements will be seperated by a single space.\
    quiz 0.2 90 90 95 ...\
    final 0.45\
Please refer to MATA23.txt to see in detail.

2) Auto predicting\
The second part has a function prediction(input_course), which asks the user to input a course object for prediction.\
It basically uses the function in calculation file. However, it will return a string that straightforwardly tells the user what he needs to achieve. Also, inside the function, it asks the user to input the total number of task in each category and the expected grade so that the code can automatically fill all the missing task for the user and predict the grade.

Feel Free to test the code and enjoy it!
