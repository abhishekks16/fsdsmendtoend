# This is my first end to end project

## First initialize the git
```
git init     
git add abc.txt ## adds the abc.txt file     
git add . ## adds all the file in the directory    
git commit -m "this is my first commit"  
git pull     
bash init_setup.sh # Note : use bash/Git bash/linux terminal
python template.py # To create the project template using python script.
```

## Ways to install the local packages
```
pip list # Lists all the packages installed
1 : python setup.py install # To install the local packages
pip uninstall DiamondPricePrediction # Uninstalls the package
2 : -e . # Add this line inside the requirements.txt and run "pip install -r requirements.txt"
```

## Data training 
> python src/DiamondPricePrediction/pipelines/training_pipeline.py

## Running Flask app
> python app.py



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### local cmd
- mlflow ui -- Opens the `MlFlow GUI` dashboard.

### dagshub
[dagshub](https://dagshub.com/)

![image](https://github.com/abhishekks16/fsdsmendtoend/assets/133478875/468f8cae-a014-4ec7-bef2-b90288ec14ce)

MLFLOW_TRACKING_URI=https://dagshub.com/abhishekks16/fsdsmendtoend.mlflow \
MLFLOW_TRACKING_USERNAME=abhishekks16 \
MLFLOW_TRACKING_PASSWORD=<password> \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/abhishekks16/fsdsmendtoend.mlflow
export MLFLOW_TRACKING_USERNAME=abhishekks16
export MLFLOW_TRACKING_PASSWORD=<password>

```


### DVC cmd
- dvc init
- dvc repro
- dvc dag

* Initialize the DVC, this will create the .dvc folder.
```
dvc init
```

* Remove the csv from git if it is already added. Because here we are using dvc to avoid the data storing in git.
* Add the csv data to track from dvc
```
dvc add notebooks/data/gemstone.csv
```
* Store these dvc into the remote storage(S3,Azure blob etc)
```
dvc remote add -d remote_storage path_to_the_storage
```
* Below is the example to store in the local storage, make local folder as remote
```
dvc remote add -d remote_storage C:/iNeuron_Code/ML/mlflow-dvc-demo/remote
```
* Push the dvc files into the remote(here it is local remote)
```
dvc push
```
* To track the file changes/ reproducibility of the file as per our `dvc.yaml` file
```
dvc repro
```
* To see the dependencies of `dvc.yaml`
```
dvc dag
```
