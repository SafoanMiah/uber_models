import pandas as pd

def explode_lists(df: pd.DataFrame, col1: str, col2: str, label) -> pd.DataFrame:
    '''
    Explode / Unpack 2 List Columns in a dataframe together

    Parameters:
    df (pd.DataFrame): The input DataFrame with columns.
    col1, col2 (str): Name of columns with list.
    label (str): Label to differentiate the exploded rows

    Returns:
    pd.DataFrame: DataFrame with exploded rows.d
    '''

    exploded_rows = []
    
    for idx, row in df.iterrows():
        column1 = row[col1]
        column2 = row[col2]
        col_label = label[idx]
        
        max_len = max(len(column1), len(column2))

        unpacked = pd.DataFrame({
            'label': col_label,
            col1: column1 + [None] * (max_len - len(column1)),
            col2: column2 + [None] * (max_len - len(column2))
        })
        
        exploded_rows.append(unpacked)
    
    exploded_df = pd.concat(exploded_rows, ignore_index=True)
    
    return exploded_df