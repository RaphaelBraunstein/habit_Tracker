"""
habit_list: is a list of all habits, which will be processed in the following methods

CRUD applications for Habit management.
get_current_habits: returns a list of all currently tracked habits
get_same_periodicity(periodicity): returns a list of all habits with the same periodicity.
get_longest_streak_all(): returns a hashmap with  the longest run streak as the value and the name of the habit as the key
get_longest_streak(habit_id): returns the longest run streak for a given habit.
get_missed_periods(habit_id): returns a list with all missed periods of a habbit
get_statistic(): returns list of lists which contain the name, the current streak and the longest streak of all defined habits.
Get_current_open(): returns a list of habbits in the current period that haven’t been done yet
Get_current_done(): returns a list of habbits that already have been done in the current period
"""