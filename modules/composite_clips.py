import moviepy.editor as movie
from .env import frames_per_clip

def composite(base_clip, new_clip):
    if frames_per_clip == "all":
        new_clip = new_clip.set_start(base_clip.duration)
    else:
        seconds = (int(frames_per_clip) / 12)
        new_clip = new_clip.set_start(base_clip.duration - new_clip.duration + seconds)
    return movie.CompositeVideoClip([base_clip, new_clip])

def recomposite(base_clip, new_clip):
    if frames_per_clip == "all":
        new_clip = new_clip.set_start(base_clip.duration)
    else:
        seconds = (int(frames_per_clip) / 12)
        new_clip = new_clip.set_start(base_clip.duration - new_clip.clips[-1].duration + seconds)
    return movie.CompositeVideoClip([base_clip, new_clip])