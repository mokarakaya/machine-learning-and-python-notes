- **Pros**: Easy to implement

- **Cons**: Can converge at local minima; slow on very large datasets

# K-means

```
Create k points for starting centroids (often randomly) While any point has changed cluster assignment for every point in our dataset:

for every centroid

  calculate the distance between the centroid and point

  assign the point to the cluster with the lowest distance

  for every cluster calculate the mean of the points in that cluster

  assign the centroid to the mean
```

# Bisecting K-means

- K-means may get caught local minima, because of poorly random initialization. K-means is sensitive to initial cluster placement.
- A way to solve this problem is to start with single cluster and split it into two clusters iteratively.
- We calculate sum of squared error (SSE) before each split, and we can either select the cluster with lowest error or the one with largest error.
- SSE is the sum of squared distances of elements to their clusters.

```
Start with all the points in one cluster While the number of clusters is less than k for every cluster

measure total error

perform k-means clustering with k=2 on the given cluster

measure total error after k-means has split the cluster in two

choose the cluster split that gives the lowest error and commit this split
```


# Defining the Number of Clusters
- We can plot within-cluster sum of square (`WSS`) vs number of cluster. This will give a `Elbow` and the `knee` is the optimal number of clusters.
