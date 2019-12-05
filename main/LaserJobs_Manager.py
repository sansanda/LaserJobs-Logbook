from Gui.GuiController import GuiController
from Logic.LogicController import LogicController

def main():
    lc = LogicController()
    gc = GuiController(lc)
    lc.setGuiController(gc)



if __name__ == "__main__":
    main()