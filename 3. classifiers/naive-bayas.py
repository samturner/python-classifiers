import numpy as np
import time
from collections import Counter

num_test = 50	# the number of test examples, the rest will be training

# build a dictionary of vectors and classes
def build_vectors(file):
	i = []
	next(file)		# skip the header line
	for line in file:
		i.append({'values': np.array(map(float,line.split(",")[0:-1])), 'class': line.split(",")[-1].strip()})

	print "Instances Loaded: " + str(len(i));
	return i
	

# http://www.danielsoper.com/statcalc3/calc.aspx?id=54
# u = mean
# o = std dev
# x is the value to calculate for
def normal_pdf (u, o, x):
	return (1 / np.sqrt(2*np.pi*o)) * pow(np.e, -(((x - u)**2)/(2*o)))


# the naive bayas
# ktest => the testing set
# ktrain => the training set
def NB(ktest, ktrain):
	# get all the classes
	classes = []
	for i in ktrain:
		classes.append(i['class'])

	out_vector = {}
	for c in list(set(classes)):
		out_vector[c] = {}
		out_vector[c]['count'] = 0
		for i in ktrain:
			if i['class'] == c:
				out_vector[c]['count'] += 1
		out_vector[c]['p'] = float(out_vector[c]['count'])/len(ktrain)

		out_vector[c]['data'] = []
		for i in range(len(ktrain[0]['values'])):
			out_vector[c]['data'].append([])

	for i in ktrain:
		x = 0
		for j in i['values']:
			out_vector[i['class']]['data'][x].append(j)
			x += 1

	for c in list(set(classes)):
		for i in range(len(out_vector[c]['data'])):
			out_vector[c][str(i)+'_avg'] = np.mean(out_vector[c]['data'][i])
			out_vector[c][str(i)+'_var'] = np.var(out_vector[c]['data'][i])

	# print out_vector

	predicted = []
	# for each of the possible classes - see which is more probable
	for curr in ktest:
		# print curr
		cl = ''
		pr = 0
		for c in list(set(classes)):
			p = out_vector[c]['p']
			for i in range(len(out_vector[c]['data'])):
				p *= normal_pdf(out_vector[c][str(i)+'_avg'], out_vector[c][str(i)+'_var'], curr['values'][i])
			if p > pr:
				pr = p
				cl = c
		predicted.append(cl)

	return predicted

# prints to command line and log
def out(f, msg):
	print(msg)
	f.write(msg + "\n")

			

def main():
	start_time = time.time()	
	f = open("naive-bayas.log", "a")
	
	out(f, "Running naive bayas...");
		
	# read in the file and build a data structure to store values and classes
	instances = build_vectors(open("pima.csv", "rU"))

	if (num_test > len(instances)):		# make sure we don't have to many test instances
		out(f, "Too many test instances, exiting...")
		exit()
		
	out(f,"---------")
	#TODO: Implement stratified cross validation
	
	k_test = instances[-num_test:]
	k_train = instances[:-num_test]

	res = NB(k_test, k_train)		# the resulting test case and the predicted class
		
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


