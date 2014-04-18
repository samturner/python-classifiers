# add the header line
f = open("pima.csv", "w")

i = 0;

f.write('num_pregnant,glucose_concentration,blood_pressure,tricep_skin,serum_insulin,BMI,diabetes_pedigree,age,class\n')
for line in open("pima-indians-diabetes.data", "rU"):
	lineArray = line.strip().split(",")
	lineArray[-1] = "class" + lineArray[-1]; # add class to last element
	

	if int(lineArray[2]) and int(lineArray[1]) and int(float(lineArray[5])) and int(float(lineArray[3])):
		f.write(",".join(lineArray) + "\n")
		i += 1;
		
f.close();

print i