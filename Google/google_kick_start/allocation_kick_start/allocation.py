test_cases = int(input())

for case in range(test_cases):
    number_of_houses, budget = [int(_) for _ in input().split()]
    house_costs = [int(_) for _ in input().split()]
    house_costs.sort()
    maximum_houses_can_buy = 0
    for cost in house_costs:
        budget -= cost
        if budget >= 0:
            maximum_houses_can_buy += 1
        else:
            break
    print(f"Case #{case+1}: {maximum_houses_can_buy}")
