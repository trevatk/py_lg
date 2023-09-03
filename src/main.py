"""entry point of the application"""
import logging

from http_server import serve


def main():
    """main function"""
    logging.basicConfig(level=logging.INFO)
    # start http server
    serve()


if __name__ == "__main__":
    main()
