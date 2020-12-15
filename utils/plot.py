import matplotlib.pyplot as plt
from utils.metric import metrics_list
from utils.preprocess import preprocs_list

def generateChart(scores):

    I = scores.shape[0]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(I) * 2 * 3.14 for n in range(I)]
    angles += angles[:1]

    ax = plt.subplot(111, polar=True)

    ax.set_theta_offset(3.14/2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], metrics_list)

    ax.set_rlabel_position(0)
    plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], ["0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1"], color="grey", size=7)
    plt.ylim(0,1)

    #uzupelnianie wykresu danymi
    for method_id, method in enumerate(preprocs_list):
        values = scores[:, method_id].tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=method)

    #legenda
    plt.legend(bbox_to_anchor=(1.15, -0.05), ncol=5)

    plt.savefig("findings/radar", dpi=200)