import os

from six.moves import urllib
import tarfile
import pandas as pd
from sklearn.model_selection import train_test_split

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url, housing_path):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    fetch_housing_data(HOUSING_URL, housing_path)
    csv_path = os.path.join(housing_path, "housing.csv")
    housing = pd.read_csv(csv_path)
    train_test = train_test_split(housing, test_size=0.2, random_state=42)

    return housing, train_test[0], train_test[1]


def train_test_after_income_cat(housing):
    train_test = train_test_split(housing, test_size=0.2, random_state=42)

    return train_test[0], train_test[1]


# housing = load_housing_data(HOUSING_PATH)
