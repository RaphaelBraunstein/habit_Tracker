## HabitTracker.py


#### Variables:

habit_list: The habit list, represents the database with all habits and their completed periods.
#### Methods:

##### get_current_habits()
The get_current_habits() method returns the current state of the habit_list. It returns a list with all habits and their competed periods. 

##### get_habit_by_name(habit_name)
The get_habit_by_name() method iterates through the habit list and returns the habit that has the same name as habit_name.

##### create_habit(name, periodicity, task_specification)
The create-habit() method creates a habit with the given attributes. All other attributes are set automatically by the program. <br> 
After creating the habit, the database stores the habit in the database and loads the current state of the db into the habit list.

##### check_off_habit_task(habit_name)
Based on the name, the method searches through the habit list and checks off the habit that has the same name as habit_name.
After checking  off the habit, it loads the data again from the database. 

##### delete_habit()
Based on the name, the method searches for the object with the same name in the db. After finding it, the object gets deleted from the database.<br>
Finally, the data from the db will be loaded again. 

##### get_same_periodicity(periodicity)
Based on the periodicity, the method searches for every habit with that specific periodicity and writes it into a new list.

##### get_longest_streak_all()
This method returns a hashmap of all habits with the name as the key and the longest streak as the value.

##### get_longest_streak_habit(habit_name)
Based on the habit name, the method returns the longest streak of the habit. 

##### get_missed_periods_all()
This method returns a hashmap of all habits, with the name as the key and the missed_periods_counter as the value.

##### get_missed_periods_habit(habit_name)
Based on the habit_name, the method return the missed_period_counter of the habit. 

##### get_current_open()
This method iterates through the habit_list and writes every object, where the result of the is_completed() is False, into a new list and returns it.

##### get_current_done()
This method iterates through the habit_list and writes every object, where the result of the is_completed() is True, into a new list and returns it.

##### print_statistic_all()
The print statistic method prints the percentage on how many times you achieved to do a task in the corresponding period. 

##### print_statistic_one(habit_name)
Based on the habit_name, this method gives you a detailed statistic on the habit.