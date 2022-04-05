import dotenv
from os import getenv

dotenv.load_dotenv()

url = getenv("POKEMON_IMAGE_URL", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{}.png")
extension = url.split(".")[-1]
frames_per_clip = getenv("FRAMES", "3")