from modules.composite_clips import composite, recomposite
from modules.generate_clip import Generator 
from json import load

with Generator("smash.mp3", "pass.mp3") as generator:
    with open("input.json", "r") as f:
        j = load(f)
        last_clip = False
        clips = []
        for k in j["choices"]:
            clip = generator.generate(int(k), j["choices"][k] == "smash")
            if last_clip:
                clip = composite(last_clip, clip)
            last_clip = clip
            if (int(k) % 25) == 0:
                clips.append(last_clip)
                last_clip = False
        clips.append(last_clip)

        last_clip = False
        for clip in clips:
            if last_clip:
                clip = recomposite(last_clip, clip)
            last_clip = clip
        last_clip.write_videofile(f"out.mp4", fps=12)