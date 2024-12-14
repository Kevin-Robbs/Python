import random

class SnakesAndLadders():
    die1 = 0
    die2 = 0
        
    def roll(self, player):
        ladders = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 51:67, 71:91, 78:98, 87:94}
        snakes = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}
        
        self.die1 = random.randint(1,6)
        self.die2 = random.randint(1,6)
        
        sum = self.die1 + self.die2
        print(f'You rolled a(n) {sum} {player.name}')
        
        player.score += sum
        
        if player.score > 100:
            print("Looks like your went over 100, you will be sent back to your tile.")
            player.score -= sum
        
        if player.score in ladders:
            self.climbLadder(player, ladders[player.score])
        elif player.score in snakes:
            self.snakeSlide(player, snakes[player.score])
        
        print(f"Your score is {player.score}")
    
    def climbLadder(self, player, tile):
        print("Looks like you hit a ladder, you lucky dog you!!")
        player.score = tile
    
    def snakeSlide(self, player, tile):
        print("Oh no, you landed on a snake and have started to slide")
        player.score = tile
        
class Player(SnakesAndLadders):
    def __init__(self, name = ""):
        self.name = name
        self.score = 0
        
def play():
    
        player1_name = input("Enter Player One's name: ")
        player1 = Player(player1_name)
        player2_name = input("Enter Player Two's name: ")
        player2 = Player(player2_name)
        
        welcome_message= f"""
    Welcome to Snakes and Ladders {player1.name} and {player2.name}!

    You both will alternate turns as you roll a pair of dice to advance along the board. 
    Scattered across the board are Snakes and Ladders. If you land on a snake, you will fall down
    the board but if you land on a ladder, you will climb further along the board. 

    First person to reach 100, WINS!!!!

    Good luck to the both of you!!
    """
        print(welcome_message)
        print("")
        still_playing = True
        while still_playing:
            
            player_turn = player1
            
            if player_turn == player1:
                decision = input(f"Here are your options {player1.name} (R)oll or (Q)uit: ")
                
                if decision:
                    if decision.lower() == "r":
                        player1.roll(player1)
                        if player1.score >= 100:
                            print(f"{player1.name} wins !!!")
                            break
                        player_turn = player2
                    elif decision.lower() == "q":
                        print(f'{player1.name} quit')
                        still_playing = False
                else:
                    print("Hmm, I don't understand that input. please try again")
                    continue
                print("")
                
            if player_turn == player2:
                
                decision = input(f"Here are your options {player2.name} (R)oll or (Q)uit: ")
                if decision:
                    if decision.lower() == "r":
                        player2.roll(player2)
                        if player2.score >= 100:
                            print(f"{player2.name} wins!!!")
                            break
                        player_turn = player1
                    elif decision.lower() == "q":
                        print(f'{player2.name} quit')
                        still_playing = False
                else:
                    print("Hmm, I don't understand that input. please try again")
                    continue
                print("")