import datetime
import unittest

import habitTracker
from habit import Habit


class HabitTrackerTest(unittest.TestCase):

    def test_get_current_habits(self):
        tracker = habitTracker.Tracker()
        self.assertEqual(tracker.get_current_habits(), tracker.habit_list)

    def test_create_habit(self):
        tracker = habitTracker.Tracker()
        length = len(tracker.habit_list)
        tracker.create_habit("habit_1", "daily", "daily_habit_one")
        length_after = len(tracker.habit_list)
        self.assertEqual(length, length_after - 1)

    def test_check_off_habit_task(self):
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_2", "daily", "daily_habit_one")
        tracker.check_off_habit_task("habit_2")
        self.assertEqual(tracker.habit_list[0].is_task_completed(), True)

    def test_delete_habit(self):
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_3", "daily", "daily_habit_one")
        length = len(tracker.habit_list)
        tracker.delete_habit("habit_3")
        self.assertEqual(len(tracker.habit_list), length - 1)

    def test_get_same_periodicity(self):
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_4", "daily", "daily_habit_one")
        tracker.create_habit("habit_5", "weekly", "daily_habit_one")
        list_ = tracker.get_same_periodicity("weekly")

        self.assertEqual(list_[0].periodicity, "weekly")

    def test_get_current_open(self):
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_6", "daily", "daily_habit_one")
        tracker.create_habit("habit_7", "weekly", "daily_habit_one")
        tracker.create_habit("habit_8", "weekly", "daily_habit_one")
        tracker.check_off_habit_task("habit_7")
        list_ = tracker.get_current_open()
        self.assertEqual(len(list_), 2)

    def test_get_current_done(self):
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_9", "daily", "daily_habit_one")
        tracker.create_habit("habit_10", "weekly", "daily_habit_one")
        tracker.create_habit("habit_11", "weekly", "daily_habit_one")
        tracker.check_off_habit_task("habit_10")
        list_ = tracker.get_current_done()
        self.assertEqual(len(list_), 1)


if __name__ == '__main__':
    # if you run all by once,
    # you will get some errors because of the length of the lists
    unittest.main()
