import matplotlib.pyplot as plt
from operator import add

# 1 bis n lists
# bottom
# liste 1 soll immer bottom sein
# liste n soll immer top sein
# bottom der aktuellen liste ist immer die summe aller bisherigen listen


def get_bottom_list(list1, list2):
    return list(map(add, list1, list2))


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 20, 27]
women_means = [0, 0, 0, 35, 0]
other_means = [5, 5, 5, 5, 5]
another_means = [5, 5, 5, 5, 5]
all_lists = [men_means, women_means, other_means, another_means]

fig, ax = plt.subplots()
stack_sums = [0, 0, 0, 0, 0]

for means in all_lists:
    ax.bar(labels, means, bottom=stack_sums)
    stack_sums = get_bottom_list(stack_sums, means)

ax.set_ylabel('Assholes')
ax.set_title('Assholes per group and gender')

plt.show()
