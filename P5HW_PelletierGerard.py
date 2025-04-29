# Gerard Pelletier
# 4/8/2025
# P5HW
# An assignment about making a game using python
# This game will be about a dungeon escape


import random
import time


def createCharacter():
    username = input("'What is your name, adventurer?': ")
    inventory_list = []
    healthpoints = 100
    character = {"inventory": inventory_list, "name": username, "health": healthpoints}
    print()
    print(f"'{character['name']}...Interesting. Well {character['name']}, this dungeon is a labrinyth of suffering, you will be lucky to survive. First, you need to get out of the cell your in. Then, you will have to fight the guard to escape. Choose your next move wisely.'")
    time.sleep(1)
    return character


def start(character):
    lock_chipped = 'false'
    swing_again = 'Y'
    plank_snapped = 'false'
    hand_broken = 'false'
    rock_shattered = 'false'
    bars_bent = 'false'
    print(f"Now, your faced with a dilemma. This mysterious robed man did not hand you a key. He simply expects you to bust out of this cell yourself, as if he was testing your worthiness.")
    print()
    time.sleep(1)
    print(f"Before you lies a few options. You could use a stray rock to break the chains of the lock off the door, you could try and break it with your hands or use a sturdy plank of wood to pry the old iron bars open.")
    time.sleep(1)
    print()
    door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)

def door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent):
    if plank_snapped == 'true' and rock_shattered == 'true' and hand_broken == 'true':
        print(f"You have exhausted all your options. The hooded man shakes his head and walks away, disgusted. You are destined to never leave this cell.")
        print(f"Sending you back to the start...")
        time.sleep(5)
        print()
        main() 
        return

    choice1 = input("What do you suppose you should try? The rock, your fist or the plank?: ").lower()
    print()

    if choice1 == 'plank':
        if plank_snapped == 'true':
            print(f"Your plank is shattered. You cannot use it to pry the bars open.")
            door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
            print()

        while swing_again == 'Y' and plank_snapped == 'false':
            plank_integer = random.randint(1,10)
            print(f"Your roll was {plank_integer}...")
            if bars_bent == 'true':
                time.sleep(1)
                plank_integer += 1
                print(f"You already bent the bars, so you get +1 to your roll. Your roll was actually {plank_integer}!")
            print()
            time.sleep(1)
            if plank_integer >= 8:
                print(f"You are able to pry the bars open with the plank, keeping the plank intact. You are able to slip out and proceed out of the cell.")
                door_open_scene(character, rock_shattered, plank_snapped, hand_broken)
                return

            if plank_integer == 7:
                print(f"You are able to pry open the bars, but the plank snaps in the process. You lose the potential weapon, but atleast you got out of the cell.")
                plank_snapped = 'true'
                door_open_scene(character, rock_shattered, plank_snapped, hand_broken)
                return

            if plank_integer <= 6 and plank_integer >= 3:
                print(f"The plank bends the bars a little, but does not open it enough. You have made progress, though.")
                bars_bent = 'true'
                time.sleep(1)
                swing_choice = input("Should you try again? Y/N: ").upper()
                if swing_choice == 'Y':
                    swing_again = 'Y'
                else: 
                    door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
                    break
                print()

            if plank_integer <= 2:
                print(f"You bent the bars, but unfortunately, you bent the plank more. It snaps in your hands and is thus unusuable. The robed man looks down upon you with massive disappointment.")
                plank_snapped = 'true'
                door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
                break


    if choice1 == 'fist':
        if hand_broken == 'true':
            print(f"You would be a fool to use a broken hand to punch at a lock. Pick another option.")
            door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
            print()
        while swing_again == 'Y' and hand_broken == 'false':
            hand_integer = random.randint(1,10)
            print(f"Your roll was {hand_integer}...")
            if lock_chipped == 'true':
                time.sleep(1)
                hand_integer += 1
                print(f"You already chipped the lock, so you get +1 to your roll. Your roll is now {hand_integer}!")
            print()
            time.sleep(1)
            if hand_integer >= 9:
                print(f"Your fist manages to loosen the lock, allowing you to pull it apart and open the door.")
                door_open_scene(character, rock_shattered, plank_snapped, hand_broken)
                return

            elif hand_integer <= 9 and hand_integer >= 3:
                print(f"Your hand hurts like hell and you didnt do much damage to the lock. You lost 10 HP.")
                time.sleep(1)
                character['health'] = character['health'] - 10
                print(f"You now have {character['health']} HP.")
                time.sleep(1)
                swing_choice = input("Should you try again? Y/N: ").upper()
                if swing_choice == 'Y':
                    swing_again = 'Y'
                else: 
                    door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
                    break
                print()

            elif hand_integer <= 2:
                print(f"You break your knuckles like glass on the lock and are unable to use it. It was your dominant hand unfortunately, which means swinging your fist is no longer an option. You also lost 20 HP.")
                character['health'] = character['health'] - 20
                time.sleep(1)
                print(f"You now have {character['health']} HP.")
                time.sleep(1)
                print(f"While the hooded man may have his face obscured, you can feel a judgemental frown shining down on your sorry head. You better find a way to get out, and fast...")
                hand_broken = 'true'
                door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
                print()
                break
        
    if choice1 == 'rock':
        if rock_shattered == 'true':
            print(f"You shattered the rock, it is now a mess of tiny pieces. Its useless in your lock picking endeavor.")
            door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
            print()
        while swing_again == 'Y' and rock_shattered == 'false':
            rock_integer = random.randint(1,10)
            print(f"Your roll was {rock_integer}...")
            if lock_chipped == 'true':
                time.sleep(1)
                rock_integer += 1
                print(f"You already chipped the lock, so you get +1 to your roll. Your roll is now {rock_integer}!")
            print()
            if rock_integer < 8 and rock_integer >= 4:
                print(f"The rock chips the lock, but does not break it. You still have the rock in your hands, as it did not shatter.")
                time.sleep(1)
                lock_chipped = 'true'
                swing_choice = input("Should you try again? Y/N: ").upper()
                if swing_choice == 'Y':
                    swing_again = 'Y'
                else: 
                    door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
                    break

            elif rock_integer <= 4 and rock_integer >= 1:
                print(f"The rock shatters on the lock, making it unusuable.")
                rock_shattered = 'true'
                print(f"While the hooded man may have his face obscured, you can feel a judgemental frown shining down on your sorry head. You better find a way to get out, and fast...")
                print()
                door_function(character, lock_chipped, swing_again, plank_snapped, hand_broken, rock_shattered, bars_bent)
                print()
                break

            elif rock_integer >= 8:
                print(f"The rock shatters the fragile, rusty lock. The door opens and you can proceed.")
                door_open_scene(character, rock_shattered, plank_snapped, hand_broken)
                return


def door_open_scene(character, rock_shattered, plank_snapped, hand_broken):
    print()
    print("=========="*5)
    print()
    print(f"You finally escape your cell, the hooded man already walking off down the hallway, as if he was guiding you out.")
    print()
    time.sleep(1)
    print(f"'I hope you didn't break any of those tools in your cell. You will need them to overcome the guard.")
    print()
    time.sleep(1)
    if rock_shattered == 'true' and plank_snapped == 'true' and hand_broken == 'true':
        print(f"How do i say this...you're in biiiiiig trouble.")
    elif rock_shattered == 'true' and plank_snapped == 'true':
        print(f"You realize how much trouble you are in. You will have to fight this guard with nothing but your fists.")
    elif rock_shattered == 'true' and plank_snapped == 'false':
        print(f"All hope is not lost, you still have the big piece of sturdy plywood to fight with.")
    elif rock_shattered == 'false' and plank_snapped == 'true':
        print(f"You can still clobber the guard with the rock, fortunately...")
    elif rock_shattered == 'false' and plank_snapped == 'false' and hand_broken == 'true':
        print(f"Your hand might be broken, but you have two of them. You'll manage.")
    else:
        print(f"You more than prepared. Lets get the party started.")
    time.sleep(1)
    print()
    print("=========="*5)
    print()
    print(f"You adventure through the halls with your hooded companion, but soon you would find the guard he talked to you about. It was time to do battle.")
    time.sleep(1)
    print()
    print(f"'Halt right there, prisoner! I will not let you leave!'")
    time.sleep(1)
    guard_health = 100
    guard_helmet = 'has his helmet'
    guard_battle(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet)

def guard_battle(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet):
    if character['health'] <= 0:
        print()
        print()
        print(f"The You have been knocked unconscious and brought back to your cell. Maybe you will escape another day.")
        print(f"-------GAME OVER!-------")
        print(f"Sending you back to the start...")
        time.sleep(5)
        print()
        main() 
        return
    print()
    print(f"The guard has {guard_health} HP. He currently {guard_helmet}. You currently have {character['health']} HP.")
    print()
    choice2 = input("What weapon will you choose? The rock, your fist, or the plank?: ").lower()

    if choice2 == 'rock':
        if rock_shattered == 'true':
            time.sleep(1)
            print(f"That rock shattered on the lock during your escape. Try another weapon.")
            guard_battle(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet)
        rock_integer = random.randint(1,10)
        print(f"Your roll was {rock_integer}...")
        if guard_helmet != 'has his helmet':
            guard_health - 5
            print(f"The guard doesnt have his helmet and is extra vulnerable! You will do 5 more damage to him!")
        if rock_integer >= 9:
            print(f"Critical Hit! You did 20 damage!")
            guard_health = guard_health - 20
        elif rock_integer <= 8 and rock_integer >= 4:
            print(f"Moderate hit! You did 10 damage.")
            guard_health = guard_health - 10
        elif rock_integer <= 3:
            print(f"Mediocre hit! You did 5 damage.")
            guard_health = guard_health - 5
        time.sleep(1)
        guard_turn(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet)
        return
    if choice2 == 'fist':
        if hand_broken == 'true':
            time.sleep(1)
            print(f"Your hand is mangled beyond use. Try another weapon.")
            guard_battle(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet)
        hand_integer = random.randint(1,10)
        print(f"Your roll was {hand_integer}...")
        if guard_helmet != 'has his helmet':
            guard_health - 5
            print(f"The guard doesnt have his helmet and is extra vulnerable! You will do 5 more damage to him!")
        if hand_integer >= 9:
            print(f"Critical Hit! You did 15 damage and dislodged his helmet!")
            guard_health = guard_health - 15
            guard_helmet = 'doesnt have his helmet'
        elif hand_integer <= 8 and hand_integer >= 4:
            print(f"Moderate hit! You did 5 damage.")
            guard_health = guard_health - 5
        elif hand_integer <= 3:
            print(f"You slammed your fist into his armor and ended up hurting yourself more than him. You lose 5 hp.")
            character['health'] = character['health'] - 5
        time.sleep(1)
        guard_turn(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet)
        return
    if choice2 == 'plank':
        if plank_snapped == 'true':
            time.sleep(1)
            print(f"The plank snapped opening the bars. It served you well for the moment, but it will serve you no longer.")
            guard_battle(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet)
        plank_integer = random.randint(1,10)
        if guard_helmet != 'has his helmet':
            guard_health - 10
            print(f"The guard doesnt have his helmet and is extra vulnerable! You will do 10 more damage to him!")
        print(f"Your roll was {plank_integer}...")
        if plank_integer >= 7:
            print(f"Critical Hit! You did 15 damage!")
            guard_health = guard_health - 15
        elif plank_integer <= 6:
            print(f"Moderate hit! You did 10 damage.")
            guard_health = guard_health - 10
        elif plank_integer <= 5:
            print(f"Mediocre hit! You did 5 damage.")
            guard_health = guard_health - 5
        time.sleep(1)
        guard_turn(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet)
        return
    

        
        
    

def guard_turn(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet):
    print("=========="*5)
    if guard_health <= 0:
        print()
        print()
        print(f"The guard has fallen unconscious! You can finally exit this forsaken prison and become a free man once more!")
        print(f"-------GAME OVER!-------")
        return
    guard_attack = random.randint(1,10)
    print(f"The guards roll was {guard_attack}...")
    if guard_attack >= 9:
        character['health'] = character['health'] - 20
        print(f"The guard landed a critical hit! He deals 20 damage to you! You have {character['health']} HP left.")
    elif guard_attack <= 8 and guard_attack >= 4:
        character['health'] = character['health'] - 10
        print(f"He landed a good swing on you with his fist, dealing 10 damage to you. You have {character['health']} HP left.")
    elif guard_attack <= 3:
        print(f"You are elusive and the guard missed!")
    guard_battle(character, rock_shattered, plank_snapped, hand_broken, guard_health, guard_helmet)
    return


        



def main():
    print(f"This is a game about escaping a dungeon with the help of a mysterious man. Would you like to begin?")
    playing = input("Y/N: ").upper()
    if playing != 'Y':
        print("I suppose you are content with your imprisonment. Until next time...")
        return
    print("You wake up in a dungeon, having been imprisoned by the kings forces. Your cell is cold, wet and depressing. While wallowing in your saddness, you spot a hooded figure approaching your cell. He calls out to you in a chilling voice, seeming to offer assistance.")
    character = createCharacter()
    print()
    start(character)


if __name__ == "__main__":
    main()


