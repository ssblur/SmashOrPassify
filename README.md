A basic script for turning https://pokesmash.xyz/ results into a video.

# Setup

## Prerequisites
Requires you have ImageMagick, FFMPEG, and all Python modules from requirements.txt installed.

## .env
After setting up your files, copy .env.default to .env and change any options needed. 

### POKEMON_IMAGE_URL
This is a string representing a URL to download Pokemon images from. {} will be replaced with the National Dex number of the Pokemon.

### FRAMES
This is either the string "all", which lets clips play out in full before the next starts, or a number of frames the next clip should be shifted forwards. Exports are in 12 FPS.

## Audio
Requires an audio clip named smash.mp3 to play for smashes and pass.mp3 to play for passes.

## input.json
This is a file containing the JSON for localStorage.offlineScore from PokeSmash. The only property this presently requires is "choices", which is an object with strings as keys, and the string "smash" or the string "pass" as values.

All key strings must resolve when substituted into POKEMON_IMAGE_URL. By default, this means integer strings within [1, 899].

# Usage
Run `python .` to automatically download all Pokemon images and generate a video from these images and input.json. The result will be written to out.mp4.