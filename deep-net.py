''' 
I/P => Weight -> 
		HL1(activation) => Weights 
			->HL2(activation) => Weights 
-> O/P 
'''
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)
#10 classes, 0-9
'''
0 = [1,0,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0,0]
3 = [0,0,0,1,0,0,0,0,0,0]
4 = [0,0,0,0,1,0,0,0,0,0]
5 = [0,0,0,0,0,1,0,0,0,0]
6 = [0,0,0,0,0,0,1,0,0,0]
7 = [0,0,0,0,0,0,0,1,0,0]
8 = [0,0,0,0,0,0,0,0,1,0]
9 = [0,0,0,0,0,0,0,0,0,1]
'''
###########################Configuration###########################
#Hidden layers
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500
#Matrix size 
n_classes = 10
#100 samples
batch_size = 100
learning_rate = 0.01
hm_epochs = 10
####################################################################
# matrix height[x] X width[y]
x = tf.placeholder('float',[None,784])
y = tf.placeholder('float')

def neural_network_model(data):
	#(input_data * weights) + biases
	hidden_layer_1 = {'weights':tf.Variable(tf.random_normal([784,n_nodes_hl1])),
					  'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

	hidden_layer_2 = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1,n_nodes_hl2])),
					  'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

	hidden_layer_3 = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2,n_nodes_hl3])),
					  'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

	output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3,n_classes])),
					  'biases':tf.Variable(tf.random_normal([n_classes]))}

	l1 = tf.add(tf.matmul(data,hidden_layer_1['weights']) , hidden_layer_1['biases'])
	l1 = tf.nn.relu(l1)

	l2 = tf.add(tf.matmul(l1,hidden_layer_2['weights']) , hidden_layer_2['biases'])
	l2 = tf.nn.relu(l2)

	l3 = tf.add(tf.matmul(l2,hidden_layer_3['weights']) , hidden_layer_3['biases'])
	l3 = tf.nn.relu(l3)

	output = tf.matmul(l2,output_layer['weights']) + output_layer['biases']

	return output

def train_neural_network(x, learning_rate):
	prediction = neural_network_model(x)
	cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction,y) )
	optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

	with tf.Session() as sess:
		sess.run(tf.initialize_all_variables())

		for epoch in range(hm_epochs):
			epoch_loss = 0
			for _ in range( int(mnist.train.num_examples / batch_size) ):
				epoch_x, epoch_y = mnist.train.next_batch(batch_size)
				_, c = sess.run([optimizer, cost], feed_dict = {x: epoch_x, y: epoch_y})
				epoch_loss += c
			print ('Epoch', epoch, 'completed out of', hm_epochs, 'loss:', epoch_loss)

		correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))

		accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
		print ('Accuracy:', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))
		#print ('Hidden Layers:', hm_nodes[1:-1])
		print ('Learning Rate:', learning_rate)


train_neural_network(x, learning_rate)