import random

class Character:
    """
    A class used to represent a Character within the game.

    ...

    Attributes
    ----------
    name : str
        The name of the character (as of now limited to be a Japanese soldier) in World War 2. User-specific.

    role_type: str
        The type of character to be created. Options include 'lucky', i.e. a soldier who is usually more lucky in
        urgent situations. A soldier's luck is rated between 1 to 10, where lucky soldiers always have luck values of
        between 8 to 10, whilst normal soldiers will only have a luck rated between 1 to 8. The values are randomly
        generated based on the random number generator in Python's random number generator. A 'strength' based soldier
        will meanwhile have higher health points, which means that the soldier can take on more damage before death.

    luck: int
        A measure of how lucky a soldier can be in situations

    health: int
        A measure of how resistant to damage a soldier is. Once health reaches 0, the soldier dies and the story is
        over.

    Methods
    -------

    __init__ : Initializes the character used based on user speciic input.

    """
    def __init__(self, name, role_type):

        """
        Parameters:

        :param name: str
            Name of the soldier to be used during the story.
        :param role_type: str
            The type of soldier to be used during the story. Can only either be lucky or strength types.
        """

        self.name = name
        self.role_type = role_type
        if role_type != 'lucky' and role_type != 'strength':
            raise ValueError("role_type can only either be lucky or strength.\n")
        if role_type == 'lucky':
            self.luck = random.randint(8, 10)
        else:
            self.luck = random.randint(1, 8)
        if role_type == 'strength':
            self.health = random.randint(100, 130)
        else:
            self.health = random.randint(60, 90)

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health
