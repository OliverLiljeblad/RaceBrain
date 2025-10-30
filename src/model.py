from sklearn.ensemble import RandomForestClassifier

def train_model(df, target_col):
    X = df.drop(columns=[target_col])
    y = df[target_col]
    model = RandomForestClassifier()
    model.fit(X, y)
    return model
