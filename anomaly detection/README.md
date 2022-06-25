[TOC]

# Anomaly Detection

## monitoring and alerting

monitoring is to collect as many metric from a single system to ensure we can observe important metric changes. however it is impossible to monitor everything all the time and thus automated alerting, usually with thresholds. some obvious use case ie disk storage can use this approach, but others will have problems with it especially those without a proper baseline

- outlying values in one dimension / variable
- outlying combination of values
- patterns of regularity or irregularity in data streams
- areas of high or low density
- illegal data values
- repetition

## outliers and anomalies detection

outliers is something that don't look like the others and anomalies is something that act differently from the past ([datadog oscon austin 2016](https://www.youtube.com/watch?v=mG4ZpEhRKHA&ab_channel=Datadog)). 

- OD, MAD media absolute deviation from the median
- OD, DBSCAN density-based spatial clustering of application with noise

> MAD is done in batch fashion, no time element in it while DBSCAN has time element considered

- AD, robust? (by decomposing into trend, periodicity and noise) [datadog blog](https://www.datadoghq.com/blog/introducing-anomaly-detection-datadog/)
- AD, adaptive? (if sudden change in baseline it will change weight from longer time period to shorter time period)

## use cases

- detecting problems, fraudulent transactions, system failures, bogus activity, medical problems
- detecting opportunitues, buying pattern, idenfitying unusually successful occurences, low usage periods for resources savings

## tricks

- using log scale (one axis or both axis)

## references

[gcp smart analytics reference pattern](https://cloud.google.com/architecture/reference-patterns/overview?utm_source=youtube&utm_medium=Unpaidsocial&utm_campaign=ana-20201116-smart-analytics-overview)

