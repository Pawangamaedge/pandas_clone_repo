import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

print(poke.tail(5))

# print(poke.tail(5))
# print(poke.describe())
# print(poke.info())
numeric_data = ['int64']
cateogric_data = ['object']
numeric_columns = poke.select_dtypes(include=numeric_data)
categoric_columns = poke.select_dtypes(include=cateogric_data)
# print(numeric_columns)
# print(numeric_columns.shape)
print(categoric_columns)
print(categoric_columns.shape)