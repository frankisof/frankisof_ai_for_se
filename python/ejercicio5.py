def has_lucky_number(nums):
    return any ([num%7==0 for num in nums])
print('\n')
def elementwise_greater_than(L, thresh):
    return [ele >thresh for ele in L]
print('\n')
def menu_is_boring(meals):
    return any (x==y for x,y in zip(meals, meals [1:])) 
    for dish in range(len(meals)-1):
        if meals[dish] == meals [dish+1]:
            return True
        return False 
print('\n')
def estimate_average_slot_payout(n_runs):
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    avg_payout = sum(payouts) / n_runs
    return avg_payout

estimate_average_slot_payout(10000000)
print('\n')

print('\n')

print('\n')

print('\n')
