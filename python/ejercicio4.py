def select_second(L):
    if len(L) < 2:
        return None
    return L[1]
print('\n')
def losing_team_captain(teams):
    return teams[-1][1]
print('\n')
def purple_shell(racers):
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1]=temp

print('\n')
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]
lengths = [3, 2, 0, 2]
print('\n')
def fashionably_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
print('\n')
