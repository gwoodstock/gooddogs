import numpy as np
from sklearn.preprocessing import OneHotEncoder


def predict_dog(input_features, trained_classifer, transformer):
    """
    predict doggo adoption

    :param input_features: 2D numpy array containing dog age (as class, not numeric), breed, and condition. Formatted in .lower()
    :param trained_classifer: sklearn estimator class
    :param transformer: sklearn one hote encoder transformer
    :return: numpy array of model prediction as float

    example input: np.array([['senior', 'dachshund', 'aged'], ['adult', 'dachshund', 'normal'], ['baby', 'dachshund', 'injured']])
    """

    def encode(inputs, transformer):
        """
        Transform list of raw categorical inputs into sparse matrix for modeling.
        :param inputs: ordered list containing dog age (as class, not numeric), breed, and condition
        :param transformer: sklearn one hote encoder transformer
        :return: sparse matrix of model's inputs for prediction
        """
        return transformer.transform(np.array(inputs).reshape(1, -1))

    data = encode(inputs=input_features, transformer=transformer)
    prediction = trained_classifer.predict_proba(data)

    return prediction[:,1]

