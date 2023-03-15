## Habit.py


#### Variables:
name: is the name of the habit which will be tracked. The name attribute is also the Primary Key in the database habit table.<br>
It is logical, because I think that you won't track the same habit two times. And even if you have maybe a habit that you do daily and a similar one that you do weekly, for identification purposes you would still not call them the same in the app. So the name is totally fine as the PK.<br>
<br>periodicity: There are 2 possible hardcoded values for periodicity: "daily" and "weekly". It is stored into a textfield. It could be considered to implement a version with an enumeration to choose from. <br>
Users still cannot type anything into the periodicity, this is handled in the UI part. You can choose between "daily" or "weekly" but you cannot type anything other into the field. <br>
If the input from the user still does not match with the options in the UI, the default value will be set to "daily".
<br><br>
task_specification:<br> The task specification is a little description about the habit. The User can type anything he wants.<br><br>
created_date: The created date stores the date when  the habit was created. The date will be set automatically via the datetime.date.today() function. It will also be stored as a text into the database and will be converted into a date when being processed. <br><br>
completed_periods: Completed_periods is a list that stores the periods that are being put into the list via the check_off_task() method. Depending on the periodicity, either the date (daily) itself or the calendar week (weekly) is being stored it the list.<br>
In the database the completed periods are being stored in a different table called dates with a reference to the habits they belong to. <br> <br>
missed_periods_counter: The missed periods counter represents the number of periods (days/weeks) you missed to check off a task. More on how it increases in the check_off_task() method.<br><br>
longest_streak: The longest streak represents the number on how many times you achieved to check off a task in a row! Gets updated every time you check off a task<br><br>
current_streak: The current streak represents the number on how many times the user achieved to check_off the habit without breaking a period at the current time.<br><br>


#### Methods:

##### is_task_completed()
This method checks, based on the periodicity, if the user checked off the task for the current period. It does that by comparing the current date/calendar week with the last entry of the completed_periods list. The last entry in the list is always the latest one.
<br> If the last period in the list is also the current period, it returns True.<br>
If the last period in the list is not the current one, it returns false.

##### check_off_task()
In this method, the checks off a task. It does that by the following steps:<br>

- First, it checks if the task is already completed via the is_task_completed method. If it returns true, the method returns a little message to the user and then jumps out of the method.
- Secondly, if not, based on the periodicity, the method checks if the last entry is also the last period. 
- Third, if not, the program increases the missed counter by the difference between the two, and sets the current streak to 0.
- Fourth, the program checks if the current streak is bigger than the longest one and updates it if necessary.
- In the fifth step, it appends the period to the list and increases the current counter by one.
- In the last step, the period, and the 3 counting metrics are being sent to the database to update the habit.