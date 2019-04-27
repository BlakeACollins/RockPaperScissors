# Rock Paper Scissors by Blake Collins
# Udacity's Inrto to Programming

import random


moves = ['rock', 'paper', 'scissors']


class Player():
    my_move = None
    their_move = None

    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))


class HumanPlayer(Player):
    def move(self):
        show = input("Select your move: Rock, Paper, or Scissors? ")
        while show != 'rock' and show != 'paper' and show != 'scissors':
            print("Wrong input. Please select your move")
            show = input("rock, paper, scissors?")
        return (show)


class ReflectPlayer(Player):
    def move(self):
        if self.their_move == 'paper':
            return 'paper'
        elif self.their_move == 'scissors':
            return 'scissors'
        else:
            return 'rock'


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


class Game():

    def __init__(self, my_move, their_move):
        self.p1 = my_move
        self.p2 = their_move
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("Player One Wins!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player Two Wins!")
            self.p2_score += 1
        else:
            print("It's a Tie!")

    def play_game(self):
        print("Game start!")
        number_rounds = int(input("How many rounds would you like to play? "))
        for round in range(number_rounds):
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("Player One Wins!")
        elif self.p1_score < self.p2_score:
            print("Player Two Wins!")
        else:
            print("It's a Tie Game!")
            print("The final score is " + str(self.p1_score) +
                  " to " + str(self.p2_score))
            print("Game over!")


if __name__ == '__main__':
    strategies = {
        "1": Player(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer()
    }

    user_input = input("Please select the type of player "
                       "you would like to play against: "
                       "1-Rock Player, "
                       "2-Random Player, "
                       "3-Cycle Player, or  "
                       "4-Reflect Player: ")

    game = Game(HumanPlayer(), strategies[user_input])
    game.play_game()
