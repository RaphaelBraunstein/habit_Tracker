import datetime

import database


class Habit:

    def __init__(self, name, periodicity, task_specification, created_date, missed_periods_counter, longest_streak,
                 current_streak):
        """
        This initializes the habit
        :param name: is the name of the habit
        :param periodicity: is the periodicity: ex. daily or weekly
        :param task_specification: is the specification of the task
        :param created_date: the date when the habit was created
        :param missed_periods_counter: is the counter how many times someone failed to complete a task
        :param current_streak: is the current streak counter on how many times
         someone managed to complete a task in a row
        :param longest_streak: is the longest streak of a habit
        """
        self.name = name
        self.periodicity = periodicity
        self.task_specification = task_specification
        self.created_date = created_date
        self.completed_periods = []
        self.missed_periods_counter = missed_periods_counter
        self.longest_streak = longest_streak
        self.current_streak = current_streak

    def __str__(self):
        """
        This method returns the basic information of a habit.
        :return: name, periodicity, current streak and the longest streak
        """
        return f"Name: {self.name} \nPeriodicity: {self.periodicity} \nCurrent streak: {self.current_streak} \nLongest streak: {self.longest_streak} \nmissed tasks: {self.missed_periods_counter}"

    def is_task_completed(self):
        """
        This method checks if a habit has been done in the current period.
        Checks separately for daily and weekly habits.
        For daily habits it checks of the current date is already in the completed periods list.
        For weekly habits it checks if the current calendar week is in the completed periods list.

        :return: it returns TRUE/FALSE TRUE= already completed, FALSE= not completed yet
        """

        if self.periodicity == "daily":

            # dates from database need to be converted, because in database they are strings, and here they are dates
            dates = []
            for x in self.completed_periods:
                dates.append(datetime.datetime.strptime(x, '%Y-%m-%d').date())  # convert text into dates for comparison

            if datetime.date.today() in dates:
                return True
            else:
                return False

        if self.periodicity == "weekly":
            if datetime.date.today().isocalendar()[1] in self.completed_periods:
                return True
            else:
                return False

    def check_off_task(self):
        """
        It checks if the current period is already completed.
        If the current period is not in the list,
        it checks if the last period is in the list.
        If it is not, it calculates the difference between the last entry and the current entry
        and adds it to the missed counter, and deletes the current counter.
        If the last period is in the list, it only adds the current one.
        At the end, it writes the changes to the db
        """

        if self.is_task_completed():
            print(f"You already done {self.name} for this period!")
            return

        if self.periodicity == "daily":
            # here it checks if the yesterday's date is in the list
            if len(self.completed_periods) != 0 and datetime.date.today() - datetime.timedelta(
                    1) not in self.completed_periods:
                self.missed_periods_counter += (
                        datetime.date.today() - datetime.datetime.strptime(self.completed_periods[-1],
                                                                           '%Y-%m-%d').date()).days
                self.current_streak = 0

            self.completed_periods.append(datetime.date.today())
            self.current_streak += 1
            print("Congratulations, you have successfully done this task")
            if self.current_streak > self.longest_streak:
                self.longest_streak = self.current_streak
                print(f"Congratulations, you have beaten your old high-score of {self.longest_streak - 1}")

        if self.periodicity == "weekly":

            # here it checks if the last weeks number is in the list
            if len(self.completed_periods) != 0 and datetime.date.today().isocalendar()[1] - 1 not in self.completed_periods:
                self.missed_periods_counter += datetime.date.today().isocalendar()[1] - self.completed_periods[-1] - 1
                self.current_streak = 0

            self.completed_periods.append(datetime.date.today().isocalendar()[1])
            self.current_streak += 1
            print("Congratulations, you have successfully done this task")  #
            if self.current_streak > self.longest_streak:
                self.longest_streak = self.current_streak
                print(f"Congratulations, you have beaten your old high-score of {self.longest_streak - 1}")

        database.check_off_task(datetime.date.today(), datetime.date.today().isocalendar()[1], self.name,
                                self.missed_periods_counter, self.longest_streak, self.current_streak)
