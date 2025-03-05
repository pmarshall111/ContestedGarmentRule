from math import floor


def min_gt_0(arr):
    curr_min = 2**31-1
    for elem in arr:
        if elem > 0 and elem < curr_min:
            curr_min = elem
    if curr_min == 2**31-1:
        raise RuntimeError("No elem found > 0")
    return curr_min


def constrained_equal_gainz(demand, supply):
    allocation = [0]*len(demand)
    while floor(supply) > 0: # Avoid floating point errors
        remaining_demand = [d-a for d,a in zip(demand, allocation)]
        # TODO: Handle exception
        to_add = min_gt_0(remaining_demand)
        shared_across = sum(i > 0 for i in remaining_demand)
        if to_add * shared_across < supply:
            max_share = to_add
        else:
            max_share = supply / shared_across
        for idx,dem in enumerate(remaining_demand):
            if dem > 0:
                allocation[idx] += max_share
                supply -= max_share
        
    return allocation


def constrained_equal_losses(demand, supply):
    total_demand = sum(demand)
    return [d-a for d,a in zip(demand, constrained_equal_gainz(demand, total_demand - supply))]


def contested_garment(demand, supply):
    total_demand = sum(demand)
    half_dem = [dem/2 for dem in demand]
    if supply <= total_demand/2:
        return constrained_equal_gainz(half_dem, supply) 
    else:
        allocs = constrained_equal_losses(half_dem, supply-total_demand/2)
        return [a1+a2 for a1,a2 in zip(half_dem, allocs)]