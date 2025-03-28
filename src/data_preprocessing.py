import pandas as pd 

def load_data(filepath):
    'Loads dataset from csv file'
    return pd.read_csv(filepath)

#df= load_data(r'C:\Users\Hi\Customer-Churn-Prediction\datasets\churn-bigml-20.csv')
# print(df.head(5))
def clean_data(df):
    'Handling missing values'
    df=df.dropna()
    return df
# clean_data(df)