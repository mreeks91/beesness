# Mind Your Beesness

## Machine learning for bee and wasp conservation


*Mind Your Beesness* is a WIP reddit bot that uses machine learning to identify and label images of common North American bees and wasps posted to /r/whatisthisbug (a board for requesting information about user-generated images of arthropods). 


Images of bee and wasp observations posted to [iNaturalist](https://www.inaturalist.org/) (and labeled by iNaturalist users) were collected from the Global Biodiversity Information Facility ([GBIF](https://www.gbif.org/)). These formed the training data for a convolutional neural network based on the ResNet architecture. The training and model evaluation made use of the FastAI library.

This repository contains code for downloading and cleaning GBIF data (```data_collection.py```) and training two models:

* ```bee_or_wasp.ipynb``` is a rudimentary model for deciding whether an image contains a bee, a wasp, or another type of bug entirely. This model formed a baseline for comparison for the final model (which seeks to be more specific about the type of bee or wasp in the image).
* ```clade_classifier_training.ipynb``` contains code to train a 9-class classifier, classifying images of bees, wasps, and other insects into biological clades (at the genus level or higher). This model achieved 67% accuracy on the training data.

Future updates will include a reddit bot that implements the clade_classifier to respond to bug ID posts, as well as refinements to the classifier.