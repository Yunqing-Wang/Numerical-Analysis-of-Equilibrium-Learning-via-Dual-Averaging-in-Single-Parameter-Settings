import math
import numpy as np
import matplotlib.pyplot as plt
import itertools

'''
This function implements the first half of the VCG function
'''
def calMarketWithMe(my_bid, my_value, other_bids, item_ctr):
    # other_bids ist the vector contains all bids but bidder 1
    #empty list to store sorted bids
    bidList = []
    # numbers of bidder with the highest bids as me
    counter = 0
    # number of bidders with higher bids than me
    num_same = 1
    result = 0

    for i in other_bids[0:]:
        if my_bid < i:
            counter += 1
        if my_bid == i:
            num_same += 1

        bidList.append(i)

    bidList.append(my_bid)

    bidList.sort(reverse=True)

    for i in range(0, len(bidList)):
        result += bidList[i] * item_ctr[i]
    #With (counter + num_same - 1) we take the worst possible allocation
    #implementation of the first half of the VCG function
    result = result - item_ctr[counter + num_same - 1] * my_bid + item_ctr[counter + num_same - 1] * my_value

    return result

'''
This function implements the second half of the VCG function
'''
def calMarketWithoutMe(other_bids, item_ctr):
    bidList = []
    result = 0

    for i in other_bids:
        bidList.append(i)

    bidList.sort(reverse=True)

    for i in range(0, len(bidList)):
        result += bidList[i] * item_ctr[i]

    return result

'''
Main part of the realization of SODA 
'''
def vcg(end_time, n, bidders, item_ctr):
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
                        utilities[bid_1] += beta_product * (
                                calMarketWithMe(bid_1, value_1, bid_combi, item_ctr) - calMarketWithoutMe(bid_combi,
                                                                                                          item_ctr)) / n
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


vcg(10, 10, 3, [10, 2])
