import numpy as np
import matplotlib.pyplot as plt

def plot(x, y1, y2):
    fig, axs = plt.subplots(1, 2)
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    axs[0].scatter(x, y1)
    axs[1].scatter(x, y2)
    plt.show()