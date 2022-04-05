import moviepy.editor as movie
from urllib.request import urlopen
from os import mkdir
import glob
from .env import *

def download(number):
    if(len(glob.glob("tmp")) == 0):
        mkdir("tmp")
    if(len(glob.glob("tmp/images")) == 0):
        mkdir("tmp/images")
    if len(glob.glob(f"tmp/images/{number}.{extension}")) == 0:
        print("Downloading {}".format(url.format(number)))
        with urlopen(url.format(number)) as r:
            with open(f"tmp/images/{number}.{extension}", "wb") as f:
                f.write(r.read())

class Generator:
    def __init__(self, smash_path, pass_path):
        if(len(glob.glob("tmp")) == 0):
            mkdir("tmp")
        if(len(glob.glob("tmp/images")) == 0):
            mkdir("tmp/clips")
        self.smash_clip = movie.AudioFileClip(smash_path)
        self.pass_clip = movie.AudioFileClip(pass_path)

    def generate(self, number, smash):
        download(number)
        if smash:
            text = movie.TextClip("SMASH", fontsize=70, color='#00ff00').set_pos('center').set_duration(self.smash_clip.duration)
            audio = self.smash_clip
        else:
            text = movie.TextClip("PASS", fontsize=70, color='#ff0000').set_pos('center').set_duration(self.pass_clip.duration)
            audio = self.pass_clip
        image = movie.ImageClip(f"tmp/images/{number}.{extension}", duration=audio.duration)
        clip = movie.CompositeVideoClip([image, text]).set_audio(audio)
        return clip
        # clip.write_videofile(f"tmp/clips/{number}.webm", fps=12)
                
    def close(self):
        self.smash_clip.close()
        self.pass_clip.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()