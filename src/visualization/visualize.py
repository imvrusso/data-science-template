import os
import logging
from dotenv import find_dotenv, load_dotenv


def main():
    """ Runs data visualization scripts to create exploratory and
        results oriented visualizations (saved in ../figures).
    """
    logger = logging.getLogger(__name__)
    logger.info('creating visualizations')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_fmt='%Y-%m-%d %H:%M:%S'
    logging.basicConfig(level=logging.INFO, format=log_fmt, datefmt=date_fmt)

    load_dotenv(find_dotenv())

    main()
