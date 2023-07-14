import pickle


def train_model_imputer(imputer, housing_num):
    imputer.fit(housing_num)
    X = imputer.transform(housing_num)
    pickle.dump(X, open("models/imputer.sav", "wb"))
