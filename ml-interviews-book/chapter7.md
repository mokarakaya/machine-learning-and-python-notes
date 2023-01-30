# 7 Machine Learning Workflows
# 7.1 Basics

- Explain supervised, unsupervised, weakly supervised, semi-supervised, and active learning.
  - **Semi-supervised:** We have a small amount of labeled data and a large amount of unlabelled 
  data. We train a classifier with the labeled data, predict the labels of unlabelled data
  and finally join two datasets and train a model again.
  - **Weakly supervised:** Rule based classifiers defines some rules for classification.
  weakly supervised methods trains a classifier by the using data which is labeled by
  a rule based classifier.
  - **Active Learning:** Active learning is the name used for the process of 
  prioritising the data which needs to be labelled in order to have the 
  highest impact to training a supervised model. E.g. Label a very small amount of data,
  train a classifier, predict the rest of the data and choose items with
  least confidence predictions.