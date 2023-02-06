import os
import imageio
from scipy.misc import imresize

def resize_frame(frame, size):
    return imresize(frame, size)

def convert_to_gif(input_folder, output_folder, size):
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            mp4_file = os.path.join(input_folder, filename)
            gif_file = os.path.join(output_folder, filename[:-4] + ".gif")
            with imageio.get_writer(gif_file, mode='I') as writer:
                reader = imageio.get_reader(mp4_file)
                for frames in reader:
                    resized_frame = resize_frame(frames, size)
                    writer.append_data(resized_frame)
                    writer.append_data(frames)
            print("Converted " + mp4_file + " to " + gif_file)
        else:
            print(filename + " is not a .mp4 file.")
    print("done")

#input_folder = input("Enter the path of the input folder: ")
#output_folder = input("Enter the path of the output folder: ")
#width = int(input("Enter the width of the output gif (in pixels): "))
#height = int(input("Enter the height of the output gif (in pixels): "))
input_folder = "D:/Users/sagvd17/mp4_to_gif/input_mp4"
output_folder = "D:/Users/sagvd17/mp4_to_gif/output_gif"
width = 100
height = 100
convert_to_gif(input_folder, output_folder, (width, height))