from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

def create_model(param=""):
    import pandas as pd

    with open(param, 'r', encoding='utf-8') as temp:
        temp2 = temp.readlines()
        list_of_strings_labels = temp2[0].split(',')
        all_items = []
        all_items.append(temp2[0].split(','))
        for item in temp2[1:]:
            all_items.append(item.split(','))

    df = pd.DataFrame(all_items[1:], None, list_of_strings_labels)

    X = df.copy().drop([df], axis=1).values  # X values from with will be predicted data
    y = df.copy().loc[:, df].replace({'setosa': 0, 'versicolor': 1, 'virginica': 2}).values

    from sklearn.model_selection import train_test_split
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, 0.2)

    model = LogisticRegression()
    model.fit(X_tr, y_tr)
    y_pr = model.predict(X_te)

    from sklearn.externals import joblib
    joblib.dump(model, 'models/{'+LogisticRegression+'}.pkl')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model2 = DecisionTreeClassifier()
    model2.fit(X_train, y_train)
    y_pr = model2.predict(X_test)

    joblib.dump(model2, 'models/{}.pkl'.format('DecisionTreeClassifier'))

    return model, model2 



