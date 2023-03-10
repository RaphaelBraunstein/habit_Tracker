import datetime


class Habit:

    def __init__(self, name, periodicity, task_specification, created_date,missed_periods_counter, current_streak, longest_streak):
        self.name = name
        self.periodicity = periodicity
        self.task_specification = task_specification
        self.created_date = created_date
        self.completed_periods = []
        self.missed_periods_counter = missed_periods_counter
        self.longest_streak = longest_streak
        self.current_streak = current_streak

    def __str__(self):
        return f"Name: {self.name} \nPeriodicity: {self.periodicity} \nCurrent streak: {self.current_streak}"

    def is_task_completed(self):

        if self.periodicity == "daily":

            if datetime.date.today() in self.completed_periods:
                return True
            else:
                return False

        if self.periodicity == "weekly":
            if datetime.date.today().isocalendar()[1] in self.completed_periods:
                return True
            else:
                return False

    def check_off_task(self):

        if self.is_task_completed():
            print(f"You already done {self.name} for this period!")
            return

        if self.periodicity == "daily":

            if len(self.completed_periods) != 0 and datetime.date.today()-datetime.timedelta(1) not in self.completed_periods:
                self.missed_periods_counter += (datetime.date.today()-self.completed_periods[-1]).days
                self.current_streak = 0

            self.completed_periods.append(datetime.date.today())
            self.current_streak += 1

        if self.periodicity == "weekly":

            if len(self.completed_periods) != 0 and datetime.date.today().isocalendar()[1]-1 not in self.completed_periods:
                self.missed_periods_counter += datetime.date.today().isocalendar()[1]-self.completed_periods[-1]
                self.current_streak = 0

            self.completed_periods.append(datetime.date.today().isocalendar()[1])
            self.current_streak += 1

        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
            print(f"Congratulations, you have beaten your old highscore of {self.longest_streak-1}")





