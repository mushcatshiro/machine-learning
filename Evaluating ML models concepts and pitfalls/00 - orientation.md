[TOC]

# Orientation

"online evaluation" live metrics of the deployed model on live data

"offline evaluation" prototyped model on historical data

note that online and offline metrics could be different, offline we might be interested in accuracy or precision but on online metrics we usually care more about business metrics. a problem to think about is are our distribution of data / search space is always stationary? its normal to see a distribution drift hence we will want to detect drift and adapt accordingly.

## a few example categories of evaluation metrics

- classification problem
- regression problem
- ranking problem (precision-recall or normalized discounted cumulative gain)

## offline metrics

we prefer to evaluate on data that the model haven't seen, this gives generalization error statistically by having hold out sets of data. there are more options available eg. bootstrapping, jackknife resampling.

## hyperparameter search

hyperparameter search, grid search and etc. a general advice is to not rely on grid search, especially in deep learning, because some parameter might be more significant than others. we should do a coarse search then lock in to those area that model performs well. another consideration is also resource, can we train more models / parameter set or we could only afford to only do a few and go further.

## online testing mechanism

eg. A / B testing and multiarmed bandits. challenges and opportunity