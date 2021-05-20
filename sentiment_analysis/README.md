# Sentiment analysis

This folder contains datasets and the code to crawl, preprocess the data and train the classification models.


## Steps to preprocess data and train the classfication models.
The notebooks and datasets used for this process are located inside the "Classification Notebooks and Datasets" folder.

### STEP 1: Upload two notebooks to drive and open them with google colab. 

The folder contains two Jupyter notebooks, namely "Preprocess Tweets.ipynb" and "Final IR Classification Notebook.ipynb". To run these notebooks, we will need TPU hardware accelerator as well as the built-in environment of google colab. Therefore, rather than running on the local machine, using google colab to execute these notebooks is recommended.

### STEP 2: Change the runtime type of google colab notebook to "TPU".
Go to Runtime > Change runtime type. \
Under Hardware Accelerator, select "TPU"

### STEP 3: Upload the folder Data to the drive.
The folder "Data" in this folder consists of our original datasets as well as the saved dataset after being preprocessed. All of the datasets used in our notebook are stored in Drive and accessed from google colab.

### STEP 4: Adjust the value of directory variables.
The directories of the dataset may vary depending on where the data is located. This means that the directory variable has to be adjusted before running the notebook. \
\
In the notebook "Preprocess Tweets.ipynb", the variable "data_folder" will need to be changed (decided by where the folder Data is uploaded in Drive). In our case, its value is as follows: \
data_folder = "/content/drive/MyDrive/CZ4034 - Information Retrieval/Data". \
\
In the notebook "Final IR Classification Notebook.ipynb", the variable "data_folder"  and "save_model_folder" will need to be changed (decided by where the folder Data is uploaded in Drive and where we would like to save the model). In our case, their values are as follows: \
data_folder = "/content/drive/MyDrive/CZ4034 - Information Retrieval/Data" \
save_model_folder = "/content/drive/MyDrive/CZ4034 - Information Retrieval/models" \

Note: The directory values here are directories of google colab after mounting Google Drive into it.
### STEP 5: Run the "Preprocess Tweets.ipynb" to process the original data.
After opening the notebook "Preprocess Tweets.ipynb" and execute the cells by following the instructions mentioned in the notebook, the original dataset will be preprocessed and saved.

### STEP 6: Run the "Final IR Classification Notebook.ipynb" to train, test and save the model.
After opening the notebook "Final IR Classification Notebook.ipynb" and executing the cells by following the instructions mentioned in the notebook, the models will be trained and saved.
