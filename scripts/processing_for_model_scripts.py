import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)
    # Removing duplicates
    data = data.drop_duplicates(keep="first")
    
    # Handling missing values (optional)
    data = data.fillna(method='ffill')
    return data

def encoder(method, dataframe, columns_label=None, columns_onehot=None):
    if method == 'labelEncoder':
        if columns_label is None:
            raise ValueError("No columns provided for label encoding.")
        
        df_lbl = dataframe.copy()
        for col in columns_label:
            if dataframe[col].dtype == 'object':
                label = LabelEncoder()
                df_lbl[col] = label.fit_transform(df_lbl[col].values)
            else:
                print(f"Skipping non-categorical column: {col}")
        return df_lbl
    
    elif method == 'oneHotEncoder':
        if columns_onehot is None:
            raise ValueError("No columns provided for one-hot encoding.")
        
        df_oh = dataframe.copy()
        df_oh = pd.get_dummies(data=df_oh, prefix='ohe', prefix_sep='_',
                       columns=columns_onehot, drop_first=True, dtype='int8')
        return df_oh

def scaler(method, data, columns_scaler):
    if method == 'standardScaler':        
        Standard = StandardScaler()
        df_standard = data.copy()
        df_standard[columns_scaler] = Standard.fit_transform(df_standard[columns_scaler])
        return df_standard
        
    elif method == 'minMaxScaler':        
        MinMax = MinMaxScaler()
        df_minmax = data.copy()
        df_minmax[columns_scaler] = MinMax.fit_transform(df_minmax[columns_scaler])
        return df_minmax
    
    elif method == 'npLog':
        df_nplog = data.copy()
        # Avoid log(0) or negative values
        if (df_nplog[columns_scaler] <= 0).any().any():
            raise ValueError("Log transformation is not possible on zero or negative values.")
        df_nplog[columns_scaler] = np.log(df_nplog[columns_scaler])
        return df_nplog
    
    return data