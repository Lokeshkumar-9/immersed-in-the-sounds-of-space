import plotly.io as pio
# import plotly.express as px
# import numpy as np

# from components.constants import class_colors
# from components.data_engg import load_data_and_clean_data

# df = load_data_and_clean_data()

# # Create the plot
# fig = px.scatter_geo(df, lat='latitude', lon='longitude', size=np.log(df['mass']), color='class_cat', projection='natural earth', animation_frame='year', color_discrete_map=class_colors, custom_data=['mass', 'year', 'name'])
# fig.update_traces(hovertemplate='<br>'.join(['Mass: %{customdata[0]} kg', 'Year: %{customdata[1]}', 'Name: %{customdata[2]}']))
# fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0.35, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))

# # Write the HTML file
# pio.write_html(fig, file='animation.html', auto_play=False)

# # Write the video file
# pio.write_video(fig, file='animation.mp4')

# import plotly.io as pio
# import plotly.express as px
# import numpy as np
# import imageio
# import imageio_ffmpeg

# from components.constants import class_colors
# from components.data_engg import load_data_and_clean_data

# df = load_data_and_clean_data()

# # Create the plot
# fig = px.scatter_geo(df, lat='latitude', lon='longitude', size=np.log(df['mass']), color='class_cat', projection='natural earth', animation_frame='year', color_discrete_map=class_colors, custom_data=['mass', 'year', 'name'])
# fig.update_traces(hovertemplate='<br>'.join(['Mass: %{customdata[0]} kg', 'Year: %{customdata[1]}', 'Name: %{customdata[2]}']))
# fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0.35, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))

# # Write the HTML file
# pio.write_html(fig, file='animation.html', auto_play=False)

# # Write the PNG images
# with imageio.get_writer('animation.mp4', fps=10) as writer:
#     for i in range(fig.frames[0].data[0].size):
#         fig.frames[0].data[0].update(visible=True, frame=i)
#         writer.append_data(np.array(pio.to_image(fig, format='png')))

# # Convert the PNG images to an MP4 video file
# imageio_ffmpeg.ffmpeg_write_images('animation.mp4', 'animation.mp4', fps=10)

import plotly.express as px
import numpy as np
import imageio
import imageio_ffmpeg

from components.constants import class_colors
from components.data_engg import load_data_and_clean_data

df = load_data_and_clean_data()

# Create the plot
fig = px.scatter_geo(df, lat='latitude', lon='longitude', size_max=np.log(df['mass']), color='class_cat', projection='natural earth', animation_frame='year', color_discrete_map=class_colors, custom_data=['mass', 'year', 'name'])
fig.update_traces(hovertemplate='<br>'.join(['Mass: %{customdata[0]} kg', 'Year: %{customdata[1]}', 'Name: %{customdata[2]}']))
fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0.35, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))

# Write the HTML file
pio.write_html(fig, file='animation.html', auto_play=False)

# Write the PNG images
with imageio.get_writer('animation.mp4', fps=10) as writer:
    for i in range(fig.frames[0].data[0].size):
        fig.frames[0].data[0].update(visible=True, frame=i)
        writer.append_data(np.array(pio.to_image(fig, format='png')))

# Convert the PNG images to an MP4 video file
imageio_ffmpeg.ffmpeg_write_images('animation.mp4', 'animation.mp4', fps=10)