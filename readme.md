# Mind Your Beesness

## Machine learning for bee and wasp conservation


*Mind Your Beesness* is a reddit bot that uses machine learning to identify and label images of common North American bees and wasps posted to /r/whatisthisbug (a board for requesting information about user-generated images of arthropods). 


Images of bee and wasp observations posted to [iNaturalist](https://www.inaturalist.org/) (and labeled by iNaturalist users) were collected from the Global Biodiversity Information Facility ([GBIF](https://www.gbif.org/)). These formed the training data for a convolutional neural network based on the ResNet architecture. The training and model evaluation made use of the FastAI library.
