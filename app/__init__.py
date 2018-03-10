from app.presenter import BasePresenter, PersistencePresenter


def init_app():
    base_presenter = BasePresenter("Personal-Projects_2018-03-10.json")
    base_presenter.create_resources()
    print()
    persistence_presenter = PersistencePresenter(base_presenter)
    persistence_presenter.create_directories()
    print()
    print("-----------------------------------")
    print("End of execution")
    print("-----------------------------------")


if __name__ == '__main__':
    init_app()
