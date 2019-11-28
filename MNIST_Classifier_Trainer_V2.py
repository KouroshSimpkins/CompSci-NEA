from __future__ import absolute_import, division, print_function
import pandas
import tensorflow as tf
import numpy as np

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)


def cnn_model_fn(features, labels, mode):
    """Model function for CNN"""
    # Input Layer
    input_layer = tf.reshape(features["x"], [-1, 28, 28, 1])

    # Convolutional Layer 1
    conv1 = tf.compat.v1.layers.conv2d(
        inputs=input_layer,
        filters=32,
        kernel_size=[5, 5],
        padding="same",
        activation=tf.nn.relu)

    # Pooling Layer 1
    pool1 = tf.compat.v1.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2],
                                              strides=2)

    # Convolutional layer 2 and Pooling layer 2
    conv2 = tf.compat.v1.layers.conv2d(
        inputs=pool1,
        filters=64,
        kernel_size=[5, 5],
        padding="same",
        activation=tf.nn.relu)
    pool2 = tf.compat.v1.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2],
                                              strides=2)

    # Dense Layer
    pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
    dense = tf.compat.v1.layers.dense(
        inputs=pool2_flat, units=1024, activation=tf.nn.relu)
    dropout = tf.compat.v1.layers.dropout(
        inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    # Logits Layer
    logits = tf.compat.v1.layers.dense(inputs=dropout, units=10)

    predictions = {
        # Generate predictions (for PREDICT and EVAL mode)
        "classes": tf.argmax(input=logits, axis=1),
        # Add `softmax_tensor` to the graph. It is used for PREDICT and by the
        # `logging_hook`.
        "probabilites": tf.nn.softmax(logits, name="softmax_tensor")
    }

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # Calculate loss (for both TRAIN and EVAL models)
    loss = tf.compat.v1.losses.sparse_softmax_cross_entropy(labels=labels,
                                                            logits=logits)

    # Configure the training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(
            learning_rate=0.001)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.compat.v1.train.get_global_step())
        return tf.estimator.EstimatorSpec(
            mode=mode, loss=loss, train_op=train_op)

    # Add evauation metrics
    eval_metric_ops = {
        "accuracy": tf.compat.v1.metrics.accuracy(
            labels=labels, predictions=predictions["classes"])
    }
    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)

# Loading the training and evaluation data


((train_data, train_labels),
 (eval_data, eval_labels)) = tf.keras.datasets.mnist.load_data()

train_data = train_data/np.float32(255)
train_labels = train_labels.astype(np.int32)

eval_data = eval_data/np.float32(255)
eval_labels = eval_labels.astype(np.int32)

# Creating the Estimator
mnist_classifier = tf.estimator.Estimator(
    model_fn=cnn_model_fn, model_dir="tmp/mnist_convent_model")

# Setting up logging for predictions
tensors_to_log = {"probabilities": "softmax_tensor"}

logging_hook = tf.estimator.LoggingTensorHook(
    tensors=tensors_to_log, every_n_iter=50)

# Training the model (calling train() on mnist_classifier)
train_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
    x={"x": train_data},
    y=train_labels,
    batch_size=100,
    num_epochs=None,
    shuffle=True)

# Training one step and displaying the probabilities
mnist_classifier.train(
    input_fn=train_input_fn,
    steps=1,
    hooks=[logging_hook])

mnist_classifier.train(input_fn=train_input_fn, steps=100000)

# Evaluating the model
eval_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
    x={"x": eval_data},
    y=eval_labels,
    num_epochs=1,
    shuffle=False)

eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)
print(eval_results)
