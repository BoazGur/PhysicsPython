import pandas as pd

df = pd.read_csv('Electric_Vehicle_Population_Data.csv')

print('Minimum', df['Electric Range'].min())
print('Maximum', df['Electric Range'].max())
print('Average', df['Electric Range'].mean())
print('Median', df['Electric Range'].median())

# Minimum 0.0
# Maximum 337.0
# Average 60.14800152133324
# Median 0.0

print('-' * 30)
print('Minimum', df[df['Electric Range'] > 0]['Electric Range'].min())
print('Maximum', df[df['Electric Range'] > 0]['Electric Range'].max())
print('Average', df[df['Electric Range'] > 0]['Electric Range'].mean())
print('Median', df[df['Electric Range'] > 0]['Electric Range'].median())

# Minimum 6.0
# Maximum 337.0
# Average 122.4639563533967
# Median 84.0

print('-' * 30)
print(df.groupby('Make')['Electric Range'].mean())

df = df.groupby('Make')[['Make' ,'Electric Range']].mean()

print('-' * 30)
print(df[df["Electric Range"] == df["Electric Range"].max()])

#JAGUAR      204.105727