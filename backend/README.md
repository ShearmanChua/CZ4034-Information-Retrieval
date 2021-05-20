# Backend code

This folder contains the code for the backend of the system (Solr)

## How to start the Solr server?
Direct to the `solr-7.7.3` folder and start the Solr server
```
$ cd solr-7.7.3/
$ ./bin/solr start
```

## How to index new data?
The existing toxic tweet data has already been indexed in Solr.
If you need to re-index or add new data, please follow the below steps:

1. Install necessary dependencies
```
$ pip install -r requirements.txt
```

2. Put the new data in the `sample_data.csv` file

3. Run the Python script to index the new data in Solr
```
$ python add_data_to_solr.py
```
