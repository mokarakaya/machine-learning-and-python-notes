# Numpy
- Unlike Python list, Numpy forces arrays to have same type.


# Tensorflow
- `tf.constant`: e.g. for epsilon
- `tf.Variable` e.g. for weights
- `tf.placeholder`: e.g. for data.

- `Unit tests`: check size of variables, placeholders, constants (e.g. dropout). Verify that accuracy is 1 for a simple data set. Check loss is not zero. Reset graph between the tests. Mock methods which takes time to execute or requires network access.
- allow_soft_placement, allow_growth, per_process_gpu_memory_fraction.
- `Model parallelism`: Horizontal parallelism does not increase performance, Vertical parallelism requires many network.
- `Data parallelism`: Each device uses a different portion of data and then we get the average of gradients. In mirrored strategy, allreduce algorithm gets the gradients, calculates mean and then distributes to all replicas. In centralized strategy, there is one instance which calculates the mean, and distributes to replicas. This can  be sync or async.
