from learntools.python import jimmy_slots
graph = jimmy_slots.get_graph()
graph

def prettify_graph(graph):
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")
    ticks = graph.get_yticks()
    new_labels = ['${}'.format(int(amt)) for amt in ticks]
    graph.set_yticklabels(new_labels)

print('\n')
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
best_items(full_dataset)
print('\n')

def blackjack_hand_greater_than(hand_1, hand_2):
     total_1 = total_2 = 0
    hand1, hand2 = hand_1, hand_2
    for i in range(len(hand_1)):
        if hand_1[i] == 'J' or hand_1[i] == 'Q' or hand_1[i] == 'K':
            total_1 += 10
        elif hand_1[i] == 'A':
            total_1 += 1
        else:
            total_1 += int(hand_1[i])
            
    while 'A' in hand1:
        if total_1 + 10 <= 21:
            total_1 += 10
        hand1.pop(hand1.index('A'))
            
    
    for i in range(len(hand_2)):
        if hand_2[i] == 'J' or hand_2[i] == 'Q' or hand_2[i] == 'K':
            total_2 += 10
        elif hand_2[i] == 'A':
            total_2 += 1
        else:
            total_2 += int(hand_2[i])
    while 'A' in hand2:
        if total_2 + 10 <= 21:
            total_2 += 10
        hand2.pop(hand2.index('A'))

    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)

print('\n')

print('\n')

print('\n')
