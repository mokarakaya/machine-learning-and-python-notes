"""
Implement kmeans clustering


"""

import numpy as np
import matplotlib.pyplot as plt


class DataOperations:
    @staticmethod
    def generate_data():
        dist_1 = np.random.normal(5, 1, 40).reshape(20, 2)
        dist_2 = np.random.normal(10, 1, 40).reshape(20, 2)
        dist_3 = np.random.normal(15, 1, 40).reshape(20, 2)
        x = np.concatenate((dist_1, dist_2, dist_3))
        np.random.shuffle(x)
        return x


class KMeans:
    def __init__(self, number_of_clusters):
        self.number_of_clusters = number_of_clusters
        self.clusters = None

    def fit_predict(self, data):
        centroids = np.random.randint(0, len(data) - 1, self.number_of_clusters)
        centroids = data[centroids]
        clusters_changed = True
        clusters = self._create_clusters(data, centroids)
        iter_id = 1
        while clusters_changed:
            print(f"iter:{iter_id}")
            clusters = self._update_clusters(clusters)
            clusters, clusters_changed = self._assign_to_clusters(clusters)
            iter_id += 1
        self.clusters = clusters
        return clusters

    def _update_clusters(self, clusters):
        for cluster_id, cluster in clusters.items():
            new_centroid = self._calculate_centroid(cluster["items"])
            cluster["centroid"] = new_centroid
        return clusters

    def _assign_to_clusters(self, clusters):
        centroids = [cluster["centroid"] for _, cluster in clusters.items()]
        new_clusters = {}
        clusters_changed = False
        for cluster_id, cluster in clusters.items():
            for item in cluster["items"]:
                nearest_cluster_id = self._get_nearest_cluster(item, centroids)
                if nearest_cluster_id in new_clusters:
                    new_clusters[nearest_cluster_id]["items"].append(item)
                else:
                    new_clusters[nearest_cluster_id] = {
                        "centroid": centroids[nearest_cluster_id],
                        "items": [item],
                    }
                if nearest_cluster_id != cluster_id:
                    clusters_changed = True
        return new_clusters, clusters_changed

    @staticmethod
    def _get_nearest_cluster(d, centroids):
        return np.argmin(np.sum(np.sqrt((d - centroids) ** 2), axis=1))

    def _create_clusters(self, data, centroids):
        clusters = {}
        for d in data:
            nearest_cluster_id = self._get_nearest_cluster(d, centroids)
            if nearest_cluster_id in clusters:
                clusters[nearest_cluster_id]["items"].append(d)
            else:
                clusters[nearest_cluster_id] = {
                    "centroid": centroids[nearest_cluster_id],
                    "items": [d],
                }
        return clusters

    @staticmethod
    def _calculate_centroid(items):
        return np.mean(items, axis=0)

    def plot_clusters(self):
        if not self.clusters:
            raise ValueError("need to cluster")
        color = ["r", "b", "g"]
        colors = []
        x = []
        y = []
        for cluster_id, cluster in self.clusters.items():
            for item in cluster["items"]:
                x.append(item[0])
                y.append(item[1])
                colors.append(color[cluster_id])
        plt.scatter(x, y, c=colors)
        plt.show()


def main():
    data = DataOperations.generate_data()
    number_of_clusters = 3
    k_means = KMeans(number_of_clusters)
    k_means.fit_predict(data)
    k_means.plot_clusters()


if __name__ == "__main__":
    main()
