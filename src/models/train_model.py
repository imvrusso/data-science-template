import os
import logging
from dotenv import find_dotenv, load_dotenv


def main():
    """ Runs scripts to train models (saved in ../models)
        on processed data from (../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('training models on processed data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_fmt='%Y-%m-%d %H:%M:%S'
    logging.basicConfig(level=logging.INFO, format=log_fmt, datefmt=date_fmt)

    load_dotenv(find_dotenv())

    main()
