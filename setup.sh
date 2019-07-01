#!/bin/bash

sudo apt-get install -y mongodb-org

mkdir ~/mongodbpath
mongod --dbpath ~/mongodbpath/ --port 1234

conda create -n hyperopt-env scipy numpy pandas scikit-learn spyder
conda activate hyperopt-env

pip install hyperopt
pip install mlflow


conda activate hyperopt-env
cd Desktop/git/hyperopt-example
python min.py

conda activate hyperopt-env
cd Desktop/git/hyperopt-example
hyperopt-mongo-worker --mongo=localhost:1234/mongodbpath --poll-interval=1 --exp-key=exp6 --last-job-timeout 60
