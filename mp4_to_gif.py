import os
import imageio
from PIL import Image
import numpy as np

def convert_to_gif(input_folder, output_folder, size):
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            mp4_file = os.path.join(input_folder, filename)
            gif_file = os.path.join(output_folder, filename[:-4] + ".gif")
            with imageio.get_writer(gif_file, mode='I') as writer:
                reader = imageio.get_reader(mp4_file)
                for frames in reader:
                    resized_frame = Image.fromarray(frames).resize(size)
                    writer.append_data(np.array(resized_frame))
            print("Converted " + mp4_file + " to " + gif_file)
        else:
            print(filename + " is not a .mp4 file.")
    print("done")


## 직접입력
#width = int(input("Enter the width of the output gif (in pixels): "))
#height = int(input("Enter the height of the output gif (in pixels): "))

## 이모지용
width,height = 100,100

input_folder = "D:/Users/"
output_folder = "D:/Users/"
#input_folder = input("Enter the path of the input folder: ")
#output_folder = input("Enter the path of the output folder: ")
convert_to_gif(input_folder, output_folder, (width, height))