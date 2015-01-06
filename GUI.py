import Tkinter as tk

class GUI():
    def __init__(self):
        print 'GUI::init'

    def run(self):
        print 'ǴUI::run'

def main():
    print 'test'
    gui = GUI()
    gui.run()

if __name__=="__main__":
    main()
