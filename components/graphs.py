import plotly.express as px


def plot_geo_with_size(df):
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', size='mass' ,color='class', color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.update_layout(showlegend=True)
    return fig

# add a slider to the plot connecting to year with animation and year ascending

import numpy as np

def plot_geo_with_size_and_year(df):
    df = df.sort_values(by='year', ascending=True)

    fig = px.scatter_geo(df, lat='latitude', lon='longitude', size=np.log(df['mass']), color='class', animation_frame='year', color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.update_layout(showlegend=True, legend=dict(x=0.5, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    return fig

def plot_geo_with_size_and_year_log(df):
    fig = px.scatter(df, x='year', y='mass', log_y=True)
    return fig