import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def create_model():
    data = pd.read_csv("./data/spam_ham_dataset.csv")
    print(data.head())
    print(data)

    #drop the unnecessary column
    cdata = data.drop(['label_num'], axis='columns')
    cdata = cdata.loc[:, ~cdata.columns.str.contains('^Unnamed')]
    print(cdata.head())

    #remove empty data for the better prediction
    cdata = cdata.dropna()
    print(cdata)


def identify_mail(user_input):
    print(str.find(user_input, 'RS'))
    if str.find(user_input, 'RS') >= 0:
        return 'its a SPAM'
    else:
        return 'its a HAM (not SPAM)'