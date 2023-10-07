import plotly.express as px


def plot_geo_with_size(df):
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', size='mass' ,color='class_cat', color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.update_layout(showlegend=True, legend_title='Class', legend=dict(x=0.1, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    return fig

# add a slider to the plot connecting to year with animation and year ascending

import numpy as np

def plot_geo_with_size_and_year(df):
    df = df.sort_values(by='year', ascending=True)

    fig = px.scatter_geo(df, lat='latitude', lon='longitude', size=np.log(df['mass']), color='class_cat', animation_frame='year', color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0.5, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    return fig

def plot_geo_with_size_and_year_log(df):
    fig = px.scatter(df, x='year', y='mass', color='class_cat', log_y=True)
    fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0.1, y=-0.2, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    return fig