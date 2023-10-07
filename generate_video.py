import imageio

# Specify the path to save the video and the image frames path
video_file_path = 'output/video.mp4'
image_frames_path = 'output/images_occur/frame_{:04d}.png'

# Create a writer object
writer = imageio.get_writer(video_file_path, fps=5)

# Loop through the image frames and add them to the video
for i in range(0, 500):
    image_file_path = image_frames_path.format(i)
    writer.append_data(imageio.imread(image_file_path))

# Close the writer to save the video
writer.close()


# ffmpeg -r 10 -i path_to_save_images/frame_%04d.png -c:v libx264 -vf "fps=10,format=yuv420p" path_to_save_video/video.mp4
