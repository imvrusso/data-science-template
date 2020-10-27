import os
import logging
from dotenv import find_dotenv, load_dotenv


def main():
    """ Runs scripts to use trained models from (../models)
        to make predictions on new data.
    """
    logger = logging.getLogger(__name__)
    logger.info('making predictions from trained models')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_fmt='%Y-%m-%d %H:%M:%S'
    logging.basicConfig(level=logging.INFO, format=log_fmt, datefmt=date_fmt)

    load_dotenv(find_dotenv())

    main()
