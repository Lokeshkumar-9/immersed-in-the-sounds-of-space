import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np


from components.data_engg import load_data_and_clean_data
from components.constants import class_colors

df = load_data_and_clean_data()
# Load your data
# meteorite_data = pd.read_csv('your_data_file.csv')

# Sort the data by year to ensure plots are generated in chronological order
meteorite_data_sorted = df.sort_values(by='year')

# Initialize a counter for the image file names
counter = 0

# Loop through each row (meteorite landing) in the sorted data
for _, row in meteorite_data_sorted.iterrows():
    # Filter the data to include all meteorites up to and including the current one
    # cumulative_data = meteorite_data_sorted.loc[:row.name]
    print(meteorite_data_sorted.dtypes)
    # Create a scattergeo plot with cumulative data
    fig = px.scatter_geo(pd.DataFrame([row]), 
                         lat='latitude', lon='longitude', 
                         color='class_cat', 
                         size='mass', 
                         projection="natural earth",
                         title=f"Meteorite Landings in {int(row['year'])}",
                         color_discrete_map=class_colors)
    
    # Adjust legend title, land color, and legend position
    fig.update_layout(geo=dict(landcolor='white'))
    fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0.35, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    
    # Save the plot as a PNG file
    image_file_path = f'output/images_occur/frame_{counter:04d}.png'
    pio.write_image(fig, image_file_path)
    
    # Increment the counter
    counter += 1
