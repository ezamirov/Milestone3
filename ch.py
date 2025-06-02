# ---------- Chapter 4: Paranoia and Manipulation ----------

def chapter_four():
    print("\n--- Chapter 4: Paranoia and Manipulation ---")
    print("It felt like the walls were closing in on me. The truth was scarier than I imagined.")
    
    # Face experiment leader
    face_leader()
    
    # Unravel memory manipulation
    unravel_manipulation()
    
    # Decide to reveal truth or hide
    reveal = reveal_or_hide_truth()
    
    # Strange event about missing man
    ghostly_figure()
    
    return reveal
    
def face_leader():
    print("\nYou confront the person most involved in the experiment, demanding answers.")
    input("Press Enter to listen carefully...")
    print("Their confession is chilling and confirms the extent of the manipulation.")
    
def unravel_manipulation():
    print("\nYou uncover evidence that villagers' memories have been altered deliberately to hide the truth.")
    input("Press Enter to piece together the puzzle...")
    print("Paranoia sets in as you question everyone around you.")
    
def reveal_or_hide_truth():
    print("\nYou face a decision:")
    choice = input("Do you (1) Reveal the truth to the villagers or (2) Protect them by hiding it? Enter 1 or 2: ")
    if choice == '1':
        print("You choose to reveal the whole truth, no matter the consequences.")
        return True
    elif choice == '2':
        print("You decide some secrets are better left buried.")
        return False
    else:
        print("Invalid choice, please try again.")
        return reveal_or_hide_truth()
    
def ghostly_figure():
    print("\nA strange event: the missing man appears as a ghostly figure, hiding in plain sight within the village.")
    input("Press Enter to steady your nerves...")