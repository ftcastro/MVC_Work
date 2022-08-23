"""The entry point was fixed with the correct class names"""

from controllers.interface_controller import AbstractController


if __name__ == '__main__':
    controller = AbstractController()
    controller.main()
