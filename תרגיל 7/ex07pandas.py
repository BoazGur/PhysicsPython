import pandas as pd

def calc(data, key1, key2):
    df = pd.DataFrame(data)
    
    return df[df[key1] > df[key1].mean()][key2].max()

if __name__ == '__main__':
    data = [{ 'A': 20, 'B': 30.5}, { 'A': 15, 'B': 140}, { 'A': 24, 'B': 26.25}]
    print(calc(data, 'A', 'B'))