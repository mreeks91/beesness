from fastai.vision.all import *
from PIL import Image
from pathlib import Path
#from settings import INFERENCE_DIRECTORY

#input: path to raw jpeg image (unrestricted size)
#output: 400x400 jpg to be passed into model
def input_processing(filename):
    path = Path(INFERENCE_DIRECTORY+'/'+filename)
    image = Image.open(img)
    image.resize((400,400))
    image.save(path)

#input: processed jpg img
#output: class prediction and vector of probabilities from clade_classifier
def clade_probabilities(img):
    learn = load_learner('bee34')
    pred,idx,probs = learn.predict(img)
    return pred,probs

#input: vector of clade probabilities
#output: broad class (friend bee, friend wasp, spicy) and proposed specific class (clade) with probability
def inference(probs):
    pass

#input: broad and specific class
#output: formatted response for reddit post with prediction and advocacy info
def output_text(preds):
    pass


