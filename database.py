import sqlite3

import habit

conn = sqlite3.connect("habit.db")

c = conn.cursor()

conn.execute("DROP TABLE IF EXISTS habits")
conn.execute("DROP TABLE IF EXISTS dates")

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
    conn.execute("""INSERT INTO habits VALUES (?,?,?,?,?,?,?)""",
                 (habit.name, habit.periodicity, habit.task_specification, habit.created_date,
                  habit.missed_periods_counter, habit.longest_streak, habit.current_streak))
    conn.commit()


def check_off_task(date, calendarweek, habit_name, habit):
    conn.execute("""UPDATE habits 
    SET MISSED_COUNTER = ?,
    LONGEST_STREAK = ?, CURRENT_STREAK = ? WHERE NAME_ = ?""",
                 (habit.missed_periods_counter, habit.longest_streak, habit.current_streak, habit_name))

    conn.execute("""INSERT INTO dates VALUES(?, ?, ?, ?)""",
                 (None, date, calendarweek, habit_name))
    conn.commit()


def delete_habit(habit_name):
    conn.execute("DELETE FROM dates WHERE habit_name = ?", (habit_name,))
    conn.execute("DELETE FROM habits WHERE NAME_ = ?", (habit_name,))
    conn.commit()


def load_data():
    """returns a list of all habits with all dates based on weekly or daily
       habit part done so far, dates missing yet """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits")
    rows = cursor.fetchall()
    cursor.execute("SELECT * FROM dates")
    rows_dates = cursor.fetchall()

    habits = []
    for row in rows:
        habit_ = habit.Habit(*row)
        for date in rows_dates:
            if habit_.periodicity == "daily":
                if date[3] == habit_.name:
                    habit_.completed_periods.append(date[1])
            if habit_.periodicity == "weekly":
                if date[3] == habit_.name:
                    habit_.completed_periods.append(date[2])
        habits.append(habit_)
    return habits

