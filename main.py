from classes.story_generator import Story
from classes.character import Character
from classes.game import Game

def main():
    character_name = input("What is the name of your character?\n")
    while True:
        try :
            character_type = input(
                "Do you want to have a lucky or strong character? Input lucky or strength to indicate your "
                "choice.\n")
            new_character = Character(character_name, character_type)
            break
        except ValueError:
            print("That was not a valid character type. Please try again.\n")
    story = Story("Test Story.", "normal")
    story.insert_story_text(story, "choice a", True)
    story.insert_story_text(story, "choice b", False)
    new_game = Game(new_character, story)
    while not new_game.end:
        new_game.showStory()
        new_game.interactiveStory()
        new_game.checkGameEnd()
        if new_game.script.choice_a is None and new_game.script.choice_b is None:
            print("Game ended.\n")
            break
        else:
            new_game.choiceSelection()
            new_game.showHealth()

    return None

if __name__ == '__main__':
    main()
