import random
team_name = 'The name the team gives to itself' # Only 10 chars displayed.

strategy_name = 'The name the team gives to this strategy'

strategy_description = 'How does this strategy decide?'

    

def move(my_history, their_history, my_score, their_score):
    if random.random()<0.4: # 40% of the other rounds
        return 'b'         # Betray
    else:
        return 'c'         # but 60% of the time collude
