def proportional(demand, supply):
    total_demand = sum(demand)
    if total_demand < supply:
        return total_demand.copy()
    
    return [supply*dem/total_demand for dem in demand]