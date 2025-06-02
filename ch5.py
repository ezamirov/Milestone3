 ---------- Chapter 5: Final Confrontation ----------

def chapter_five():
    print("\n--- Chapter 5: Final Confrontation ---")
    print("The village was no longer the place I once knew. The truth changed everything.")
    
    # Psychological battle
    psychological_battle()
    
    # Face past and accept responsibility
    face_past()
    
    # Decide village fate
    fate = decide_fate()
    return fate
    
def psychological_battle():
    print("\nYou enter a psychological battle with the mastermind of memory manipulation.")
    input("Reality shifts and your perceptions blur...")
    print("You must stay strong to confront your own mind.")
    
def face_past():
    print("\nYou finally face your role in the experiments and their tragic consequences.")
    input("Press Enter to accept your fate...")
    print("It is a heavy burden but one you must carry.")
    
def decide_fate():
    print("\nYou must decide the fate of the village.")
    choice = input("Do you (1) Reveal the whole truth risking division, or (2) Keep the secret to maintain peace? Enter 1 or 2: ")
    if choice == '1':
        print("You choose to expose the truth, whatever the cost.")
        return True
    elif choice == '2':
        print("You keep the secret, protecting the village from harm.")
        return False
    else:
        print("Invalid choice, please try again.")
        return decide_fate()

# ---------- Main game flow ----------

def play_game():
    chapter_one()
    chapter_two()
    choice3 = chapter_three()
    if not choice3:
        print("\nYou turned back at the abandoned facility. Your journey ends here.")
        return
    choice4 = chapter_four()
    choice5 = chapter_five()
    print("\n--- Game Over ---")
    if choice5:
        print("You revealed the truth. The village will never be the same.")
    else:
        print("You chose to keep the secret. Peace remains, but at what cost?")

if __name__ == "__main__":
    play_game()