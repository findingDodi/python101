from Printy import Printy


def get_printy_listy(listy):
    printy_listy = []
    for item in listy:
        the_item = Printy(item)
        printy_listy.append(the_item)

    return printy_listy


the_list = ["Faultier", "Hamster", "Zebra"]
object_list = get_printy_listy(the_list)

for item in object_list:
    item.do_print()

object_list.reverse()

for item in object_list:
    item.do_print()
