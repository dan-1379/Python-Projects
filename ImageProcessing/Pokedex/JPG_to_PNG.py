import sys
import os
from PIL import Image

# GRAB THE FIRST AND LAST ARGUMENT
path = sys.argv[1]
directory = sys.argv[2]

# CHECK IF NEW/ EXISTS, IF NOT CREATE IT
if not os.path.exists(directory):
    os.makedirs(directory)

# LOOP THROUGH POKEDEX, CONVERT IMAGES TO PNG
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')

# SAVE TO THE NEW FOLDER
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
