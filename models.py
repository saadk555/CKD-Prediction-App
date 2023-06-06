import re
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def read_csv_file(file_path):
    return pd.read_csv(file_path)


def drop_rows(df, rows):
    df.drop(rows, axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def set_display_options():
    pd.set_option("display.max_columns", None)


def map_column_values(df, column, value_mapping):
    df[column] = df[column].map(value_mapping)
    return df


def preprocess_dataframe(df):
    regexp = re.compile(r"≥|≤")
    df = df.applymap(lambda x: str(x).replace(" ", "") if " " in str(x) else x)
    df = df.applymap(
        lambda x: (float(str(x).split("-")[0]) + float(str(x).split("-")[1])) / 2
        if "-" in str(x)
        else x
    )
    df = df.applymap(
        lambda x: float(x[1:]) - 1
        if "<" in str(x)
        else (
            str(x).replace("≥", "").replace("≤", "")
            if regexp.search(str(x))
            else (float(x[1:]) + 1 if ">" in str(x) else x)
        )
    )
    df.at[179, "grf"] = 200
    df = df.apply(pd.to_numeric)
    return df


def split_data(df, target_column, test_size, random_state):
    X = np.asarray(df.drop([target_column], axis=1))
    y = np.asarray(df[target_column])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def create_linear_svc_classifier():
    return SVC(kernel="linear", random_state=0)


def create_random_forest_classifier(n_estimators):
    return RandomForestClassifier(n_estimators=n_estimators)


def create_decision_tree_classifier(criterion):
    return DecisionTreeClassifier(criterion=criterion, random_state=0)


def train_classifier(classifier, X_train, y_train):
    classifier.fit(X_train, y_train)
    return classifier


# Read the CSV file
df = read_csv_file("./ckd-dataset-v2.csv")

# Drop rows 0 and 1
df = drop_rows(df, [0, 1])

# Set display options
set_display_options()

# Map "class" column values to 1 and 0
df = map_column_values(df, "class", {"ckd": 1, "notckd": 0})

# Map "stage" column values
df = map_column_values(df, "stage", {"s1": 1, "s2": 2, "s3": 3, "s4": 4, "s5": 5})

# Preprocess dataframe values
df = preprocess_dataframe(df)

# Split data into train and test sets
X_train, X_test, y_train, y_test = split_data(
    df, "class", test_size=0.25, random_state=0
)

# Create classifiers
support_vector_classifier = create_linear_svc_classifier()
random_forest_classifier = create_random_forest_classifier(n_estimators=20)
decision_tree_classifier = create_decision_tree_classifier(criterion="gini")

# Fit the classifiers to the training data
support_vector_classifier = train_classifier(
    support_vector_classifier, X_train, y_train
)
random_forest_classifier = train_classifier(random_forest_classifier, X_train, y_train)
decision_tree_classifier = train_classifier(decision_tree_classifier, X_train, y_train)
