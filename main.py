from classes.character import Character
from classes.game import Game
from scripts import script_loading as Script
import time

def main():
    character_name = input("What is the name of your character?\n")
    time.sleep(0.5)
    while True:
        try :
            character_type = input(
                "Do you want to have a lucky or strong character? Input lucky or strength to indicate your "
                "choice.\n")
            new_character = Character(character_name, character_type)
            break
        except ValueError:
            print("That was not a valid character type. Please try again.\n")
    story = Script.scenario_1
    new_game = Game(new_character, story)
    print("Character History:\n")
    print("It is early 1942. You are a junior officer at the rank of Lieutenant in the Imperial Japanese Army who was "
          "prompted to sign on with the army shortly after graduation from Waseda University due to your strong "
          "patriotism.\n")
    #time.sleep(4)
    print("Character Attribute:\n")
    if new_character.role_type == 'lucky':
        print("Furthermore, you have always been sure of your luck as well. Since youth, you have always been saved "
              "from unfortunate incidents due to sheer luck despite having partaken in them, and you regularly win "
              "small amounts of money from gambling with your friends as well.\n\nBeing confident of your luck, you "
              "are sure that you will be able to survive and get out of dangerous situations with luck on your side.\n")
        #time.sleep(4)
    else:
        print("Furthermore, you have always been sure of your physical fitness and ability as well. Since youth, you "
              "have always been first in local athletic events, and have even represented your university in "
              "Volleyball and Baseball.\n\nYou are sure that even if you are placed in a pinch, your athletic ability "
              "and toughness will allow you to survive and adapt to most situations.\n")
        #time.sleep(4)
    print("Initial Health:\n")
    print("Your character has initial health of {}\n".format(new_game.character.getHealth()))
    #time.sleep(2.5)
    while not new_game.end:
        new_game.showStory()
        #time.sleep(6.5)
        new_game.interactiveStory()
        #time.sleep(6.5)
        if new_game.character.health <= 0:
            print("Oh no, your health has reached 0. You have died!\n")
            break
        else:
            pass
        if new_game.script.story_type == 'chapter_end':
            new_game.showHealth()
            new_game.script = new_game.script.choice_a
        else:
            if new_game.script.choice_a is None and new_game.script.choice_b is None:
                print("Game has ended.\n")
                new_game.end = True
            else:
                new_game.choiceSelection()
                #time.sleep(1)
                new_game.showHealth()
                #time.sleep(1)
    end = input("Thanks for playing! Click Enter to exit the game.")
    if end is not None:
        return None
    return None

if __name__ == '__main__':
    main()
