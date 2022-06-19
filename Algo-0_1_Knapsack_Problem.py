'''
Knapsack problem: given a set of items with respective weights and values. Given the maximum weight constraint, find a subset of items that have maximum values.

0/1 means we cannot split the item. If not 0/1, we can first sort items by value, add items from the most valuable until we reach the maximum weight. Then split the last item so it fits into the weight constraint.
'''
# %%
'''
Bottom-up dynamic programming approach
'''
def knapsack(values, weights, maxWeightConstraint):
    '''
    Args:
        values: list of int indicating the values of the items
        weights: list of int indicating the weights of the items
        maxWeightConstraint: int indicating the maximum weight constraint
    '''
    cache = [[0 for _ in range(maxWeightConstraint + 1)] for _ in range(len(values) + 1)]

    for total_items in range(len(values) + 1):
        for max_weight in range(maxWeightConstraint + 1):

            current_item = total_items - 1

            if total_items == 0 or max_weight == 0:
                cache[total_items][max_weight] = 0
            elif weights[current_item] > max_weight:
                cache[total_items][max_weight] = cache[total_items - 1][max_weight]
            else:
                with_item = cache[total_items - 1][max_weight - weights[current_item]] + values[current_item]
                without_item = cache[total_items - 1][max_weight]
                cache[total_items][max_weight] = max(with_item, without_item)
    
    return cache[-1][-1]


values = [60, 50, 70, 30]
weights = [5, 3, 4, 2]
maxWeight = 8
knapsack(values, weights, maxWeight)

# %%
