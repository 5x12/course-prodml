# HSE Productive development of machine learning scripts
HW#3. Course: Research Seminar “Big Data: Principles and Paradigms”.
## Summary
This repository contains an attempt to create an imitation of productive script development with predictive machine learning models.
## Data
<b>Data Source (provided by Andrew Wolf):</b> <a href="https://github.com/5x12/ml-cookbook/blob/master/supplements/data/heart.csv" target="_blank">ml-cookbook heart.csv</a>
<br>This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V. It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them. The "target" field refers to the presence of heart disease in the patient. It is integer valued 0 = no disease and 1 = disease.

<b>Data Description:</b>
1. age
2. sex
3. chest pain type (4 values)
4. resting blood pressure
5. serum cholestoral in mg/dl
6. fasting blood sugar > 120 mg/dl
7. resting electrocardiographic results (values 0,1,2)
8. maximum heart rate achieved
9. exercise induced angina
10. oldpeak = ST depression induced by exercise relative to rest
11. the slope of the peak exercise ST segment
12. number of major vessels (0-3) colored by flourosopy
13. thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.

## Folder structure
<a href="https://github.com/missukrof/hse-ml-rs-hw3/tree/main/conf" target="_blank">conf folder</a> includes configuration files for a program
<br><a href="https://github.com/missukrof/hse-ml-rs-hw3/tree/main/connector" target="_blank">connector folder</a> includes the bridge to the source of data
<br><a href="https://github.com/missukrof/hse-ml-rs-hw3/tree/main/model" target="_blank">model folder</a> includes the models as well as their configuration files util folder includes miscellaneous functions like save/load models
<br><a href="https://github.com/missukrof/hse-ml-rs-hw3/tree/main/util" target="_blank">util folder</a> includes miscellaneous functions like save/load models
<br>The entrypoint.py contains a prediction function with the path to the models. The entrypoint_cli.py contains a prediction function with the path to the models to launch via the terminal.

## Algorithms used (formed in Pipeline: preprocessor & model)
0. Preprocessor -> <a href="https://github.com/missukrof/hse-ml-rs-hw3/blob/main/model/conf/preprocessor_heart.pkl" target="_blank">ColumnTransformer (Scaler: StandardScaler; Encoder: OneHotEncoder)</a>
1. Models:
<br>1.1 K-Nearest Neighbours -> <a href="https://github.com/missukrof/hse-ml-rs-hw3/blob/main/model/conf/kneighbors_heart.pkl" target="_blank">K-Nearest Neighbours in pickle format</a>
<br>1.2 XGBoost -> <a href="https://github.com/missukrof/hse-ml-rs-hw3/blob/main/model/conf/xgboost_heart.pkl" target="_blank">XGBoost in pickle format</a>

## Results
All the algorithms were compared using the accuracy metric. K-Nearest Neighbours and XGBoost were compared. Both of these were then used (alone with feature preprocessing and best hyperparameters) on the test dataset and "target" was classified into 1 and 0.
<br>Accuracy of Pipeline (model: KNeighborsClassifier): 86.04 -> <a href="https://github.com/missukrof/hse-ml-rs-hw3/blob/main/model/reports/kn_report_20221220_020701.522892.txt" target="_blank">KNeighborsClassifier performance report</a>
<br>Accuracy of Pipeline (model: XGBClassifier): 93.83 -> <a href="https://github.com/missukrof/hse-ml-rs-hw3/blob/main/model/reports/xgb_report_20221220_020701.659265.txt" target="_blank">XGBClassifier performance report</a>
