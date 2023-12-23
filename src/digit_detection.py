from sklearn.tree import DecisionTreeClassifier
import pandas as pd


# CONSTANTS
TRAIN_FILE = "sample_data/train.csv"
TEST_FILE = "sample_data/test.csv"


def main():
    model = train_model()
    results = model.predict([get_testing_data()])
    print(results)


def train_model():
    samples, targets = get_training_data()
    model = DecisionTreeClassifier()

    print("Training model...")
    model.fit(samples, targets)
    print("Model trained.\n")

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

    return test_df.values[0]


if __name__ == "__main__":
    main()