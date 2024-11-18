#allen gaines
#11/18/24
#p5hw
#making a game


import random


def generate_spell(spell_name, attack_damage, mana):
    """
    Generate spell details based on character attributes.
    
    Args:
        spell_name (str): Name of the spell
        attack_damage (float): Character's attack damage
        mana (float): Character's mana points
    
    Returns:
        dict: Spell details
    """
    spell_types = {
        "fire ball": {
            "damage": attack_damage * 1.5,
            "mana_cost": mana * 0.3,
            "description": "Launches a powerful fireball"
        },
        "ice punch": {
            "damage": attack_damage * 1.2,
            "mana_cost": mana * 0.25,
            "description": "Freezes target with an icy strike"
        },
        "air bullet": {
            "damage": attack_damage * 1.3,
            "mana_cost": mana * 0.2,
            "description": "Shoots a compressed air projectile"
        }
    }
    
    # Use the spell or generate a random one if not found
    spell_details = spell_types.get(spell_name.lower(), 
        random.choice(list(spell_types.values())))
    
    return spell_details
#create character 

def create_character():
    """
    Create a game character dictionary with user-specified attributes.
    
    Returns:
    dict: A dictionary containing the character's attributes
    """
    # Prompt for character attributes
    name = input("Enter character name: ")
    
    # Use error handling to ensure numeric inputs
    while True:
        try:
            attack_damage = float(input("Enter attack damage: "))
            break
        except ValueError:
            print("Please enter a valid number for attack damage.")
    
    while True:
        try:
            mana = float(input("Enter mana points: "))
            break
        except ValueError:
            print("Please enter a valid number for mana.")
    while True:
        try:
            health = float(input("Enter health points: "))
            break
        except ValueError:
            print("Please enter a valid number for health.")
    
    spell_name = input("Enter character's signature spell(fire ball,ice punch, air bullet): ")
    
    # Create the character dictionary with spell generation
    character = {
        "name": name,
        "attack_damage": attack_damage,
        "mana": mana,
        "health": health,
        "spell_name": spell_name,
        "spell": generate_spell(spell_name, attack_damage, mana)
    }
    
    return character
#display charaxter 

def display_character(character):
    """
    Display character details with emoji formatting.
    
    Args:
        character (dict): Character dictionary
    """
    print("🔥🔥🔥🔥🔥🔥🔥🔥")
    for key, value in character.items():
        if key == 'spell':
            print("Spell Details:")
            for spell_key, spell_value in value.items():
                print(f"  {spell_key}: {spell_value}")
        else:
            print(f"{key}: {value}")
    print("🔥🔥🔥🔥🔥🔥🔥🔥")
    #battle system 
def battle(attacker, defender):
    """
    Simulate a battle between two characters.
    """
    max_damage = attacker['spell']['damage']
    damage_dealt = random.uniform(0, max_damage)
    
    defender['health'] -= damage_dealt
    defender['health'] = max(defender['health'], 0)
    
    print(f"🔥 {attacker['name']} attacks {defender['name']} with {attacker['spell_name']}!")
    print(f"💥 Damage dealt: {damage_dealt:.2f}")
    print(f"❤️ {defender['name']} remaining health: {defender['health']:.2f}")
    
    return defender

def battle_simulation(char1, char2):
    """
    Simulate a complete battle between two characters.
    """
    round_number = 1
    while char1['health'] > 0 and char2['health'] > 0:
        print(f"\n🏹 Round {round_number}")
        
        # First character attacks
        char2 = battle(char1, char2)
        if char2['health'] <= 0:
            print(f"🏆 {char1['name']} wins!")
            break
        
        # Second character attacks
        char1 = battle(char2, char1)
        if char1['health'] <= 0:
            print(f"🏆 {char2['name']} wins!")
            break
        
        round_number += 1

def main():
    """
    Main game initialization function.
    """
    print("Game is starting")
    print("Create first character")
    char1 = create_character()
    print("Create second character")
    char2 = create_character()
    
    display_character(char1)
    display_character(char2)
    battle_simulation(char1, char2)

# Call the main function
if __name__ == "__main__":
    main()
