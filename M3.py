import random

# ---------- Chapter 1: Return to Barnaul ----------

def chapter_one():
    print("\n--- Chapter 1: Return to Barnaul ---")
    print("The village was the last place I ever wanted to go back to. The air here always seemed heavier...")
    
    # Interact with locals
    villager_interaction()
    
    # Explore disappearance location
    explore_location()
    
    # Talk to family/friends of missing person
    talk_to_family()
    
    # Follow clues to forest
    follow_forest_clues()
    
def villager_interaction():
    npc_names = ["Lorenzo", "Isabella", "Francesco", "Beatrice", "Giovanni"]
    responses = [
        "Have you come about the disappearance?",
        "I haven't seen him in days. Strange times.",
        "People say the forest hides dark secrets.",
        "Beware who you trust here in Barnaul.",
        "My family has suffered enough already."
    ]
    npc = random.choice(npc_names)
    response = random.choice(responses)
    
    print(f"\n{npc}: Hello stranger, what brings you to Barnaul?")
    answer = input("Press 'y' to talk, or any other key to walk away: ").lower()
    if answer == 'y':
        print(f"{npc}: {response}")
    else:
        print(f"{npc}: Very well, stay safe.")
        
def explore_location():
    clues = [
        "You find a torn piece of fabric caught on a branch.",
        "There are strange footprints leading into the forest.",
        "An old, broken watch lies near the riverbank.",
        "You spot a hidden symbol carved into a tree trunk."
    ]
    print("\nYou arrive at the site of the disappearance.")
    input("Press Enter to search for clues...")
    
    clue_found = random.choice(clues)
    print(f"Clue found: {clue_found}")
    
def talk_to_family():
    responses = [
        "They were worried about something but never told me.",
        "He was acting strange in the days before disappearing.",
        "We hope they come back soon, we miss them dearly."
    ]
    print("\nYou meet with the family and close friends of the missing person.")
    input("Press Enter to listen to their stories...")
    
    print(f"Family says: {random.choice(responses)}")
    
def follow_forest_clues():
    print("\nFollowing the clues, you head towards a secluded spot in the forest...")
    input("Press Enter to continue...")
    print("The forest feels cold and unnerving, something is hidden here.")
    

# ---------- Chapter 2: Shadows of the Past ----------

def chapter_two():
    print("\n--- Chapter 2: Shadows of the Past ---")
    print("As darkness fell, I felt fear, as if the shadows themselves were watching me...")
    
    # Search records linked to past
    search_past_records()
    
    # Talk to elderly villagers
    talk_elderly()
    
    # Memory flashbacks
    memory_flashback()
    
    # Follow first sign into forest
    forest_structure()
    
def search_past_records():
    records = [
        "A dusty ledger linking the village to strange experiments.",
        "Old letters referencing psychological trials.",
        "Faded sketches of apparatus used long ago.",
        "Notes describing unusual behavior of villagers."
    ]
    print("\nYou search old records for connections to your past.")
    input("Press Enter to examine the documents...")
    print(f"Found record: {random.choice(records)}")
    
def talk_elderly():
    elderly_responses = [
        "I remember those days... things weren't normal.",
        "You were involved in something dangerous back then.",
        "Many of us tried to forget what happened.",
        "Some say the village still suffers from those experiments."
    ]
    print("\nYou speak with the elderly villagers about your previous work.")
    input("Press Enter to listen...")
    print(f"Elderly villager: {random.choice(elderly_responses)}")
    
def memory_flashback():
    memories = [
        "You recall a shadowy figure watching you from the courtyard.",
        "Fragments of an experiment you once led come rushing back.",
        "You hear faint whispers about forbidden knowledge and control.",
        "A flash of a scandal that ruined your reputation strikes you."
    ]
    print("\nYour mind drifts to the past...")
    input("Press Enter to remember...")
    print(f"Memory: {random.choice(memories)}")
    
def forest_structure():
    print("\nFollowing a sign, you enter the forest deeper and discover a strange structure hidden beneath thick vines.")
    input("Press Enter to investigate the structure...")
    print("The air feels charged with old secrets.")


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
    

# ---------- Chapter 5: Final Confrontation ----------

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