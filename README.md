# Diabetes-prediction-using-Adaptive-Boosting

These days, diabetes has become one of the most common and prevalent diseases amongst people of all age groups. The exact cause of diabetes is unknown but is believed to arise due to a combination of lifestyle, genetics, stress and age factors. 
This project aims to predict a person’s risk of diabetes using a machine learning model. 
The PIMA Indians Diabetes (PID) Dataset has been chosen to perform exploratory data analysis in the proposed work.
Preprocessing techniques are applied on this dataset to remove data inconsistencies. 
On this preprocessed data, backward feature selection and dimensionality reduction using UMAP(Unified Manifold Approximation and Projection) is applied. 
Gridsearchcv is used for parameter tuning.
Finally, Random Forest and Support Vector Classifier (SVC) algorithms along with AdaBoost are stacked as a hybrid model to improve the accuracy of the model.
This model achieved an overall accuracy of ’84.65%’ in predicting diabetes.
In the proposed work, various health parameters like BMI, blood glucose, number of pregnancies and diabetes pedigree function are taken as input from the user to make prediction of diabetes by using flask.

