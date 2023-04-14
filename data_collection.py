import urllib.request
from PIL import Image
from settings import TSV_DIRECTORY, IMAGE_DIRECTORY, CLASSES
import os
import pandas as pd

def image_urls_from_file(relpath,file_type = 'txt', sample_proportion = .05):
    if file_type == 'tsv' or file_type == 'txt':
        df = pd.read_table(TSV_DIRECTORY+'/'+relpath+'.'+file_type)
    elif file_type == 'csv':
        df = pd.read_csv(TSV_DIRECTORY+'/'+relpath+'.'+file_type)
    df.dropna(subset = ['identifier'],inplace = True)
    data_sample = df.sample(round(df.shape[0]*sample_proportion))
    return data_sample[['gbifID','identifier']]

def download_images(url_df,class_name,image_size=(400,400)):
    path = IMAGE_DIRECTORY + '/' + class_name
    if not os.path.exists(path):
        os.makedirs(path)
    for url in url_df.iterrows():
        filename = class_name+str(url[1][0])+'.jpg'
        fullpath = path+'/'+filename
        try:
            urllib.request.urlretrieve(str(url[1][1]), filename=fullpath)
        except (urllib.error.HTTPError,urllib.error.URLError,TypeError):
            pass
        try:
            im = Image.open(fullpath)
            im = im.thumbnail(image_size)
            im = im.save(fullpath)
        except (AttributeError,FileNotFoundError):
            pass

def compress_images(class_name,compressRatio = 10):
    source_path = IMAGE_DIRECTORY + '/' + class_name
    save_path = source_path + '_compressed'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for filename in os.listdir(source_path):
        im = Image.open(source_path+'/'+filename)
        try:
            im.save(save_path+'/'+filename,
                    'JPEG',
                    optimize = True,
                    quality = 10)
        except OSError:
            pass


if __name__ == "__main__":
    classes = ['sphecidae','vespa','vespula','xylocopa']
    for cls in classes:
        #sample = image_urls_from_file(cls)
        #download_images(sample,cls)
        print(f"Compressing {cls} images...")
        compress_images(cls)