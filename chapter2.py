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
