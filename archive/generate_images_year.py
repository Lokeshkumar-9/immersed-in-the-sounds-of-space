import plotly.express as px
import plotly.io as pio
import pandas as pd


from components.data_engg import load_data_and_clean_data
from components.constants import class_colors

df = load_data_and_clean_data()
min_year = df['year'].min()
max_year = df['year'].max()
# Load your data
# meteorite_data = pd.read_csv('your_data_file.csv')
unique_years = df['year'].unique()
# Loop through each year, generate a plot, and save it
# for year in range(min_year, max_year+1):

# Loop through each year in the desired range, generate a plot, and save it
for year in range(min_year, max_year+1):
# for year in unique_years:
    # Filter the data for the specific year
    yearly_data = df[df['year'] == year]
    
    # Check if there is data for the year
    if not yearly_data.empty:
        # Create a scattergeo plot with data
        fig = px.scatter_geo(yearly_data, 
                             lat='latitude', lon='longitude', 
                             color='class_cat', 
                             size='mass', 
                             projection="natural earth",
                             title=f"Meteorite Landings in {year}",
                             color_discrete_map=class_colors)
        # Adjust legend title and land color
        fig.update_layout(geo=dict(landcolor='white'), legend_title='Class', showlegend=True, legend=dict(x=0.35, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    else:
        # Create a blank scattergeo plot (no data)
        fig = px.scatter_geo(projection="natural earth",
                             title=f"Meteorite Landings in {year}")
        # Adjust land color
        fig.update_layout(geo=dict(landcolor='white'),
                          legend_title='Class',
                          showlegend=True)
    
    # Save the plot as a PNG file
    image_file_path = f'output/images/{year}.png'
    pio.write_image(fig, image_file_path)