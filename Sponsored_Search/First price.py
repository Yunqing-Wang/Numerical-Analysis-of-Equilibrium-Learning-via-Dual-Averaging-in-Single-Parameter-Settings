import math
import numpy as np
import matplotlib.pyplot as plt
import itertools

'''
This function determines which slot will be assigned to bidder 1
'''
def allocation_rule(my_bid, bids, item_ctr):
    # bids ist the vector contains all bids but bidder 1
    num_same = 1  # numbers of bidder with the same bids as me
    counter = 0  # number of bids which are higher than mein, also the rank position of my bids among all
    result = 0
    for i in bids[0:]:
        if my_bid < i:
            counter += 1
        if my_bid == i:
            num_same += 1

    #calculate the averaged CTR which bidder 1 can get
    for j in range(counter, counter + num_same):
        result += item_ctr[j] / num_same

    return result

'''
This function deliveries the bid bidder 1 needs to pay
'''
def payment_rule(bid1, allocation):
    return bid1 * allocation

'''
Main part of the realization of SODA 
'''
def sponsored_search_first(end_time, n, bidders, item_ctr):
    # initialize the strategy table of two dimension with the probability 1/n+1
    beta = np.zeros((n + 1, n + 1))
    beta[:, :] = 1 / (n + 1)
    # make the item set as long as the bidders when there are fewer items than bidders
    while len(item_ctr) < bidders:
        item_ctr.append(0)

    # generate the needed value and bid combinations
    range_values = range(0, n + 1)
    value_combinations = list(itertools.product(range_values, repeat=bidders - 1))
    bid_combinations = list(itertools.product(range_values, repeat=bidders - 1))

    for t in range(1, end_time + 1):
        # iterate over all possible discrete values for bidder 1
        for value_1 in range(0, n + 1):
            utilities = {}
            # iterate over all possible discrete bids for bidder 1
            for bid_1 in range(0, n + 1):
                utilities[bid_1] = 0
                # iterate through all possible value and bid combinations for other bidders
                for value_combi in value_combinations:
                    for bid_combi in bid_combinations:
                        beta_product = 1
                        # calculate the product of strategies of other bidders
                        for j in range(0, bidders - 1):
                            beta_product *= beta[value_combi[j], bid_combi[j]]

                        assignment = allocation_rule(bid_1, bid_combi, item_ctr)

                        # new utility for bidder 1 when offering bid 1, value 1
                        utilities[bid_1] += beta_product * (assignment * value_1 - payment_rule(bid_1, assignment)) / n

            # implementation of the update part
            summary = 0
            for bid_1 in range(0, n + 1):
                summary += math.exp(1 / math.sqrt(t) * utilities[bid_1]) * beta[value_1, bid_1]
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


sponsored_search_first(10, 20, 3, [10, 5, 1])
