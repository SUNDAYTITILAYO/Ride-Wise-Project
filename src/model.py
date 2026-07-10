import pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / 'Data' / 'model_df.parquet'
df = pd.read_parquet(data_path, engine='pyarrow')

x = df.drop(columns = ['churn'])
y = df['churn']



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
mlflow.set_experiment("Ridewise-Wise-Project")

#with mlflow.start_run(run_name = "Logistic-Regression-v1"):
    #model = LogisticRegression(random_state=42, class_weight='balanced')
    #model.fit(x_train, y_train)

with mlflow.start_run(run_name = "RandomForestClassifier-v1"):
    model = RandomForestClassifier(
    n_estimators=500,
    random_state=42,
    class_weight="balanced"
)
    model.fit(x_train, y_train)   
    y_pred = model.predict(x_test)
    auc = roc_auc_score(y_test, y_pred)p

    mlflow.log_param("model", "Random Forest")
    mlflow.log_param("Features", x.columns.tolist())
    mlflow.log_param("mi_threshold", 0.01)
    mlflow.log_metric("roc_auc", auc)
    mlflow.sklearn.log_model(model)

    print(auc)

    
