import math
import numpy as np
import matplotlib.pyplot as plt
import itertools

'''
This function determines if bidder 1 will be assigned with an item
'''
def allocation_rule(my_bid, bids, num_item):
    # bids ist the vector contains all bids but bidder 1
    # numbers of bidder with the same bids as me
    num_same = 1
    # number of bidders with higher bids than me
    counter = 0

    for i in bids[0:]:
        if my_bid < i:
            counter += 1
        if my_bid == i:
            num_same += 1

    # the number of higher bids than me is greater equal than the number of ietms, therefore I won't get any item
    if counter >= num_item:
        return 0
    else:
        # case where I own the highest bid, the probability to get the item is 1
        if counter == 0:
            if num_same == 1:
                return 1

        # other cases
        result = (num_item-counter)/num_same
        if result > 1:
            return 1
        return result

'''
This function deliveries the bid bidder 1 needs to pay
'''
def payment_rule(bid1, allocation):
    return bid1 * allocation

'''
This function calculates the distribution formula
'''
def power_rule(alpha, value):
    return math.pow(value, alpha-1)
'''
This function calculates the distribution formula
'''
def exponential_distribution(lamda, value):
    return math.pow(2, -lamda * value)


'''
Main part of the realization of SODA 
'''
def multiunit_soda_first_prior(end_time, n, bidders, num_item, priortype, parameter): #priortype = 1 power law priortype = 2 exponential distribution
    # initialize the strategy table of two dimension with the probability 1/n+1
    beta = np.zeros((n + 1, n + 1))
    beta[:, :] = 1 / (n + 1)


    # generate the needed value and bid combinations
    range_values = range(0, n + 1)
    value_combinations = list(itertools.product(range_values, repeat=bidders - 1))
    bid_combinations = list(itertools.product(range_values, repeat=bidders - 1))


    prior_table = np.zeros(n+1)
    prefactor = 1

    if priortype == 1:
        # modify alpha and calculate the contant part α*...*α
        prefactor = math.pow(parameter, bidders - 1)
        # generate the table when using power law
        for i in range(0, n + 1):
            prior_table[i] = power_rule(parameter, i/n)
    elif priortype == 2:
        #modify the lamda and calculate the contant part λ*...*λ
        prefactor = math.pow(parameter, bidders-1)
        # generate the table when using exponential distribution
        for i in range(0, n + 1):
            prior_table[i] = exponential_distribution(parameter, i/n)

    # iteration number
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

                        #calculate the product of the prior distributions of other bidders
                        prior_product = 1
                        for k in range(0, bidders - 1):
                            prior_product *= prior_table[value_combi[k]]

                        assignment = allocation_rule(bid_1, bid_combi, num_item)

                        # new utility for bidder 1 when offering bid 1, value 1
                        utilities[bid_1] += beta_product * prefactor * prior_product * (assignment * value_1 - payment_rule(bid_1, assignment)) / n

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



multiunit_soda_first_prior(10, 20, 3, 1, 2, 10)
