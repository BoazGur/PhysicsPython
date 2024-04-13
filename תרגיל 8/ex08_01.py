import pandas as pd

def cars_per_seller():
    df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    print(df.groupby('Make').count()['VIN (1-10)'])

def best_seller():
    df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    df = df.groupby('Make')['VIN (1-10)'].count()
    print(df[df == df.max()])

if __name__ == '__main__':
    cars_per_seller()
    best_seller()