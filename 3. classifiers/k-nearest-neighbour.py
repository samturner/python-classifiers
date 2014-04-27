import numpy as np
import time, sys
import argparse
from collections import Counter

num_test = 100	# the number of test examples, the rest will be training
num_nn = 3		# the number of nearest neighbours to calculate

# build a dictionary of vectors and classes
def build_vectors(file):
	i = []
	next(file)		# skip the header line
	for line in file:
		i.append({'values': np.array(map(float,line.split(",")[0:-1])), 'class': line.split(",")[-1].strip()})
	print "Instances Loaded: " + str(len(i));
	return i
	
# given two attribute lists, find the euclidean distance, wraps numPy function
# a,b => vector containing instance values
def euclidean_dist (a, b):
	return np.linalg.norm(a-b)
	
# given the classes, return the most common class
# classes => a list of the classes of the nearest k neighbours
def most_common(classes):
	lst = Counter(classes).most_common()
	highest_count = max([i[1] for i in lst])
	return [i[0] for i in lst if i[1] == highest_count][0]

# given a list of the nearest neighbours, classify the example
# k_nn => the k nearest instances
def classify(k_nn):
	classes = []
	for inst in k_nn:
		classes.append(inst[1]['class'])
	return most_common(classes);

# the nearest neighbour algorithm	
# k => the number of nearest neighbours
# ktest => the testing set
# ktrain => the training set
def NN(k, ktest, ktrain):
	pred_classes = []			# the predicted classes for each of the test instances
	for inst in ktest:
		distances = []
		ki = inst['values'] 		# a vector containing the data
		
		for d in ktrain: 		# calculate and store all the distances to every other point
			di = d['values']
			distances.append((euclidean_dist(ki, di), d))
			
		k_nn = sorted(distances)[:k]	# sort the distances and get the k closest neighbours
		pred_classes.append(classify(k_nn))	# get the class that occurs most frequently and append it
	
	return pred_classes

# prints to command line and log
def out(f, msg):
	print(msg)
	f.write(msg + "\n")

				
def main():
	parser = argparse.ArgumentParser(description='K Nearest Neighbour Algorithm - Reads a pima.csv file and attempts to classify a number of instances specified.')
	parser.add_argument("--t", "-t", help="number of instances you want to test, the remaining instances will be used as a training set.", type=int, default=50)
	parser.add_argument("--k", "-k", help="number of nearest neighbours", type=int, default=3)
	args = parser.parse_args()
		
	num_test = args.t 
	num_nn = args.k
	
	start_time = time.time()
	f = open("k_nearest_neighbor.log", "a")
	
	out(f, "Running Nearest Neighbour with [" + str(num_nn) + "] nearest neighbours...");
		
	# read in the file and build a data structure to store values and classes
	instances = build_vectors(open("pima.csv", "rU"))
	
	if (num_test > len(instances)):		# make sure we don't have to many test instances
		out(f, "Too many test instances, exiting...")
		exit()
		
	out(f,"---------")
	#TODO: Implement stratified cross validation
	k_test = instances[-num_test:]
	k_train = instances[:-num_test]

	# k_test = instances[:num_test]			
	# k_train = instances[num_test+1:]		
	res = NN(num_nn, k_test, k_train)		# the resulting test case and the predicted class
		
	correct = 0
	for c in range(len(res)):		# count the number of correct classifications
		if k_test[c]['class'] == res[c]:
			correct += 1
			
	out(f, "Number of test instances: " + str(num_test))
	out(f, "Correctly classified instances: " + str(correct) + "\t[" + str(int(float(correct)/float(num_test) * 100)) + "%]")
	out(f, "Incorrectly classified instances: " + str(num_test-correct) + "\t[" + str(int((1-float(correct)/float(num_test)) * 100)) + "%]")
	out(f, "Completed in " + "%0.2f" % (time.time() - start_time) + " seconds");
	
	f.write("\n");	# new lines for output
	f.close()

if __name__ == '__main__':
	main()


