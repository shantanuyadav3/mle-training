# mle-training

# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## Conda Environment
    conda config --append channels conda-forge # set conda-forgre channel active
    conda env export --no-builds > env.yml #export conda environment one which is active in  env.yml file
    conda env create -f env.yml # create the environment using env.yml file


## To excute the script
    export QT_QPA_PLATFORM=offscreen
    python src/nonstandardcode.py
