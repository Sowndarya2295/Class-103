import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv(r"data.csv")
fig = px.bar(df, x='Country', y='InternetUsers')
fig.show()