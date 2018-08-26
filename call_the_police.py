from helper import load_data
from __future__ import absolute_import,dividion,print_function
import numpy as np
import tensorflow as tf
import cv2


class Model:

	def __init__(self,features,labels):
		self.train_features = features #training
		self.train_labels = labels
		self.test_features = features
		self.test_labels = labels
		self.mode = None 

	def create_model(self):
		input_layer = tf.reshape(self.train_features,[-1,250,250,1])

		conv1 = tf.layers.conv2d(
				inputs=input_layer,
				filters=32,
				kernel_size=[5,5],
				activation=tf.nn.relu
		)

		pool1 = tf.layers.max_pooling2d(inputs=conv1,pool_size=[2,2],strides=2)

		conv2 = tf.layers.conv2d(
				inputs=pool1,
				filters=64,
				kernel_size=[5,5],
				padding="same",
				activation=tf.nn.relu
		)

		pool2 = tf.layers.max_pooling2d(inputs=conv2,pool_size=[2,2],strides=2)

		pool2_flat = tf.reshape(pool2,[-1,7*7*64])


		dense = tf.layers.dense(inputs=pool2_flat,units=1024)

		# Regularization
		dropout =  tf.layers.dropout(
				inputs=dense,
				rate=0.4,
				training=self.mode == tf.estimator.ModeKeys.TRAIN
		)

		self.logits = tf.layers.dense(inputs=dropout,units=10)

	def train(self):
		loss = tf.losses.sparse_softmax_cross_entropy(labels=self.train_labels, logits=self.logits)

		if self.mode == tf.estimator.ModeKeys.TRAIN:
			optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
			train_op = optimizer.minimize(
        		loss=loss,
        		global_step=tf.train.get_global_step()
        	)
		return tf.estimator.EstimatorSpec(mode=self.mode,loss=loss,train_op=train_op)

	def evaluate(self):
		eval_metric_ops = {
			"accuracy":tf.metrics.accuracy(
				labels=labels,predictions=predictions["classes"]
			)
		}
		return tf.estimator.EstimatorSpec()

	def predict(self):
		predictions = {
      		"classes": tf.argmax(input=logits, axis=1),
      
      		"probabilities": tf.nn.softmax(logits, name="softmax_tensor")
  		}
		if mode == tf.estimator.ModeKeys.PREDICT:
			return tf.estimator.EstimatorSpec(mode=self.mode, predictions=predictions)

def model_fn():
	pass

def main():
	data = load_data()
	classifier = tf.estimator.Estimator(
		model_fn=model_fn,model_dir=os.getcwd())
	train_data = 
	test_data = 
if __name__ == '__main__':
	main()