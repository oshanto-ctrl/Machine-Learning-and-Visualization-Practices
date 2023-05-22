import matplotlib.pyplot as plt

# plt.style.use('seaborn')
plt.style.use('seaborn-ticks')

inputs = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fx, ax = plt.subplots()
ax.plot(inputs, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Squared values", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()

