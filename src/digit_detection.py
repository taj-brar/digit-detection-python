from sklearn.tree import DecisionTreeClassifier
import joblib
import pandas as pd
import os
import csv
import numpy as np
from PIL import Image


# CONSTANTS
TRAIN_FILE = "sample_data/train.csv"
TEST_FILE = "bin/post_image.csv"#"sample_data/test.csv"#
MODEL_FILE = "bin/model.joblib"


def main():
    with open(TEST_FILE) as csv_file:
        csv_reader = csv.reader(csv_file)

        # skip headers
        next(csv_reader)

        for row in csv_reader:
            pixels = np.array(row, dtype='uint8')
            pixels = pixels.reshape((28, 28))
            image = Image.fromarray(pixels)
            image.show()
            break

    model = get_model()
    results = model.predict(get_testing_data())
    print(results)


def get_model():
    if os.path.isfile(MODEL_FILE):
        print("Found existing model.")
        return joblib.load(MODEL_FILE)
    else:
        print("Building new model...")
        return train_model()


def train_model():
    samples, targets = get_training_data()
    model = DecisionTreeClassifier()

    print("Training model...")
    model.fit(samples, targets)
    print("Model trained.")

    joblib.dump(model, MODEL_FILE)
    print("Model saved.")

    return model


def get_training_data():
    print("Fetching training samples and targets...")
    train_df = pd.read_csv(TRAIN_FILE)
    samples = train_df.drop(columns=["label"]).values
    targets = train_df["label"].values
    print("Retrieved training samples and targets.")

    return samples, targets


def get_testing_data():
    print("Fetching testing samples...")
    test_df = pd.read_csv(TEST_FILE)
    print("Retrieved testing samples.")

    return test_df.values


if __name__ == "__main__":
    main()
