"""

Creating a Logic Controller to control the logic part of the Laser Job Manager

David SAnchez Sanchez


"""
class LogicController():

    def __init__(self, guiController=None):
        self.guiController = guiController

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller

    def getGuiController(self):
        return self.guiController
