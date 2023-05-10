"""Controller for polarization experiment"""
from models import robot

def controller():
    analyzer  = robot.Analyzer()
    analyzer.hello()
