import requests
import pandas as pd

if __name__ == '__main__':

    print('Start')

    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=20c737f1a0042f2e9df4d1e8e3e7b315')
    print(response)

    df = pd.json_normalize(response.json())
    print(df.head())