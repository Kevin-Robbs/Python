import random
import os

def hit_me():
    card_list = ['King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'Ace']
    cards_values = {'King': 10, 'Queen': 10, 'Jack': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'Ace': 0}
    card = random.choice(card_list)
    value = cards_values[f'{card}']
    
    print(f'You pulled a {card}')
    print(' ')
    
    if card == 'Ace':
        print('Do you want it to be worth 11 points or 1 point?')
        ace_value = 0

        while ace_value != '1' and ace_value != '11':
            ace_value = input('Enter 1 or 11: ')

        value = int(ace_value)

    return value

continue_game = ''

while continue_game !=  'n':
    os.system('cls')
    print('Welcome to 21')
    print(' ')
    print('Here is your first draw...')
    print(' ')

    dealer_score = random.randrange(15,30)
    user_score = 0
    user_score = user_score + hit_me()

    print(f'Your current score: {user_score}')
    print(' ')
    user_input = input('Continue? (type "s" to stop): ')
    print(' ')
    os.system('cls')
    while user_input != 's':
        user_score = user_score + hit_me()
        print(f'Your current score: {user_score}')
        print(' ')
        if user_score > 21:
            print('You busted!')
            if dealer_score > 21:
                print('so did the dealer though, so its a draw!')
                print(f'Dealers score is: {dealer_score}')
                print(' ')
            else:
                print('The dealer won this one!')
                print(f'Dealers score is: {dealer_score}')
                print(' ')
            break
        user_input = input('Continue? (type "s" to stop)')
        print(' ')
        os.system('cls')

    if user_input == 's':
        if dealer_score > 21:
            print('Looks like the dealer busted! You win!!')
            print(f'Your score is {user_score} and the dealer score is {dealer_score}')
            print(' ')
        else:
            u_score = 21 - user_score
            d_score = 21 - dealer_score
            
            if u_score < d_score:
                print("You win!!")
                print(f'Your score is {user_score} and the dealer score is {dealer_score}')
                print(' ')
            elif d_score < u_score:
                print('You lost this one, maybe next time')
                print(f'Your score is {user_score} and the dealer score is {dealer_score}')
                print(' ')
            else:
                print('Seems we have a draw')
                print(f'Your score is {user_score} and the dealer score is {dealer_score}')
                print(' ')

    continue_game = input("Would you like to play again? Enter any key to continue or type 'n' to exit.")
