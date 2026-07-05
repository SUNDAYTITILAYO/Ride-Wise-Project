import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report
import mlflow
import mlflow.sklearn

df = pd.read_parquet('../Data/model_df.parquet', engine='pyarrow')

x = df.drop(columns = ['churn'])
y = df['churn']



x_train, y_train, x_test, y_test = train_test_split(x,y, test_size = 0.2, random_state = 42, stratify = y)  
mlflow.set_experiment("Ridewise-Wise-Project")

with mlflow.start_run(run_name = "Logistic-Regression-v1"):
    model = LogisticRegression(Random_state = 42, class_weight = 'balanced')
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)
    auc = roc_auc_score(y_test, y_pred)

    mlflow.log_param("model", "Logistic Regression")
    mlflow.log_param("Features", x.columns.tolist())
    mlflow.log_param("mi_threshold", 0.01)
    mlflow.log_metrics("model_performance", auc)
    mlflow.sklearn.log_model(model)

    print(auc)
    
    
