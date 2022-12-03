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
    }

letter_to_outcome = {
    'X': Outcome.LOSE,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN,
    }

win_lose_score = {
    # oponent choice, outcome, your choice
    (Choice.ROCK, Outcome.DRAW): Choice.ROCK,
    (Choice.ROCK, Outcome.WIN): Choice.PAPER,
    (Choice.ROCK, Outcome.LOSE): Choice.SCISSORS,
    (Choice.PAPER, Outcome.LOSE): Choice.ROCK,
    (Choice.PAPER, Outcome.DRAW): Choice.PAPER,
    (Choice.PAPER, Outcome.WIN): Choice.SCISSORS,
    (Choice.SCISSORS, Outcome.WIN): Choice.ROCK,
    (Choice.SCISSORS, Outcome.LOSE): Choice.PAPER,
    (Choice.SCISSORS, Outcome.DRAW): Choice.SCISSORS,
    }

def calc_score(opponent, outcome):
    """Caclulate the score for a round"""
    return win_lose_score[(opponent, outcome)].value + outcome.value

def main():
    """Solve the Problem"""
    score = 0
    with open('./input.txt') as f:
        for line in f:
            opponent_letter, outcome_letter = line.strip().split(' ')
            opponent = letter_to_choice[opponent_letter]
            outcome = letter_to_outcome[outcome_letter]
            score += calc_score(opponent, outcome)

    print(score)


if __name__ == '__main__':
    main()
