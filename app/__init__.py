import os
import sys
from app.presenter import BasePresenter, PersistencePresenter


def init_app(filename=None):
    
    base_presenter = BasePresenter(filename)
    base_presenter.create_resources()
    
    print()
    
    persistence_presenter = PersistencePresenter(base_presenter)
    persistence_presenter.create_directories()
    
    print()
    print("-----------------------------------")
    print("End of execution")
    print("-----------------------------------")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            init_app(sys.argv[1])
        else:
            print(sys.argv[1] + " is not a valid file.")
    else:
        print("Usage: app.py [filename]")
