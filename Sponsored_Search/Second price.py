import math
import numpy as np
import matplotlib.pyplot as plt
import itertools

'''
This function includes both allocation and calculation of to-be-paid bid and returns rubsequently the utility
'''
def cal_benefit(my_value, my_bid, other_bids, item_ctr):
    # bids ist the vector contains all bids but bidder 1
    # empty list to store sorted bids
    bidList = []
    # my_bid the highest rank
    counter = 0
    # numbers of bidder with the same bids as me
    num_same = 1
    result = 0
    bidList.append(my_bid)

    for i in other_bids:
        if i > my_bid:
            counter += 1
        if i == my_bid:
            num_same += 1
        bidList.append(i)

    # to make sure there is always a lower bid to match when calculating the result, avoid array out of range
    bidList.append(0)
    bidList.sort(reverse=True)

    for i in range(counter, counter + num_same):
        result += item_ctr[i] * 1 / num_same * (my_value - bidList[i + 1])

    return result

'''
Main part of the realization of SODA 
'''
def sponsored_search_second(end_time, n, bidders, item_ctr):
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

                        # new utility for bidder 1 when offering bid 1, value 1
                        utilities[bid_1] += beta_product * cal_benefit(value_1, bid_1, bid_combi, item_ctr) / n

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


sponsored_search_second(10, 10, 3, [2, 2, 2])
