import sys
sys.path.append('modules')
sys.path.append('modules/model')
sys.path.append('modules/view')
sys.path.append('modules/controller')
from model import main
from view import home
from controller import controller


def main():
    showGUI = home.GUI()



if __name__ == '__main__':
    main()