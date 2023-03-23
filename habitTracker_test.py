import datetime
import unittest

import database
import habitTracker
from habit import Habit


class HabitTrackerTest(unittest.TestCase):

    def test_get_current_habits(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        self.assertEqual(tracker.get_current_habits(), tracker.habit_list)
        print("test_get_current_habits successfully done")

    def test_get_habit_by_name(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("dishes", "daily", "daily_habit_one")
        habit_ = tracker.get_habit_by_name("dishes")
        self.assertEqual(habit_.name, "dishes")
        print("test_get_habit_by_name successfully done")

    def test_create_habit(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        length = len(tracker.habit_list)
        tracker.create_habit("habit_1", "daily", "daily_habit_one")
        length_after = len(tracker.habit_list)
        self.assertEqual(length, length_after - 1)
        print("test_create_habit successfully done")

    def test_check_off_habit_task(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_2", "daily", "daily_habit_one")
        tracker.check_off_habit_task("habit_2")
        self.assertEqual(tracker.habit_list[0].is_task_completed(), True)
        print("test_check_off_habit_task successfully done")

    def test_delete_habit(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_3", "daily", "daily_habit_one")
        length = len(tracker.habit_list)
        tracker.delete_habit("habit_3")
        self.assertEqual(len(tracker.habit_list), length - 1)
        print("test_delete_habit successfully done")

    def test_get_same_periodicity(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_4", "daily", "daily_habit_one")
        tracker.create_habit("habit_5", "weekly", "daily_habit_one")
        list_ = tracker.get_same_periodicity("weekly")
        self.assertEqual(list_[0].periodicity, "weekly")
        print("test_get_same_periodicity successfully done")

    def test_get_longest_streak_all(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("focus", "daily", "daily_habit_one")
        tracker.create_habit("manage", "weekly", "daily_habit_one")
        tracker.check_off_habit_task("focus")
        self.assertIn("focus", tracker.get_longest_streak_all().keys())
        self.assertIn(str(tracker.get_habit_by_name("focus").longest_streak), tracker.get_longest_streak_all().values())
        print("test_get_longest_streak_all successfully done")

    def test_get_longest_streak_habit(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("think", "daily", "daily_habit_one")
        tracker.check_off_habit_task("think")
        tracker.create_habit("habit_a", "daily", "daily_habit_one")
        self.assertEqual(tracker.get_habit_by_name("think").longest_streak, 1)
        self.assertEqual(tracker.get_habit_by_name("habit_a").longest_streak, 0)
        print("test_get_longest_streak_habit successfully done")

    def test_get_missed_periods_all(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_b", "daily", "daily_habit_one")
        tracker.create_habit("habit_c", "weekly", "daily_habit_one")
        self.assertIn("habit_b", tracker.get_missed_periods_all().keys())
        self.assertIn(str(tracker.get_habit_by_name("habit_b").missed_periods_counter), tracker.get_longest_streak_all().values())
        print("test_get_missed_periods_all successfully done")

    def test_get_missed_periods_habit(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_d", "daily", "daily_habit_one")
        self.assertEqual(tracker.get_habit_by_name("habit_d").missed_periods_counter, 0)
        print("test_get_missed_periods_habit successfully done")

    def test_get_current_open(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_6", "daily", "daily_habit_one")
        tracker.create_habit("habit_7", "weekly", "daily_habit_one")
        tracker.create_habit("habit_8", "weekly", "daily_habit_one")
        tracker.check_off_habit_task("habit_7")
        list_ = tracker.get_current_open()
        self.assertEqual(len(list_), 2)
        print("test_get_current_open successfully done")

    def test_get_current_done(self):
        database.init_db()
        tracker = habitTracker.Tracker()
        tracker.create_habit("habit_9", "daily", "daily_habit_one")
        tracker.create_habit("habit_10", "weekly", "daily_habit_one")
        tracker.create_habit("habit_11", "weekly", "daily_habit_one")
        tracker.check_off_habit_task("habit_10")
        list_ = tracker.get_current_done()
        self.assertEqual(len(list_), 1)
        print("test_get_current_done successfully done")


if __name__ == '__main__':
    # if you run all by once,
    # you will get some errors because of the length of the lists
    unittest.main()
