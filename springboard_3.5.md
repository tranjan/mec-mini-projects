## Three datasets

Per the instructions of section 3.5, I have found the following
three datasets that I think I would like to work with. All
three of them are hosted on [kaggle.com](https://kaggle.com).

#### [Uber Fares Dataset](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)

This is a dataset comprised of 200,000 Uber rides in New York City 
over a 6.5 year period starting in January 2009. It is a single
CSV file consisting of the following columns:
- Fare amount in dollars
- Pickup date and time
- Pickup latitude
- Pickup longitude
- Dropoff latitude
- Dropoff longitude
- Number of passengers

#### [Flickr30k](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset)

This is a dataset of over 30,000 images from Flickr, each of which
is accompanied by 5 captions. The dataset is 9 GB overall, consisting
of a single directory that contains all images and a single CSV file
consisting of all the captions.

#### [NIH Chest X-Rays](https://www.kaggle.com/datasets/nih-chest-xrays/data)

This is a labeled dataset of 112,120 chest X-rays from 30,805 unique patients.
There is also an accompanying CSV which lists the following for each X-ray:
- Findings, which can either have a value of "No Finding" or a "|"-separated
  list of at least one of the following:
  - Atelectasis
  - Cardiomegaly
  - Consolidation
  - Edema
  - Effusion
  - Emphysema
  - Fibrosis
  - Hernia
  - Infiltration
  - Mass
  - Nodule
  - Pleural_Thickening
  - Pneumonia
  - Pneumothorax
- Patient Age
- Patient Gender
- View Position

## Chosen Dataset

I'd like to work with the Flickr30k dataset. It would provide 
a good opportunity to train an image-captioning model.