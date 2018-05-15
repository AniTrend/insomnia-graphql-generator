import sys
from app.presenter import BasePresenter, PersistencePresenter


def init_app(filename=None):
    base_presenter = BasePresenter(filename)
    base_presenter.create_resources()
    
    persistence_presenter = PersistencePresenter(base_presenter)
    persistence_presenter.create_directories()

    print("-----------------------------------")
    print("End of execution")
    print("-----------------------------------")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].__contains__('.json'):
            init_app(sys.argv[1])
        else:
            print(sys.argv[1] + " is not a valid file.")
    else:
        print("All files must be placed inside the .app/io/input directory before hand.")
        print("Usage: python3 __init__.py filename.json")
        print("e.g. python3 __init__.py workspace_2018-04-29.json")
