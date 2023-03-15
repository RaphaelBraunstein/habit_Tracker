import database
import habitTracker

database.init_db()

# initializing the db, so that the testdata can be loaded into the db without errors.
# In a "normal" environment, the db would not be dropped and loaded again when opening the program!

database.insert_test_data()
tracker = habitTracker.Tracker()

print("----WELCOME TO THE HABIT TRACKER!----")
print("")
print("Your currently tracked habits are:")
for habit in tracker.get_current_habits():
    print(habit.name)
print("")
print("Here you have a little list on what you can do:")
print("[1]: get a list of all currently tracked habit")
print("[2]: get the data of a specific habit")
print("[3]: create a habit you want to track")
print("[4]: check off the habit for the current period")
print("[5]: delete a habit")
print("[6]: get a list of habits with the same periodicity")
print("[7]: get the longest streak of all tracked habits")
print("[8]: get the longest streak of a specific habit")
print("[9]: get the counter of the missed periods of all habits")
print("[10]: get the counter of the missed periods of a specific habit")
print("[11]: get all habits that haven't been done for the current period")
print("[12]: get all habits that have been done for the current period")
print("[13]: get the statistics of all habits")
print("[14]: get the statistics of a specific habit")
print()
print("When you want to see this list again, type \"help\" ")
print()
print("When you want to exit the program, type \"exit\" ")

while True:
    command = input()

    match command:

        case "1":
            print("here is a list of all currently tracked habits:")
            for habit in tracker.get_current_habits():
                print(habit.__str__())

        case "2":
            name = input("What is the name of the habit you want to get the details from?")
            print(tracker.get_habit_by_name(name))

        case "3":
            name = input("What is the name of the habit you want to create?")
            print("What is the periodicity of the habit? \n[1] daily \n[2] weekly")
            x = input()
            if x == "1":
                periodicity = "daily"
            elif x == "2":
                periodicity = "weekly"
            else:
                print(f"I am sorry, you can only choose between [1] or [2] ...as a default {name} is going to be a daily habit")
                periodicity = "daily"
            task_specification = input("Please write a little description for the task")

            tracker.create_habit(name, periodicity, task_specification)
            print(tracker.habit_list[-1])

        case "4":
            name = input("What is the name of the habit you want to do?")
            tracker.check_off_habit_task(name)

        case "5":
            name = input("Which habit do you want to delete?")
            tracker.delete_habit(name)
            print("here you can see the remaining habits:")
            for habit in tracker.get_current_habits():
                print(habit.name)

        case "6":
            print("Which periodicity do you want to see? \n [1] daily \n [2] weekly")
            x=input()
            if x == "1":
                periodicity = "daily"
            elif x == "2":
                periodicity = "weekly"
            else:
                print("Sorry we do not have this periodicity in our database")
                break

            for habit in tracker.get_same_periodicity(periodicity):
                print(habit)

        case "7":
            print("here is the longest streak for every tracked habit")
            set_ = tracker.get_longest_streak_all()
            for key in set_:
                print(key, set_[key])

        case "8":
            name = input("What is the name of the habit you want to get the longest streak?")
            print(f"The longest streak of {name} is",tracker.get_longest_streak_habit(name))

        case "9":
            print("here is the missed counter for every tracked habit")
            set_ = tracker.get_missed_periods_all()
            for key in set_:
                print(key, set_[key])

        case "10":
            name = input("What is the name of the habit you want to get the missed period counter from?")
            print(f"The counter of missed periods of {name} is", tracker.get_missed_periods_habit(name))

        case "11":
            print("These are the habits that haven't been done for this period so far")
            for habit in tracker.get_current_open():
                print(habit.name)
            print()
            print("If you want to check off a task, type [4]")

        case "12":
            print("These are the habits that have already been done for this period")
            for habit in tracker.get_current_done():
                print(habit.name)

        case "13":
            print("Here are some statistics for all habits:")
            print()
            tracker.print_statistic_all()

        case "14":
            name = input("What is the name of the habit you want to see the statistics from?")
            print()
            print(f"Here are some statistics for {name}: ")
            tracker.print_statistic_one(name)


        case "help":

            print("Here you have a little list on what you can do:")
            print("[1]: get a list of all currently tracked habit")
            print("[2]: get the data of a specific habit")
            print("[3]: create a habit you want to track")
            print("[4]: check off the habit for the current period")
            print("[5]: delete a habit")
            print("[6]: get a list of habits with the same periodicity")
            print("[7]: get the longest streak of all tracked habits")
            print("[8]: get the longest streak of a specific habit")
            print("[9]: get the counter of the missed periods of all habits")
            print("[10]: get the counter of the missed periods of a specific habit")
            print("[11]: get all habits that haven't been done for the current period")
            print("[12]: get all habits that have been done for the current period")
            print("[13]: get the statistics of all habits")
            print("[14]: get the statistics of a specific habit")
            print()
            print("When you want to see this list again, type \"help\" ")
            print()
            print("When you want to exit the program, type \"exit\" ")

        case "exit":
            exit()
