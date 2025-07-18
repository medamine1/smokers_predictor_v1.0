import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('C:/Users/ELYADRIMohammedAmine/Downloads/train.csv')
df = df.dropna()
X = df.drop(['id', 'smoking'], axis=1)
y = df['smoking']
scaler = MinMaxScaler()
scaled_X = scaler.fit_transform(X) 
scaled_df = pd.DataFrame(scaled_X, columns=X.columns)
X_train, X_test, y_train, y_test = train_test_split(scaled_X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)



model.fit(X_train, y_train)


# Test on the test set
y_pred = model.predict(X_test)

print("Test accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


joblib.dump(model, 'ml_model/model.pkl')
joblib.dump(scaler, 'ml_model/scaler.pkl')