"""Controller for polarization experiment"""
from analyzer.models import robot

def controller():
    analyzer  = robot.Analyzer()
    analyzer.hello()
    analyzer.menu()
    analyzer.goodbye()
