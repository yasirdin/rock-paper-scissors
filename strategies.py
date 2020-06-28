import random

# Complex strategies will require historical information for each player.
# For this, we can use a Strategies object which RockPaperScissors inherits.
# And, RockPaperScissors will need to be updated to store historical moves.


def default_random_choice() -> str:
    # Randomly select option, each with equal probability
    return random.choice(['rock', 'paper', 'scissors'])

