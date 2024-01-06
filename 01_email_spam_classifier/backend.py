# Reference
# https://www.youtube.com/watch?v=IBFrrnec1dE&t=1192s

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import pickle, os

def create_model():
    #read dataset
    data = pd.read_csv("./data/spam_ham_dataset.csv")
    # print(data.head())
    # print(data)

    #drop the unnecessary column
    cdata = data.drop(['label_num'], axis='columns')

    #remove column which does not have header
    cdata = cdata.loc[:, ~cdata.columns.str.contains('^Unnamed')]
    #print(cdata.head())

    #remove empty data for the better prediction
    cdata = cdata.dropna()
    #print(cdata)

    #change to numeric format
    cdata.loc[cdata['label'] == 'ham', 'label'] = 0
    cdata.loc[cdata['label'] == 'spam', 'label'] = 1

    print(cdata.info())

    X = cdata['text']
    y = cdata['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

    #remove english general word
    vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
    
    X_train_features = vectorizer.fit_transform(X_train)
    X_test_features = vectorizer.transform(X_test)
    y_train = y_train.astype('int')
    y_test = y_test.astype('int')

    #Use ML algorithm and fit the model
    model = LogisticRegression()
    model.fit(X_train_features, y_train)

    print("Model Score:", model.score(X_test_features, y_test))

    prediction_on_test_data = model.predict(X_test_features)
    accuracy_on_test_data = accuracy_score(y_test, prediction_on_test_data)

    print("Accuracy based on the test data:", accuracy_on_test_data)

    if save_model_vectorizer(model, vectorizer):
        print("Model saved successfully.")
    else:
        print("Error occurred.")

def save_model_vectorizer(model, vectorizer):
    #first delete
    if os.path.exists('model.pkl'):
        os.remove('model.pkl')
    if os.path.exists('vectorizer.pkl'):
        os.remove('vectorizer.pkl')

    #save the model
    pickle.dump(model, open('model.pkl', 'wb'))

    #save the vectorizer
    pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

    if os.path.exists('model.pkl') and os.path.exists('vectorizer.pkl'):
        return True
    else:
        return False

def load_create_model():
    if not os.path.exists('model.pkl') or not os.path.exists('vectorizer.pkl'):
        create_model()    
    model = pickle.load(open('model.pkl', 'rb'))   
    vectorizer  = pickle.load(open('vectorizer.pkl', 'rb'))

    return model, vectorizer
        

def identify_mail_type(user_input):
    model, vectorizer = load_create_model()

    # Transform input using the loaded vectorizer
    user_input_feature = vectorizer.transform([user_input])
    prection = model.predict(user_input_feature)

    if prection == 1:
        return 'its a SPAM'
    else:
        return 'its a HAM (not SPAM)'
    
if __name__ == '__main__':
    #create_model()

    print(identify_mail_type('Please found the address'))