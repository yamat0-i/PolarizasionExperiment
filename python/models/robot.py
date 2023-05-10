import questionary
from questionary import Style

from models import input_data
from models import analyze
from views import console

DEFAULT_ROBOT_NAME = 'Analyzer'

class Analyzer(object):
    """Base model for Robot."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        self.name = name
        self.user_name = user_name

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning."""
        template = console.get_template('hello.txt')
        print(template.format(robot_name=DEFAULT_ROBOT_NAME))
        
        what_to_do = questionary.select(
            "What do you want to do?", 
            choices=["Input", "Analyze"],
            ).ask()
        if what_to_do == "Input":
            print("OK. Start inputting.")
            input_data.main()
        if what_to_do == "Analyze":
            print("OK. Start analyzing.")
            # analyze.main()