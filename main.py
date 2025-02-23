import pandas as pd
import matplotlib.pyplot as plt

depressionData = pd.read_csv(filepath_or_buffer='StudentDepressionData.csv', index_col = 0, parse_dates = True)

print(depressionData.head())