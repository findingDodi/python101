import matplotlib.pyplot as plt
from operator import add


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 20, 27]
women_means = [0, 0, 0, 35, 0]
other_means = [5, 5, 5, 5, 5]
another_means = [5, 5, 5, 5, 5]
print(men_means + women_means)
print(list(map(add, men_means, women_means)))

fig, ax = plt.subplots()
ax.bar(labels, men_means, label='Men')
ax.bar(labels, women_means, bottom=men_means, label='Women')
ax.bar(labels, other_means, bottom=list(map(add, men_means, women_means)), label="other")
ax.bar(labels, other_means, bottom=list(map(add, list(map(add, men_means, women_means)), other_means)), label="another")

ax.set_ylabel('Assholes')
ax.set_title('Assholes per group and gender')
ax.legend()

plt.show()
