import sys
from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3

letter_to_choice = {
    'A': Choice.ROCK,
    'B': Choice.PAPER,
    'C': Choice.SCISSORS,
    'X': Choice.ROCK,
    'Y': Choice.PAPER,
    'Z': Choice.SCISSORS,
    }

win_lose_score = {
    # oponent choice, your choice, score
    (Choice.ROCK, Choice.ROCK): Outcome.DRAW,
    (Choice.ROCK, Choice.PAPER): Outcome.WIN,
    (Choice.ROCK, Choice.SCISSORS): Outcome.LOSE,
    (Choice.PAPER, Choice.ROCK): Outcome.LOSE,
    (Choice.PAPER, Choice.PAPER): Outcome.DRAW,
    (Choice.PAPER, Choice.SCISSORS): Outcome.WIN,
    (Choice.SCISSORS, Choice.ROCK): Outcome.WIN,
    (Choice.SCISSORS, Choice.PAPER): Outcome.LOSE,
    (Choice.SCISSORS, Choice.SCISSORS): Outcome.DRAW,
    }

def calc_score(opponent, you):
    """Caclulate the score for a round"""
    return win_lose_score[(opponent, you)].value + you.value

def main():
    """Solve the Problem"""
    score = 0
    with open('./input.txt') as f:
        for line in f:
            opponent, me = line.strip().split(' ')
            score += calc_score(letter_to_choice[opponent], letter_to_choice[me])

    print(score)



if __name__ == '__main__':
    main()
