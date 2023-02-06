#아카콘 변환
import os
import imageio

def convert_to_gif(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            mp4_file = os.path.join(input_folder, filename)
            gif_file = os.path.join(output_folder, filename[:-4] + ".gif")
            with imageio.get_writer(gif_file, mode='I') as writer:
                reader = imageio.get_reader(mp4_file)
                for frames in reader:
                    writer.append_data(frames)
            print("Converted " + mp4_file + " to " + gif_file)
        else:
            print(filename + " is not a .mp4 file.")

#input_folder = input("Enter the path of the input folder: ")
input_folder = "D:/Users/sagvd17/mp4_to_gif/input_mp4"
output_folder = "D:/Users/sagvd17/mp4_to_gif/input_mp4"
#output_folder = input("Enter the path of the output folder: ")
convert_to_gif(input_folder, output_folder)