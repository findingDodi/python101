import matplotlib.pyplot as plt
from StockItem import StockItem


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

        # TODO: Fix double Items in List (look at plot)
        for kaka in stock_item_list:
            if item_name == kaka.get_name():
                kaka.set_amount(kaka.get_amount() + int(item_amount))

        stock_item_list.append(StockItem(item_index, item_amount, item_name))

    return stock_item_list


def get_total_amount(list_of_stock_items):
    max_amount = 0
    item: StockItem
    for item in list_of_stock_items:
        if item.get_amount() > max_amount:
            max_amount = item.get_amount()

    return max_amount


def get_amount_percentage(max_amount, amount):
    return (amount / max_amount) * 100


def show_stock(list_of_stock_items):
    fig, ax = plt.subplots()

    items = []
    amounts = []
    bar_colors = []
    max_amount = get_total_amount(list_of_stock_items)

    item: StockItem
    for item in list_of_stock_items:
        items.append(item.get_name())
        amounts.append(item.get_amount())

        item_percentage = get_amount_percentage(max_amount, item.get_amount())
        if item_percentage <= 10:
            bar_colors.append('tab:red')
        elif item_percentage <= 50:
            bar_colors.append('tab:orange')
        elif item_percentage <= 100:
            bar_colors.append('tab:green')

    ax.bar(items, amounts, color=bar_colors)

    ax.set_ylabel('amount')
    ax.set_title('Stock items by amount')

    plt.show()


if __name__ == "__main__":
    stock_list = get_array_from_file()
    stock_item_list = get_stock_item_list(stock_list)
    show_stock(stock_item_list)
    for stock_item in stock_item_list:
        print(stock_item)
