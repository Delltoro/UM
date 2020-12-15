# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from utils.metric import metrics_list
from utils.preprocess import preprocs_list

# Set data
df = pd.DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'var1': [38, 1.5, 30, 4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
})


# ------- PART 1: Define a function that do a plot for one line of the dataset!

def generateChart2(scores,row, title, color):
    cmap = plt.cm.get_cmap('Spectral')
    print(cmap)

    # number of variable
    I = scores.shape[0]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(I) * 2 * pi for n in range(I)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(2, 2, row + 1, polar=True, color='grey', size=8)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], row, color='grey', size=8)
    plt.xticks(angles[:-1], metrics_list)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
    plt.ylim(0, 40)

    # uzupelnianie wykresu danymi
    for method_id, method in enumerate(preprocs_list):
        values = scores[:, method_id].tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=method)
        ax.fill(angles, values, color='blue', alpha=0.4)


    # Add a title
    plt.title(title, size=11, color='yellow', y=1.1)

    # ------- PART 2: Apply to all individuals
    # initialize the figure
    my_dpi = 96
    plt.figure(figsize=(1000 / my_dpi, 1000 / my_dpi), dpi=my_dpi)
