import math

import numpy as np
import matplotlib.pyplot as plt


def simple_soda(end_time, n):
    # initialize the strategy table of two dimension with the probability 1/n+1
    beta = np.zeros((n + 1, n + 1))
    beta[:, :] = 1 / (n + 1)

    #iteration frequency
    for t in range(1, end_time + 1):
        #iterate over all possible discrete values for bidder 1
        for value_1 in range(0, n+1):
            utilities = {}
            #iterate over all possible discrete bids for bidder 1
            for bid_1 in range(0, n + 1):
                utilities[bid_1] = 0
                # iterate over all possible discrete values for bidder 2
                for value_2 in range(0, n + 1):
                    # iterate over all possible discrete bids for bidder 2
                    for bid_2 in range(0, n + 1):
                        if bid_1 > bid_2:
                            utilities[bid_1] += (value_1 - bid_1) * beta[value_2, bid_2] / ((n + 1)**2)
                        elif bid_1 == bid_2:
                            utilities[bid_1] += (value_1 / (n + 1) - bid_1 / (n + 1)) * beta[value_2, bid_2] / (
                                        2 * ((n + 1)**2))

            #implementation of the update part
            summary = 0
            for bid_1 in range(0, n+1):
                summary += math.exp(1/math.sqrt(t)*utilities[bid_1]) * beta[value_1, bid_1]
            for bid_1 in range(0, n + 1):
                instrument = math.exp(1 / math.sqrt(t) * utilities[bid_1])

                beta[value_1, bid_1] = (beta[value_1, bid_1] * instrument) / summary

    # drawing the graph


    # Set the new axis values
    x_vals = np.round(np.linspace(0, 1, n + 1), 2)
    y_vals = np.round(np.linspace(0, 1, n + 1), 2)

    # Create a figure and axes object
    fig, ax = plt.subplots()

    # Plot the array using imshow()
    im = ax.imshow(beta.transpose(), cmap='viridis', interpolation='nearest', origin='lower',
                   extent=[x_vals[0], x_vals[-1], y_vals[0], y_vals[-1]])

    ax.set_xlabel('value')
    ax.set_ylabel('bid')

    # Set the tick values and labels
    ax.set_xticks(x_vals[::5])  # Use only every 5th tick
    ax.set_xticklabels(x_vals[::5])  # Use only every 5th label
    ax.set_yticks(y_vals)
    ax.set_yticklabels(y_vals)

    cbar = ax.figure.colorbar(im, ax=ax)
    plt.show()


simple_soda(10000, 10)

