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
    