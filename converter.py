import concurrent
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

from moviepy.editor import *


def convert_mp4_folder_to_mp3(mp4folder, mp3folder):
    with concurrent.futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        for root, dirs, files in os.walk(mp4folder):
            for file in files:
                executor.submit(convert_mp4_file_to_mp3, file, mp4folder, mp3folder)


def convert_mp4_file_to_mp3(file, mp4folder, mp3folder):
    VideoFileClip(os.path.join(mp4folder, file)).audio.write_audiofile(os.path.join(mp3folder, file[:-4] + ".mp3"))


convert_mp4_folder_to_mp3(sys.argv[1], sys.argv[2])
