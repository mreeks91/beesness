import os
import shutil
import random

PATH = 'E:/Bees/compressed_images'
TRAIN_PATH = 'E:/Bees/compressed_images'
TEST_PATH = 'E:/Bees/train'
TEST_RATIO = 0.2 

for path in [TRAIN_PATH,TEST_PATH]:
    if not os.path.exists(path):
        os.makedirs(path)

images = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(PATH)) for f in fn]
n_images = len(images)
print(n_images)
for image in random.sample(images, round(n_images*TEST_RATIO)):
    shutil.move(os.path.join(TRAIN_PATH,image), TEST_PATH)







