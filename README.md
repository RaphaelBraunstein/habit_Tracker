# Habit Tracker

### Installation
To install the Habit tracker, you need to create a local git repository
with the remote address of this repository. <br>
To do so:<br>
- go to your local folder
- initialize a new git repo via the *git init* command
- now add the remote url of this project: *git remote add origin https://github.com/RaphaelBraunstein/habit_Tracker.git*
- now you can pull the project via *git pull origin main*
- After that, you go to your folder in the cmd and type *start main.py*
- The database will be initialized in the background while starting the app. So no further steps are needed to run the app! 
- Now you run the habit tracking app! 

##### Be aware that this project was built for educational purposes. In order to fill the db with the testdata, the db will be dropped at the beginning of each session! <br> 
##### The testdata is dated with the 5th march! Due to the fact that the habit tracker processes real time data, and the testdata is "outdated", when "checking off" a task for a habit from the testdata, the misscounter will always increase by the missed dates between today and the last entry,  and the current counter will drop to 1!

### How to run tests?
To run the tests, you open the project in your IDE. 
In your Project File System, you should see the "Documentation" folder, the "venv" folder and a bunch of classes. 
Under the habitTracker.py file, you see the habitTracker_*test*.py file. When you open the file you can either run each test case by clicking the start button next to the function.
Or you can run all at once by clicking the start button next to the definition of the class!

### Predefined Testdata 
The required pre-defined testdata of 4 weeks for 5 habit is hardcoded in the database.py file in the insert_test_data() method, which will be executed in the main.py file. 

### Description
This description section will hold some basic information on how to use the app:<br>

- When starting the app, you will get a little introduction on how to use the habit tracker!
- When you need help, or you want to see the menu, you can type *help*.
- - -
#### How to create a habit?
The command for creating a habit is stored in [3], so type 3.<br>
After that you are asked to type in the name,the periodicity,and a little description for it. <br> 
After submitting you get a little info text of your habit.

#### How to check off a task for a habit? <br>
To check off the habit you just created, type 4 into the cli. <br>
Now type in the name of the habit, you want to check  off for the current period. <br>
After successfully doing the task, you get a "congratulations" message. <br>
If you have already done the task for the current period, the tracker will tell you that you have already done it.

#### How to delete a habit? <br>
To delete a habit, type *5* into the cli. <br>
Next, you are asked to type in the name of the habit. <br>
After that you get a list of the remaining habits.


#### How to get a list of all currently tracked habits?<br>
To get a list of the currently tracked habits, type *1*. <br>
To get the statistic of all currently tracked habits, type *13*


----

These are just some basic functions, you can do with the habit tracker. To see all available commands, just type *help* into the cli

----
<br>

### Contributions

If you have any additional ideas for this project, feel free to contact me :)




