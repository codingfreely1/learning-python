import random

who_won = {'rockrock': 0,
           'paperpaper': 0,
           'scissorsscissors': 0,
           'rockscissors': 1,
           'paperrock': 1,
           'scissorspaper': 1,
           'scissorsrock': 2,
           'rockpaper': 2,
           'paperscissors': 2
           }


def rock_paper_scissors():
    player1 = raw_input('choose rock|paper|scissors|q to quit:')
    while player1 != 'q':
        player2 = computer_hand()
        print ('computer choose: ' + player2)
        key = player1 + player2
        winner = who_won[key]
        if winner == 0:
            print 'Tie'
        elif winner == 1:
            print 'You Won!'
        else:
            print 'Try Again'
        player1 = raw_input('choose rock|paper|scissors|q to quit:')


def computer_hand():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)


rock_paper_scissors()
