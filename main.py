import logging
import argparse
from dotenv import find_dotenv, load_dotenv

# from src.data.make_dataset import main as make_dataset
# from src.features.build_features import main as build_features
# from src.models.train_model import main as train_model
# from src.models.predict_model import main as predict_model
# from src.utils.utils import *


def main():
    """ Runs the following script to ...
    """
    logger = logging.getLogger(__name__)
    logger.info('running movie classifier')

    parser = argparse.ArgumentParser()
    parser.add_argument('--myarg', type=str, required=True, help='myarg help')
    args = parser.parse_args()

    logger.info('done')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_fmt = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(level=logging.INFO, format=log_fmt, datefmt=date_fmt)

    load_dotenv(find_dotenv())

    main()
