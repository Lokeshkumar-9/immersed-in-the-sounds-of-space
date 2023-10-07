# %%
import pandas as pd

def load_data_and_clean_data():
# Load Data
    df = pd.read_csv('data/Meteorite_Landings.csv')

    # Drop null values
    df = df.dropna()

    # Drop irrelevant columns
    df = df.drop(['nametype', 'GeoLocation'], axis=1)

    # Rename columns
    df = df.rename(columns={'mass (g)': 'mass', 'recclass':'class', 'reclat': 'latitude', 'reclong': 'longitude'})

    # Convert data types
    df['year'] = df['year'].astype(int)
    df['mass'] = df['mass'].astype(int)

    # Convert mass from grams to kilograms
    df['mass'] = df['mass'] / 1000

    # Sort by mass descending
    df = df.sort_values(by='mass', ascending=False)

    # Choose top 500 values
    df = df.iloc[:500]

    return df
# print(df.columns)
# print(df.head())
# print(len(df))
# print(df.dtypes)
# print(df.describe())
# %%
