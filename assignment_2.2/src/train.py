import pickle
import os


def train_model_imputer(imputer, housing_num):
    os.makedirs("models", exist_ok=True)
    imputer.fit(housing_num)
    X = imputer.transform(housing_num)
    pickle.dump(X, open("models/imputer.sav", "wb"))
