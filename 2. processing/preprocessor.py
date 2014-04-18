# add the header line
f = open("pima_processed.csv", "w")

f.write('num_pregnant,glucose_concentration,blood_pressure,tricep_skin,serum_insulin,BMI,diabetes_pedigree,age,class\n')	# write out the header file

for line in open("pima-indians-diabetes.data", "rU"):
	lineArray = line.strip().split(",")		# split into an array
	lineArray[-1] = "class" + lineArray[-1]; 	# add class to last element

	if int(lineArray[2]) and int(lineArray[1]) and int(float(lineArray[5])) and int(float(lineArray[3])):	# remove missing values from appropriate attributes
		f.write(",".join(lineArray) + "\n")
		
f.close();