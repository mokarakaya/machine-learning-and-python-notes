# Value Definition
## Constant
- `tf.constant(value, dtype=None, shape=None, name='Const')`: Crates a constant tensor.

## Variable
- `tf.Variable(initial_value=None, trainable=None)`
- `v = tf.Variable(1.) `
  - `v.assign(2.) `
  - `v.assign_add(0.5) `
- Variables are trainable by default. So we generally keep weights in Variable.
- In TensorFlow1, we need to initialize variables before we run the graphs as follows. This is not needed in Tensorflow2.     
```
init=tf.global_variables_initializer()
sess.run(init)
```

## Placeholder
- `tf.placeholder( dtype, shape=None, name=None)`
- We do not need to assign value to placeholders and we can set the values in feed_dict `sess.run(y, feed_dict={x: rand_array}` where `x` is a placeholder and `y` is an arbitrary function.
- We generally keep input in placeholder because we can data is generally large and feed it later.
- `x = tf.placeholder(tf.float32, [None, 2])`: We have not decided yet the batchsize. Therefore we can define the first dimension of the placeholder as `None` which means the size of the first dimension is arbitrary.

# Neural Network

- Example is mnist data set where each picture as 784 pixels, and it is a classification problem.


```
import tensorflow as tf

x = tf.placeholder(tf.float32, shape=[None, 784])

# There are 10 neurons.
W = tf.Variable(tf.zeros([784,10]))

b = tf.Variable(tf.zeros([10]))

I = tf.matmul(x,W) + b

# There are 10 possible outputs. [0,9]
y_true = tf.placeholder(tf.float32, [None, 10])

individual_loss = tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=I)

loss_function = tf.reduce_mean(individual_loss)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)

train = optimizer.minimize(loss_function)

init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)
  for step in range(1000):
    batch_x, batch_y = mnist.train.next_batch(100)
    sess.run(train, feed_dict={x:batch_x, y_true:batch_y})

```


## NN with Keras

```
## output has 10 possible values, and softmax is needed since it is a classification problem.
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28,28)),
  tf.keras.layers.Dense(100, activation=tf.nn.relu),
  tf.keras.layers.Dense(10,activation=tf.nn.softmax)])

model.compile(optimizer='adam',
  loss='sparse_categorical_crossentropy',
  metrics=['accuracy'])

model.fit(x_train,y_train, epochs = 10)
model.evaluate(x_test, y_test)
```


# Taking Tensorflow to Production

## Implementing unit-tests
 - Check sizes of the variables and placeholders.
 - Check values of constants and other values e.g. dropout should be more than 0.1.
 - Create a very simple data and check if the accuracy is 100%.
 - Check shape of batch_size and target_size.
 - Check shape of the neural network.
 - Make sure the loss is never zero.
 - Make sure you reset the graph between each test.
 - Mock methods which may take long time to execute or requires network access.


### Eliminate non-determinism and flakes
- Use random with seed `random.seed(42)` or `np.random.seed(42)`
- Avoid using sleep.


## Using Multiple Executors

- We can set the config options as follows;

```
config=tf.ConfigProto()
# set config options here.
sess = tf.Session(config=config)
```

- `log_device_placement=True`: log the device of each operation e.g `cpu:0` and `gpu:0`
- `config.allow_soft_placement = True`: By default Tensorflow decides how to distribute calculations to the devices. If we specify the device as GPU and it is not available, we will get error. This option allows it to fall into CPU when the given device is not available.
- `config.gpu_options.allow_growth = True`: Tensorflow allocates a large portion of GPU memory by default. We can start with a small memory and increase automatically when need by enabling this option.
- `config.gpu_options.per_process_gpu_memory_fraction = 0.4`: Limits the GPU memory usage of tensorflow.

- We can run operations by specifying a device as follows;

```
with tf.device("/cpu:0"):
    c = tf.Variable(42.0)

```

## TF Serving
- TF Serving project enables us to deploy saved models, and serve the predict function via REST API, or gRPC API.
- It is also possible to serve several versions of models for A/B testing.
- A simple way is to use docker image of TF Serving and start the container by setting the model in options `-v`.
- REST API is useful when the input and output is small.
- `gRPC API` uses `PredictRequest` and `PredictResponse` for communication. These objects in `tensorflow-serving-api` project, and transfered via serialization.
- If we expect to receive too many requests per second, we can also run multiple TF Serving instance and we can configure a Load Balancer on top of the instances.

# Training Models Across Multiple Devices
- There are two options to consider while splitting the operations into multiple devices. These are Model Parallelism and Data Parallelism.

## Model Parallelism
- There two ways to implement Model Parallelism
  - `Horizontally`: Each layer on a different device.
  - `Vertically`: Split first part of each layer into once device and so on.
- Model Parallelism may not work very well depending on the model. As an example it is complicated to apply model parallelism to fully connected layers. Horizontally parallelization does not increase the performance for fully connected layers because, each layer waits the output of the previous layer. Vertical parallelization is relatively better, but it requires many network communication since a neuron needs the output of other splits. Vertical parallelization may fit better to CNN since the layers are not fully connected.
- Although, it may not be faster in practice, it is easier to horizontally parallelise RNNs. At the beginning only the first device will be active, but later the upper layers will get the output of the lower layer and work simultaneously.
- In short, model parallelism depends on model, and data parallelism is much simple and efficient.  

## Data Parallelism
- Model is replicated on each device, and each device use a different portion of data to train the model. Then we get the average of gradients from devices and update the model parameters. This is the main idea, and there are several ways to implement it.

### The Mirrored Strategy
- The parameters are mirrored perfectly, and they are always same in all replicas. This effective especially when all replicas are on the same machine. `AllReduce` algorithm collects the gradients, gets the mean, and distributes the output to all replicas. This process is `synchronous`.

### Centralized Parameters
- Parameter servers (generally has only CPU) keeps all the parameters. It gets the mean and updates the parameters. This process can either be `synchronous` or `asynchronous`.

- `Synchronous`: Replicas calculates the gradients and sent it to the server, then they wait until they get the new parameters. The slowest replica determine the performance. A workaround is to ignore slowest n replicas. Parameter server may saturate bandwidth since it sends the parameters to the replicas at the same time.

- `Asynchronous`: A replica does not wait for getting updates from the server and it continues with the next epoch. It may get update anytime. The problem is that it may receive `stale gradients`. These gradients are not up-to-date and they may have a different direction. In order to alleviate this problem we can;
  - Reduce the learning rate.
  - Drop stale gradients or scale them down.
  - Adjust mini-batch size.
  - Start with single replica for a few epochs and then activate others.

### Data Parallelism Implementation

```
distribution = tf.distribute.MirroredStrategy()
# distribution = tf.distribute.experimental.CentralStorageStrategy()

with distribution.scope():
    mirrored_model = keras.models.Sequential([...])
    mirrored_model.compile([...])

batch_size = 100 # must be divisible by the number of replicas
history = mirrored_model.fit(X_train, y_train, epochs=10)
```

- Tensorflow Cluster Roles:
  - `worker`: Performs computations.
  - `chief`: Performs computations and writes to Tensorflow board, saves checkpoints etc.
  - `Parameter Server`: Keeps track of variable values.
  - `Evaluator`: Evaluates performance.

# Other Tensorflow Projects
- `TF Lite` is used to deploy models and get predictions on the mobile devices.
- `Tensorflow.js` is used to deploy models to browsers.
