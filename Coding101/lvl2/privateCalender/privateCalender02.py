# Markiere "Heute"
# Mit eingabe eines Monats diesen Monat anzeigen
# Mit eingabe eines Jahres+Monats diesen Monat anzeigen
import calendar
import datetime

CYAN = "\033[36m"
CLEAR = "\033[0m"


def get_week_number_as_string(year, month, week):
    week_reversed = week.copy()
    week_reversed.sort(reverse=True)
    week_number = datetime.date(year, month, week_reversed[0]).isocalendar().week
    if week_number < 10:
        return "0{} ".format(week_number)

    return "{} ".format(str(week_number))


def get_day_string(month, day):
    today = datetime.date.today()
    day_string = ""

    if day == int(today.strftime("%d")) and month == int(today.strftime("%m")):
        day_string += f"{CYAN}"

    if day == 0:
        day_string += " ** "
    elif day < 10:
        day_string += " 0{} ".format(str(day))
    else:
        day_string += " {} ".format(str(day))

    day_string += f"{CLEAR}"

    return day_string


def print_month(year, month):
    my_month = calendar.monthcalendar(year, month)

    for week in my_month:
        week_string = get_week_number_as_string(year, month, week)

        for day in week:
            week_string += get_day_string(month, day)

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
