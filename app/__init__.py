from app.presenter import BasePresenter


# ToDo 2018/03/10 set file location or name dynamically
def init_app():
    base_presenter = BasePresenter("Personal-Projects_2018-03-09.json")
    base_presenter.generate_resource_map()


if __name__ == '__main__':
    init_app()
