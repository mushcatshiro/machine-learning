[TOC]

# Evaluation metrics

the common tasks

- classification
- regression
- ranking
- clustering
- topic modelling and etc

some metrics can be good for multiple tasks. this chapter only discuss on supervised learning metrics.

## classification metrics

we got binary classification, multilabel classification and multiclass classification.

### accuracy

a simple measurement of how the classifier correctly classifies a sample.
$$
accuracy = \frac{no.\,of\,correct\,predictions} {total\,data\,points}
$$

### confusion matrix

accuracy is simple but it makes no distinction between classes. we might be interested on false-positives and false negatives. confusion matrix allows to to breakdown further. 
$$
confussion\,matix = \begin{bmatrix}
TP & FP\\
TN & FN
\end{bmatrix}
$$

### average per class accuracy

this is a variation of accuracy, its knows as a macro average (contrast to accuracy as micro average).??
$$
if: positive\,accuracy = TP + T,\\
    negative\,accuracy = TN + N\\
average\,per\,class\,accuracy = (pa + na) /2
$$
when there is different number of examples per class the average per class accuracy will be different from the accuracy. when per class accuracy is used in a imbalance between classes, if we are using average per class accuracy the class with more example will dominate the statistic thus its better to look at both per class accuracy and average per class accuracy. but there is a caveat using per class accuracy, test statistics for class with very few examples will have large variance and thus the accuracy estimate will be not reliable resulting the confidence interval to be large.

### log loss

log loss gets into finer detail of a classifier and its usually use when the output is a numeric probability instead of class label 0 or 1. this probability is used as a confidence instead of clear cut 1 or 0. its a soft measurement of accuracy with the idea of probabilistic confidence.
$$
log\,loss = - \frac{1} {N}\sum_{i}^{N} {y_i \log {p_i} + (1-y_i)log(1-{p_i})}\\
note: 0\,log0 = 0
$$
log loss is the cross entroy between distribution of the true labels and the predictions, and is closely related to relative entropy (Kullback-Leibler divergence). entropy measures the unpredictability of something, cross entropy incorporates the entropy of the true distribution plus the extra unpredictability when one assumes a different distribution than the true distribution. by minimizing log loss we maximize the accuracy of the classifier.

### AUC

AUC here is the area under the curve of the receiver operating characteristic curve (ROC). ROC curve shows the sensitivity of the classifier by plotting the rate of true positives to the rate of false positives. it shows how many correct positive classifications can be gained as you allow for more and more false positives. in simple terms the larger the AUC the better due to steep curve.

- true positive rate is equivalent to recall or sensitivity

$$
TPR = \frac{TP} {TP + FN}
$$



- specificity

$$
specificity = \frac{TN} {TN+FP}
$$



- false positive rate

$$
FPR = 1 - specificity\\
    = \frac{FP} {TN+FP}
$$

when AUC is 1 which means there exists a idea measure of separability between the classes, no overlapping of TN and TP distribution. but usually what we get is a overlapped distribution, where we have type 1 and type 2 error. if the AUC is 0.7 which implies that on average there is a 70% change the model will be able to distinguish between positive and negative class. when AUC is 0.5, this implies both positive and negative class distribution is completely overlapped. finally AUC is 0 implies that model is predicting negative class as positive and vice versa.