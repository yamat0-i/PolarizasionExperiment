import questionary

from analyzer.models import input_data
from analyzer.models import fiber_measure
from analyzer.models import s_parameter
from analyzer.views import console

DEFAULT_ROBOT_NAME = 'Analyzer'

class Analyzer(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        self.name = name
        self.user_name = user_name

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning."""
        temp_hello = console.get_template('hello.txt')
        print(temp_hello.format(robot_name=DEFAULT_ROBOT_NAME))
        
    def menu(self):
        what_to_do = questionary.select(
            "Select mode.", 
            choices=["Input", "Analyze"],
            ).ask()
        if what_to_do == "Input":
            input_data.main()
        if what_to_do == "Analyze":
            self.menu_2()

    def menu_2(self):
        what_to_do = questionary.select(
            "Select one to analyze.", 
            choices=["Fiber Diameter", 
                     "S Parameter"],
            ).ask()
        if what_to_do == "Fiber Diameter":
            fiber_measure.main()
        if what_to_do == "S Parameter":
            s_parameter.main()
    
    def goodbye(self):
        temp_goodbye = console.get_template('goodbye.txt')
        print(temp_goodbye.format(robot_name=DEFAULT_ROBOT_NAME))