import pandas as pd
import csv

df = pd.read_csv("bright_star.csv")

print(df.shape)

df = df[df['Mass'].notna()]

df = df[df['Radius'].notna()]

del df["Luminosity"]
del df["Num"]

df.to_csv('bright_star2.0.csv')


print(df.shape)