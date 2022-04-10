from src.controller import Controller
from src.model import Model
from src.interface import Interface


def main():
    app = Controller(Model(), Interface())
    app.start_app()


if __name__ == '__main__':
    main()
