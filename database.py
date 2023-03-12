import sqlite3
import habit as hb

"""
When running the file database.py it creates the database.
That's why the connect-method, the cursor-method and the 2 table executes are outside of a method.
When running the file, it will create 2 tables:
habits: habits represent the habits.py class itself with all attributes. The NAME_ attribute is the primary key,
because it is very unlikely to have 2 habits with the same name, so i chose the name to be the primary key.

dates: the dates table holds the dates of the tasks when a habit has been completed.
For each date, it holds the date itself,
the calendar week for weekly habits and the name of the habit as a foreign key,
so the date can be assigned to the habit. 
"""
conn = sqlite3.connect("habit.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS habits
                ( 
                NAME_ TEXT PRIMARY KEY NOT NULL,
                PERIODICITY TEXT,
                TASK_SPECIFICATION TEXT,
                CREATED_DATE text,
                MISSED_COUNTER INTEGER,
                LONGEST_STREAK INTEGER,
                CURRENT_STREAK INTEGER)""")

c.execute("""CREATE TABLE IF NOT EXISTS dates
                (id INTEGER PRIMARY KEY,
                _date TEXT NOT NULL,
                calendarweek INTEGER NOT NULL,
                habit_name INTEGER NOT NULL,
                FOREIGN KEY(habit_name) REFERENCES habit(NAME_)
                )""")


def insert_habit_into_db(habit):
    """
    This method takes a given habit and stores it in the database
    :param habit: Habit which was created by the user
    """
    conn.execute("""INSERT INTO habits VALUES (?,?,?,?,?,?,?)""",
                 (habit.name, habit.periodicity, habit.task_specification, habit.created_date,
                  habit.missed_periods_counter, habit.longest_streak, habit.current_streak))
    conn.commit()


def check_off_task(date, calendarweek, habit_name, missed_periods_counter, longest_streak, current_streak):
    """
    This method updates the habit's longest streak, current streak and missed counter.
    After updating the counters of the habit, the method stores a new date into the dates table
    :param date: The date on which the task has been checked.
    :param calendarweek: The calendar week of the date above.
    :param habit_name: The name of the habit, which should be checked off.
    :param missed_periods_counter: Counts how many times someone missed a period
    :param longest_streak: Is the longest streak how often someone checked a task in a row.
    :param current_streak: Is the current counter on how many times someone managed to check a habit in a row.
    """
    conn.execute("""UPDATE habits 
    SET MISSED_COUNTER = ?,
    LONGEST_STREAK = ?, CURRENT_STREAK = ? WHERE NAME_ = ?""",
                 (missed_periods_counter, longest_streak, current_streak, habit_name))

    conn.execute("""INSERT INTO dates VALUES(?, ?, ?, ?)""",
                 (None, date, calendarweek, habit_name))
    conn.commit()


def delete_habit(habit_name):
    """
    This method deletes all dates that belong to a specific habit.
    After deleting the dates, it deletes the habit itself
    :param habit_name: Is the name of the habit that should be deleted.
    """
    conn.execute("DELETE FROM dates WHERE habit_name = ?", (habit_name,))
    conn.execute("DELETE FROM habits WHERE NAME_ = ?", (habit_name,))
    conn.commit()


def load_data():
    """
    This method loads the whole database. First, it loads all habits into a list, then it loads the dates which belong the a habit
    into the habit.completed_periods list.
    :return: habits, a list of all habits with their dates.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits")
    rows = cursor.fetchall()
    cursor.execute("SELECT * FROM dates")
    rows_dates = cursor.fetchall()

    habits = []
    for row in rows:
        habit_ = hb.Habit(*row)
        for date in rows_dates:
            if habit_.periodicity == "daily":
                if date[3] == habit_.name:
                    habit_.completed_periods.append(date[1])
            if habit_.periodicity == "weekly":
                if date[3] == habit_.name:
                    habit_.completed_periods.append(date[2])
        habits.append(habit_)
    return habits

