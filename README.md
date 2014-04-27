# COMP3308 Assignment 1

### Folders & Steps
* **1. Raw Data** - Contains the raw pima indians diabetes `.data` file as well as the `.name` file as well as the assignment spec.
* **2. Processing** - Contains everything needed to generate the processed `.csv` file:
	*  Run the `preprocessor.py` file to add a header, change the class names and remove invalid results (see *Assumptions and Invalid Data*).
	* Open the resulting `pima_processed.csv` file in Weka and go `Filter > Choose > Attribute > Normalise > Apply` and then save the file as `pima.csv` to get a normalised CSV file.
* **3. Classifiers** - contains python scripts to run the classifiers:
	* `classifier.py`
		* Run `classifier.py -h` for more information about argument usage.
		* A log file `classifier.log` will be created which logs information about the run such as *number of correctly and incorrectly identified instances*.
		* `--folds`, `-f`  number of folds you want to split the data into (default 10)
		* `--neighbours`, `-k`, number of nearest neighbours (default 3)
		* `--algorithm`, `-a`, the algorithm to run (KNN/NB)
* **4. Feature Selection** - contains a version of the data that has been run through Weka's CFS feature selection:
	* Open the `pima.csv` file generated in step 2 in Weka and go `Select Attributes > Start > Right click the result > Save Reduced data...`
	* Some header information that Weka generates in puts in the file had to be removed manually.

* **5. Results** - contains a results spreadsheet and the final report.
	* `results_matrix.xlsx` - Compares our classifiers to Weka's for both the data with no feature selection and the data with feature selection (this is also included in `report.pdf`)
	* `report.pdf` - TODO

### Assumptions and Invalid Data
* There are a number of fields in the data where attributes are missing and have been coded as 0. We have decided to remove the rows containing a 0 value in the following fields:
	* Glucose Concentration
	* Blood Pressure
	* Tricep Skin
	* Body Mass Index (BMI)