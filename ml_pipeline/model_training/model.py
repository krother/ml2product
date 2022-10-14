import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from get_data import load_and_sort_data


def preprocess(df):
    """Sometimes gender contains missing values"""
    return df.dropna()


def get_xy(df):
    """remove both target columns"""
    target = "Claims1"
    X = df.copy()
    # all these columns are probably related to target and not useful
    X.drop(
        [target, "Claims2", "NClaims1", "NClaims2", "PolID", "Types"],
        axis=1,
        inplace=True,
    )
    y = df[target].astype(int)
    return X, y


def train_model(Xtrain, ytrain):
    """Trains a RandomForest model"""
    rf = RandomForestClassifier(n_estimators=10, min_samples_leaf=50)
    rf.fit(Xtrain, ytrain)
    return rf


def evaluate_model(model, X, ytrue):
    predictions = model.predict(X)
    accuracy = accuracy_score(predictions, ytrue)
    return accuracy


if __name__ == "__main__":
    print("--------------- preparing data ---------------")
    df_train, df_test = load_and_sort_data()
    df_train = preprocess(df_train)
    df_test = preprocess(df_test)
    Xtrain, ytrain = get_xy(df_train)
    Xtest, ytest = get_xy(df_test)
    print(Xtrain.shape, ytrain.shape, Xtest.shape, ytest.shape)

    print("--------------- training model ---------------")
    model = train_model(Xtrain, ytrain)
    train_acc = evaluate_model(model, Xtest, ytest)
    test_acc = evaluate_model(model, Xtest, ytest)
    print(f"training accuracy: {train_acc:6.3f}")
    print(f"test accuracy    : {train_acc:6.3f}")

    pickle.dump(model, open("model.pkl", "wb"))
