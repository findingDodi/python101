import matplotlib.pyplot as plt
from StockItem import StockItem
from operator import add


def get_array_from_file(file="instockbroken.csv"):
    file_handle = open(file, "r")
    file_content = file_handle.readlines()
    file_handle.close()
    file_content.pop(0)

    return file_content


def get_stock_item_list(string_array):
    stock_item_list = []

    for item in string_array:
        stock_item = item.strip().split(";")

        item_index = stock_item[0]
        item_amount = stock_item[1]
        item_name = stock_item[2]

        if item_index == "":
            item_index = 0
        if item_amount == "":
            item_amount = 0
        if item_name == "":
            item_name = "no name"

        stock_item_list.append(StockItem(item_index, item_amount, item_name))

    return stock_item_list


def get_bottom_list(list1, list2):
    return list(map(add, list1, list2))


def show_stock(list_of_stock_items):
    fig, ax = plt.subplots()

    names = []

    '''
    labels:     Hamster, Sloth, Rabbit
    amounts[0]:       7,     4,      8
    amounts[1]:       0,     0,      2      
    '''

    name_occurrences = {}
    name_row_position = {}

    item: StockItem
    for item in list_of_stock_items:
        if item.get_name() not in name_occurrences:
            name_occurrences[item.get_name()] = 0
            name_row_position[item.get_name()] = 0

        name_occurrences[item.get_name()] += 1

    amounts = [[0] * len(name_occurrences) for i in range(max(name_occurrences.values()))]

    item: StockItem
    for item in list_of_stock_items:
        if item.get_name() not in names:
            names.append(item.get_name())

        row_index = name_row_position[item.get_name()]
        name_row_position[item.get_name()] += 1
        name_index = list(name_row_position).index(item.get_name())
        amounts[row_index][name_index] = item.get_amount()

    stack_sums = [0] * len(names)

    for amount in amounts:
        ax.bar(names, amount, bottom=stack_sums)
        stack_sums = get_bottom_list(stack_sums, amount)

    ax.set_ylabel('amount')
    ax.set_title('Stock items by amount')

    plt.show()


if __name__ == "__main__":
    stock_list = get_array_from_file()
    stock_item_list = get_stock_item_list(stock_list)
    show_stock(stock_item_list)
    for stock_item in stock_item_list:
        print(stock_item)
