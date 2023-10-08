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

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Assume meteorite_data_sorted is your DataFrame sorted by 'year'

# Define the minimum and maximum marker sizes you want in your plot
min_marker_size = 10
max_marker_size = 100

# Calculate the logarithm of the mass for the entire dataset
meteorite_data_sorted['log_mass'] = np.log(meteorite_data_sorted['mass'] + 1)  # Adding 1 to avoid log(0)

# Normalize the logarithm of the mass across the entire dataset to your desired range
meteorite_data_sorted['normalized_log_mass'] = (
    (meteorite_data_sorted['log_mass'] - meteorite_data_sorted['log_mass'].min()) /
    (meteorite_data_sorted['log_mass'].max() - meteorite_data_sorted['log_mass'].min())
) * (max_marker_size - min_marker_size) + min_marker_size

# Initialize a counter for the image file names
counter = 0
print(meteorite_data_sorted)
# Loop through each row (meteorite landing) in the sorted data
for _, row in meteorite_data_sorted.iterrows():
    
    # Creating a single-row DataFrame for the current meteorite
    single_row_df = pd.DataFrame([row])
    
    # Create a scattergeo plot with data only for the current meteorite
    fig = px.scatter_geo(single_row_df, 
                         lat='latitude', lon='longitude', 
                         color='class_cat', 
                         size='normalized_log_mass',  # Using the normalized logarithm of mass for size
                         projection="natural earth",
                         title=f"Meteorite Landing in {int(row['year'])}",
                         color_discrete_map=class_colors)
    
    # Adjust legend title, land color, and legend position
    fig.update_layout(geo=dict(landcolor='white'))
    fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0.35, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    
    # Save the plot as a PNG file
    image_file_path = f'output/images/frame_{counter:04d}.png'
    pio.write_image(fig, image_file_path)
    
    # Increment the counter
    counter += 1

