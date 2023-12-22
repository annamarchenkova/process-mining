import os
import yaml
import pandas as pd

def load_config(cnf_dir=PROJECT_DIR, cnf_name='config.yml'):
    config_file = open(os.path.join(cnf_dir, cnf_name))
    return yaml.load(config_file, yaml.FullLoader)

def date_cols_to_datetime(df, cols):
    '''Convert selected columns to datetime type'''
    df[cols] = df[cols].apply(lambda x: pd.to_datetime(x, infer_datetime_format=True))
    return df
