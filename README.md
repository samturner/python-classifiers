# COMP3308 Assignment 1

### Folders & Steps
* **1. Raw Data** - Contains the raw pima indians diabetes `.data` file as well as the `.name` file. Also contains the assignment spec.
* **2. Processing** - Contains everything needed to generate the processed `.csv` file:
	*  Run the `preprocessor.py` file to add a header, change the class names and remove invalid results.
	* Open the resulting `pima_processed.csv` file in Weka and go `Filter > Choose > Attribute > Normalise > Apply` and then save the file as `pima.csv` to get a normalised CSV file.
* **3. Classifiers**
	* `k-nearest-neighbour.py`
		* Run `k-nearest-neighbour.py -h` for more information about argument usage.
		* A log file `k_nearest_neighbor.log` will be created which logs information about the run such as *number of correctly and incorrectly identified instances*.
	* `naive-bayes.py`
		* Run `naive-bayes.py -h` for more information about argument usage.
		* A log file `naive-bayes.log` will be created which logs information about the run such as *number of correctly and incorrectly identified instances*.

### Assumptions and Invalid Data
* There are a number of fields in the data where attributes are missing and have been coded as 0. We have decided to remove the rows containing a 0 value in the following fields:
	* Glucose Concentration
	* Blood Pressure
	* Tricep Skin
	* Body Mass Index (BMI)