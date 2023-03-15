## Database.py

#### init_db()

The init_db() method is responsible for creating the database. For inserting the testdata without errors, the table will be dropped at the beginning.
This can be "solved" by cutting out the "DROP" statements and initializing the db seperately from the rest of the program like a setup file, that runs just once.
The method creates 2 tables, one called habit, one called dates. The habit table represents the habit itself, 
while the dates table represent the list of dates when a specific habit has been checked off.


#### insert_habit_into_db()
The insert_habit_into_db() method inserts a given habit into the habit db database.

#### check_off_task()
The check_off_task() method inserts the date when the habit has been checked off into the dates table
and updates the missed counter, the current streak and the longest streak of the corresponding habit.

#### delete_habit()
THe delete_habit() method deletes all dates that belong to a specific habit from the dates table.
After that it deletes the table itself.

#### load_data()
The load_data() method reads both of the tables into 2 list variables.
After that, the lists are being looped through and Habit objects are being created out of the rows.
After creating a specific habit, the second list of dates is being looped through and (depending on the periodicity)
the dates or the calendar weeks are being inserted into the habit.completed_periods list.

Be aware that the dates are actually strings when they are inserted into the complete_periods list and need to converted into dates
when processing or comparing them. 

#### insert_test_data()

The insert_test_data() method inserts testdata into the database. 

For the test data, I chose to create 2 daily habits called drinking and exercise,
and 3 weekly habits called cleaning, trash, and laundry.

Keep in mind that the program operates with realtime data .
The last entry of the testdata ex. "exercise" dates back to 2023-03-05.
So no matter what the current counter is, if you check off a task, the missed counter will
increase by the days between today and the 5th of march and the current counter will drop to 1.