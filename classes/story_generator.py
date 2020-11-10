class Story:
    """
        A class used to represent a Story within the game. Since text adventure games are branching games with usually
        only two choices, a Story can be represented as a binary tree, where each node contains a story, with its left
        child denoting another story node denoting what happens if you choose choice A, and its right node denoting
        another story node denoting what happens if you choose choice B.

        The creation of such a class is to facilitate the creation of stories, which will allow the game designer to
        create branching stories in a non-confusing manner given that the game designer will be able to choose on
        whether the story is an ending, or a decision point and then insert the corresponding stories for whatever
        choice the user has made.

        ...

        Attributes
        ----------
        story : str
                Story to be displayed on screen. Story should either be an ending (a leaf) where no choices are present
                and a decision point (a node) where the user will be able to choose choice A or choice B which is itself
                a story node / leaf.

        Methods
        -------

        __init__ : Initializes the story based on the list of strings (lines) given
        """

    def __init__(self, story: str, moment,  type, choice_a=None, choice_b=None):
        self.story_node = story
        self.choice_moment = moment
        self.story_type = type
        self.choice_a = choice_a
        self.choice_b = choice_b

    def insert_story_text(self, inserted_story: str, inserted_story_moment : str, choice_a_bool: bool, type="normal"):
        if choice_a_bool:
            if self.choice_a is None:
                self.choice_a = Story(inserted_story, inserted_story_moment, type)
            else:
                raise (ValueError("Choice A already exists for this story.\n"))
        else:
            if self.choice_b is None:
                self.choice_b = Story(inserted_story, inserted_story_moment, type)
            else:
                raise (ValueError("Choice B already exists for this story.\n"))

    def insert_story_node(self, inserted_story_node, choice_a_bool: bool):
        if choice_a_bool:
            if self.choice_a is None:
                self.choice_a = inserted_story_node
            else:
                raise (ValueError("Choice A already exists for this story.\n"))
        else:
            if self.choice_b is None:
                self.choice_b = inserted_story_node
            else:
                raise (ValueError("Choice B already exists for this story.\n"))
