# Rock Paper Scissors!

## Let's play! You have to return which player won! In case of a draw return Draw!.

"""
def rps(p1, p2):
    rules = {
        ("rock", "scissors"): "Player 1 won!",
        ("scissors", "paper"): "Player 1 won!",
        ("paper", "rock"): "Player 1 won!",
    }
    if p1 == p2:
        return "Draw!"
    elif (p1, p2) in rules:
        return rules[(p1, p2)]
    else:
        return "Player 2 won!"
"""

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
