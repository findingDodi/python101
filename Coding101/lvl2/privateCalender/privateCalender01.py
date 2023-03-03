# Liste Tage des aktuellen Monats (eine Woche je Zeile, mit Wochennummer) Wochenanfang ist Montag
import calendar
import datetime


def get_week_number_as_string(year, month, weekdays):
    weekdays_reversed = weekdays.copy()
    weekdays_reversed.sort(reverse=True)
    week_number = datetime.date(year, month, weekdays_reversed[0]).isocalendar().week
    '''
    if week_number < 10:
        return "0{} ".format(str(week_number))

    return "{} ".format(str(week_number))
    '''
    return "{:02d} ".format(week_number)


def print_month(year, month):
    month_weeks = calendar.monthcalendar(year, month)

    for weekdays in month_weeks:
        week_string = get_week_number_as_string(year, month, weekdays)

        for day in weekdays:
            if day == 0:
                week_string += " ** "
            else:
                week_string += " {:02d} ".format(day)

        print(week_string)


def print_header():
    print("CW  {}  {}  {}  {}  {}  {}  {} ".format("Mo", "Tu", "We", "Th", "Fr", "Sa", "So"))


if __name__ == "__main__":
    print_header()
    print_month(2023, 1)
    print("=" * 20)
    print_month(2023, 2)
