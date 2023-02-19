# Liste Tage des aktuellen Monats (eine Woche je Zeile, mit Wochennummer) Wochenanfang ist Montag
import calendar
import datetime


def get_week_number(year, month, week):
    week_reversed = week.copy()
    week_reversed.sort(reverse=True)
    week_number = datetime.date(year, month, week_reversed[0]).isocalendar().week
    if week_number < 10:
        return "0{} ".format(week_number)

    return "{} ".format(str(week_number))


def print_month(year, month):
    my_month = calendar.monthcalendar(year, month)

    for week in my_month:
        week_string = get_week_number(year, month, week)
        for day in week:
            if day == 0:
                week_string += " ** "
            elif day < 10:
                week_string += " 0{} ".format(str(day))
            else:
                week_string += " {} ".format(str(day))
        print(week_string)


def print_header():
    print("CW  {}  {}  {}  {}  {}  {}  {} ".format("Mo", "Tu", "We", "Th", "Fr", "Sa", "So"))


if __name__ == "__main__":
    print_header()
    print_month(2023, 1)
    print_month(2023, 2)
