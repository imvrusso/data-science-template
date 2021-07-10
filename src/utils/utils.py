import os
import joblib

import numpy as np
import pandas as pd
import scipy.sparse


def read_csv(dataset: str, subfolder: str):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'data', subfolder, dataset))
    return pd.read_csv(path, low_memory=False)


def write_csv(dataset: pd.DataFrame, name: str, subfolder: str):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'data', subfolder, name))
    dataset.to_csv(path, index=False)


def read_array(array: str, subfolder: str):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'data', subfolder, array))
    return np.load(path)


def write_array(array: np.array, name: str, subfolder: str):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'data', subfolder, name))
    np.save(path, array)


def read_matrix(matrix: str, subfolder: str):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'data', subfolder, matrix))
    return scipy.sparse.load_npz(path)


def write_matrix(matrix: scipy.sparse.csr_matrix, name: str, subfolder: str):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'data', subfolder, name))
    scipy.sparse.save_npz(path, matrix)


def read_model(model: str):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'models', model))
    return joblib.load(path)


def write_model(model: dict, name: str):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'models', name))
    joblib.dump(model, path)


def file_exists(name: str, folder: str, subfolder: str = None):
    path = os.path.abspath(os.path.join(__file__, "../../..", folder, subfolder, name)) if subfolder \
            else os.path.abspath(os.path.join(__file__, "../../..", folder, name))
    return os.path.isfile(path)
