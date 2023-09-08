def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else :
        return 0;
print('\n')
def to_smash(total_candies):
    if total_candies==1:
        print("Splitting 1 candie" )
    else :
        print("Splitting", total_candies, "candies")
        return total_candies % 3
print('\n')
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False
(not (rain_level > 0)) and is_workday
not (rain_level > 0 and is_workday)
print(actual)
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number <0
print('\n')
def wants_all_toppings(ketchup, mustard, onion):
    return ketchup and mustard and onion
print('\n')
def wants_plain_hotdog(ketchup, mustard, onion):
    return not (ketchup or mustard or onion)
print('\n')
def exactly_one_sauce(ketchup, mustard, onion):
    return (ketchup and not mustard) or (mustard and not ketchup)
print('\n')
def exactly_one_topping(ketchup, mustard, onion):
    return (int(ketchup) + int(mustard) + int(onion)) == 1
