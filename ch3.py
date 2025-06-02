# ---------- Chapter 3: The Abandoned Facility ----------

def chapter_three():
    print("\n--- Chapter 3: The Abandoned Facility ---")
    print("The building stood in eerie silence, as if waiting for me to go inside...")
    
    # Explore lab
    explore_lab()
    
    # Discover missing person's involvement
    missing_person_info()
    
    # Flashback to unethical actions
    unethical_flashback()
    
    # Make choice
    choice = reveal_truth_or_turn_back()
    return choice
    
def explore_lab():
    findings = [
        "Medical files marked with strange symbols.",
        "Journals filled with disturbing experiment notes.",
        "Photographs of villagers undergoing trials.",
        "A hidden room with locked cabinets."
    ]
    print("\nYou explore the abandoned research lab.")
    input("Press Enter to search...")
    print(f"Found: {random.choice(findings)}")
    
def missing_person_info():
    print("\nYou discover evidence that the missing man was a participant in the experiment and may have uncovered a dangerous secret.")
    
def unethical_flashback():
    print("\nA sudden flashback reveals your involvement in these experiments, showing moments of moral conflict and regret.")
    
def reveal_truth_or_turn_back():
    print("\nYou uncover disturbing truths about the experiments.")
    choice = input("Do you want to (1) Reveal the truth or (2) Turn back? Enter 1 or 2: ")
    if choice == '1':
        print("You decide to reveal the truth, no matter the cost.")
        return True
    elif choice == '2':
        print("You choose to protect yourself by turning away from the past.")
        return False
    else:
        print("Invalid choice, please try again.")
        return reveal_truth_or_turn_back()
