# grade calculator and predictor

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
To 

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
Please refer to MATA23.txt to see in detail.\

2) Auto predicting\
The second part 
