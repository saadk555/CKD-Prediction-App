import joblib

# Load the saved models
svc_model = joblib.load("./models/support_vector_classifier.pkl")
random_forest_model = joblib.load("./models/random_forest_classifier.pkl")
decision_tree_model = joblib.load("./models/decision_tree_classifier.pkl")