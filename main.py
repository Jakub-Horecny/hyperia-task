"""
File that runs the program
"""

from website_parser import Parser


def run() -> None:
    """
    Runs the program
    :rtype: None
    """
    parser: Parser = Parser()
    parser.get_all_jobs_from_website()


if __name__ == '__main__':
    run()
