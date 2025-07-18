## Model Training / RandomForestClassifier

Before running the prediction or testing scripts, **you must train the machine learning model first** to generate the `model.pkl` file.

### Steps to train the model

1. Prepare your training dataset.
2. Run the training script (e.g., `train_model.py`).
3. This will create the serialized model file `ml_model/model.pkl`.
4. Once the model file is created, you can run the prediction/testing scripts.

## Requirements

Make sure you have Python 3.x installed.

Install the required Python packages with:

```bash
pip install -r requirements.txt

---

**Note:** The `model.pkl` file is not included in the repository due to its size. Please train the model locally or obtain the pre-trained model file before testing.
