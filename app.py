import tinify
from glob import glob
import os.path
tinify.key = "api_key"
source_dir_name = 'src'
destination_dir_name = 'dist'
# get all files names in directory
files = glob(source_dir_name + '/*')
# compress all files
for file in files:
    print('compressing ' + file)
    source = tinify.from_file(file)
    file_name, ext = os.path.splitext(file)
    file_name = file_name.replace(source_dir_name + '/', '')
    source.to_file(destination_dir_name + "/" + file_name + ".png")
print('compressed all images')