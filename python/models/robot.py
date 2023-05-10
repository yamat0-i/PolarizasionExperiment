import string

import questionary

# from models import input_data
from models import analyze
from views import console

DEFAULT_ROBOT_NAME = 'Analyzer'

class Analyzer(object):
    """Base model for Robot."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='',
                 speak_color='blue'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning."""
        template = console.get_template('hello.txt', self.speak_color)
        template.substitute({'robot_name': self.name})
        what_to_do = questionary.select(
            "What do you want to do?", 
            choices=["Input", "Analyze"]
            ).ask()
        if what_to_do == "Input":
            print("OK. Start inputting.")
            # input_data.main()
        if what_to_do == "Analyze":
            print("OK. Start analyzing.")
            # analyze.main()