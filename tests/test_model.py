from src.model import train_model
import pandas as pd

def test_train_model_runs():
    data = pd.DataFrame({'feature': [1, 2], 'target': [0, 1]})
    model = train_model(data, 'target')
    assert model is not None
