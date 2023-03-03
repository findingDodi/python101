# Markiere "Heute"
# Mit eingabe eines Monats diesen Monat anzeigen
# Mit eingabe eines Jahres+Monats diesen Monat anzeigen
import calendar
import datetime

CYAN = "\033[36m"
CLEAR = "\033[0m"


def is_today(year, month, day):
    today = datetime.date.today()
    if day == today.day and month == today.month and year == today.year:
        return True

    return False


def get_week_number_as_string(year, month, weekdays):
    weekdays_reversed = weekdays.copy()
    weekdays_reversed.sort(reverse=True)
    week_number = datetime.date(year, month, weekdays_reversed[0]).isocalendar().week

    return "{:02d} ".format(week_number)


def get_day_string(day, mark):
    day_string = ""

    if mark:
        day_string += f"{CYAN}"

    if day == 0:
        day_string += " ** "
    else:
        day_string += " {:02d} ".format(day)

    day_string += f"{CLEAR}"

    return day_string


def print_month(year, month):
    month_weeks = calendar.monthcalendar(year, month)

    for weekdays in month_weeks:
        week_string = get_week_number_as_string(year, month, weekdays)

        for day in weekdays:
            mark = is_today(year, month, day)
            week_string += get_day_string(day, mark)

        print(week_string)


def print_header():
    print("CW  {}  {}  {}  {}  {}  {}  {} ".format("Mo", "Tu", "We", "Th", "Fr", "Sa", "So"))


if __name__ == "__main__":
    print("Welcome to Private Calender!")

    user_year = int(input("Please enter the year you would like to see: "))
    user_month = int(input("Please enter the month you would like to see: "))

    if user_year >= 1970 and 1 <= user_month <= 12:
        print_header()
        print_month(user_year, user_month)
    else:
        print("Sorry the given information is not in our system!")
