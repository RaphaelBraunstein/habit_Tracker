import datetime
import database
from habit import Habit


class Tracker:

    def __init__(self):
        """
        This method initializes the habit tracker and loads the data from the database.
        """
        self.habit_list = database.load_data()

    def get_current_habits(self):
        """
        This method returns a list of all currently tracked habits'
        :return: habit_list
        """
        return self.habit_list

    def create_habit(self, name, periodicity, task_specification):
        """
        This method creates a habit and writes it to the database.
        After that, it loads the database into the list again.
        :param name: name of the habit
        :param periodicity: periodicity of the habit
        :param task_specification: specification of the habit
        """
        habit = Habit(name, periodicity, task_specification, datetime.date.today(), 0, 0, 0)
        database.insert_habit_into_db(habit)
        self.__init__()

    def check_off_habit_task(self, habit_name):
        """
        This method completes the task for this period for a specific habit.
        :param habit_name: is the name of the habit
        """
        for habit in self.habit_list:
            if habit_name == habit.name:
                habit.check_off_task()
        self.__init__()

    def delete_habit(self, habit_name):
        """
        This method deletes a habit based on habit_name.
        After deleting, it loads the data from the db again
        :param habit_name:  name of the habit
        """
        for habit in self.habit_list:
            if habit.name == habit_name:
                database.delete_habit(habit_name)
                self.__init__()
                return
        print("This habit is not tracked yet!")

    def get_same_periodicity(self, periodicity):
        """
        This method returns a list of habits based on the periodicity
        :param periodicity: periodicity_ of habits ex. weekly or daily
        :return: returns a list of habits with same periodicity
        """
        result = []
        for h in self.habit_list:
            if h.periodicity == periodicity:
                result.append(h)

        return result

    def get_longest_streak_all(self):
        """
        This method returns an ordered hashmap of habits with its longest streak
        :return: returns an ordered hashmap of habits with its longest streak
        """
        result = {}
        for h in self.habit_list:
            result[h.name] = h.longest_streak
        final = sorted(result, key=lambda habit: habit.longest_streak)

        return final

    def get_longest_streak_habit(self, habit_name):
        """
        This method returns the longest streak of a specific habit
        :param habit_name: is the name of the habit
        :return: longest_streak of given habit
        """
        for habit in self.habit_list:
            if habit.name == habit_name:
                return habit.longest_streak

    def get_missed_periods_all(self):
        """
         This method returns an ordered hashmap of habits with its missed streak counter
        :return: returns an ordered hashmap of habits with its missed streak counter
        """
        result = {}
        for h in self.habit_list:
            result[h.name] = h.missed_periods_counter

        final = sorted(result, key=lambda habit: habit.missed_periods_counter)

        return final

    def get_missed_periods_habit(self, habit_name):
        """
        This method returns the missed streak counter of a specific habit
        :param habit_name: is the name of the habit
        :return: missed_streak_counter of given habit
        """
        for habit in self.habit_list:
            if habit.name == habit_name:
                return habit.missed_periods_counter

    def get_current_open(self):
        """
        This method returns a list of all habits that haven't been done for the current period
        :return: list of habits
        """
        result = []
        for habit in self.habit_list:

            if not habit.is_task_completed():
                result.append(habit)

        return result

    def get_current_done(self):
        """
        This method returns a list of all habits that have already been done for the current period
        :return: list of habits
        """
        result = []
        for habit in self.habit_list:

            if habit.is_task_completed():
                result.append(habit)

        return result

    def print_statistic_all(self):
        """
        This method prints the current statistic for all habits.
        """

        for habit in self.habit_list:
            percentage = (len(habit.completed_periods)/(len(habit.completed_periods) + habit.missed_periods_counter))*100
            print("You achieved to do ", percentage, " % of all tasks for", habit.name)

    def print_statistic_one(self, habit_name):
        """
        This method prints the data for a specific habit
        :param habit_name: name of the habit
        """

        for habit in self.habit_list:
            if habit.name == habit_name:
                percentage = (len(habit.completed_periods) /
                              (len(habit.completed_periods) + habit.missed_periods_counter)) * 100

                print("You achieved to do ", percentage, " % of all tasks for", habit.name)
                print("periodicity:", habit.periodicity)
                print("Current streak:", habit.current_streak)
                print("Longest streak:", habit.longest_streak)
                print("missed periods:", habit.missed_periods_counter)
                print("done periods:")
                for date in habit.completed_periods:
                    print(date)
                print("------------------------")
                print(habit.is_task_completed())
                if habit.is_task_completed():
                    print("The task has already been done for this period")
                else:
                    print("The task hasn't been done for the current period!")




