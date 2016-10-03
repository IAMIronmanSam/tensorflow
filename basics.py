#Install Tensorflow https://www.youtube.com/watch?v=CvspEt8kSIg
import tensorflow as tf
#Constants genrally it will be arrays
x1 = tf.constant(5)
x2 = tf.constant(6)

#Mul Operation
#result = x1 * x2
result = tf.mul(x1,x2)
#print(result)

## Classic 
#sess = tf.Session()
#op = sess.run(result)
#print(op)
#sess.close()

## Advanced
with tf.Session() as sess:
	op = sess.run(result)

print(op)