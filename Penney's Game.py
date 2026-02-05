from random import choice
    
def main():
    print("Let's play the Penney's game! Here are the rules:")
    print("""
    You declare a sequence of three coin toss results,
    then I declare mine
    then I toss a fair coin any numbers at a time until my chosen sequence
    or yours appears, whoever has the sequence that appears first,
    that person is the winner.

    Let's do a better of five.
    """)

    winner = start_round()

    player_count = 0
    computer_count = 0

    while True:
        player_count += 1 if winner == "Player" else 0
        computer_count += 1 if winner == "Computer" else 0

        print(f"Player: {player_count}\nComputer: {computer_count}")

        if player_count >= 3:
            print("You won 3 out of 5, you beat me!")
            break
        elif computer_count >= 3:
            print("I won 3 out of 5, I beat you!")
            break
        else:
            print("Alright, let's go again!")
            print("="*50)
            winner = start_round()
    

def start_round() -> str:    
    print("You first!")
    
    player_sequence = get_player_sequence()

    computer_sequence = get_computer_sequence(player_sequence)

    print(f"I made my sequence\nYour sequence: {player_sequence}\nMy sequence: {computer_sequence}\nNow, let's flip the coins!")

    seq = ""
    count = 0
    while True:
        input("[Press Enter to Flip the Coin]")
        coin = choice(["Tails", "Heads"])
        seq += "T" if coin == "Tails" else "H"
        print(f"Coin result: {coin}")
        print(f"Coins flips = {seq}")
        count += 1

        if count >= 3:
            if seq[:3] == player_sequence:
                print("You won!")
                return "Player"
            if seq[:3] == computer_sequence:
                print("I won!")
                return "Computer"
            if seq[count-3:count] == player_sequence:
                print("You won!")
                return "Player"
            if seq[count-3:count] == computer_sequence:
                print("I won!")
                return "Computer"
    
    

def get_player_sequence() -> str:
    print("Enter sequence like 'HHT'\nH - Heads\nT - Tails")
    while (seq := str(input('> ')).strip().upper()) not in ["HHH", "HHT", "HTH", "HTT", "THH", "THT", "TTH", "TTT"]:
        print("Invalid input. Try again.")
    return seq

def get_computer_sequence(player_sequence: str) -> str:
    return ("T" if player_sequence[1] == "H" else "H") + player_sequence[0] + player_sequence[1]


if __name__ == "__main__":
    main()
