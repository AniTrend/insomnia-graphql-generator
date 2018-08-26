import argparse
import os

from app import PersistencePresenter, BasePresenter
from app.util import InputOutputHelper


def __description() -> str:
    return "Convert your insomnia collections to GraphQL files. This application helps you generate .graphql files " \
           "from a GraphQL export workspace in insomnia so you can use it in projects like Apollo or " \
           "retrofit-graphql for android."


def __usage() -> str:
    return "manage.py --file ./app/io/input"


def __init_command_line_interface() -> argparse:
    parser = argparse.ArgumentParser(description=__description(), usage=__usage())
    parser.add_argument('-f', '--file', default=None,
                        help="load file from a given directory path")
    parser.add_argument('-i', '--input', default=None,
                        help="load the given file in the input directory")
    return parser


def __print_program_end() -> None:
    print("-----------------------------------")
    print("End of execution")
    print("-----------------------------------")


def __init_app(args: argparse) -> None:
    filename = args.file
    if args.input is not None:
        filename = os.path.join(InputOutputHelper.get_input_directory(), args.input)
    if filename is not None:
        base_presenter = BasePresenter(filename)
        base_presenter.create_resources()
        persistence_presenter = PersistencePresenter(base_presenter)
        persistence_presenter.create_directories()
        __print_program_end()
    else:
        print()
        print("For instructions on how to use this program, please run:\nmanage.py --help")


if __name__ == '__main__':
    __init_app(__init_command_line_interface().parse_args())
