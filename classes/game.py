import random
from .character import Character
from .story_generator import Story
"""
Sequence of objects:

showStory, interactiveStory, checkGameEnd, choiceSelection. showHealth
"""

class Game:
    def __init__(self, char: Character, script: Story, difficulty=5):
        self.end = False
        self.character = char
        self.script = script
        self.difficulty = difficulty

    def choiceSelection(self):
        print(self.script.choice_moment)
        invalid_choice = True
        while invalid_choice:
            choice = input("What do you choose? Choice A or B?\n")
            if choice.lower() == 'a':
                self.script = self.script.choice_a
                invalid_choice = False
            elif choice.lower() == 'b':
                self.script = self.script.choice_b
                invalid_choice = False
            else:
                print("Invalid choice. Please enter a or b.\n")
        return None

    def showStory(self):
        if not self.script.story_node:
            return False
        else:
            print(self.script.story_node)
            return True

    def interactiveStory(self):
        if self.script.story_type == 'normal':
            pass
        elif self.script.story_type == 'luck_damage':
            luck_barrier = random.randint(3, 9)
            if self.character.luck < luck_barrier:
                if self.difficulty > 5:
                    self.character.health -= random.randint(30, 50)
                    print("You have received damage, your current health is {}\n".format(self.character.health))
                else:
                    self.character.health -= random.randint(20, 40)
                    print("You have received damage, your current health is {}\n".format(self.character.health))
            else:
                if self.difficulty > 5:
                    self.character.health -= random.randint(15, 20)
                    print("You have received damage, your current health is {}\n".format(self.character.health))
                else:
                    self.character.health -= random.randint(10, 16)
                    print("You have received damage, your current health is {}\n".format(self.character.health))
                pass
        elif self.script.story_type == 'chapter_end':
            pass
        else:
            raise ValueError("No such story type.\n")
        return None

    def showHealth(self):
        print("Your remaining health is {}\n".format(self.character.getHealth()))
        return None