# data_processing.py

import pandas as pd

def load_data(gracedb_path: str, gwskynet_path: str) -> pd.DataFrame:
    """
    Load data from the provided CSV files and merge them on the 'Event_ID' column.
    
    Args:
        gracedb_path (str): Path to the GraceDB CSV file.
        gwskynet_path (str): Path to the GWSkyNet CSV file.

    Returns:
        pd.DataFrame: Merged DataFrame.
    """
    gracedb_df = pd.read_csv(gracedb_path)
    gwskynet_df = pd.read_csv(gwskynet_path)
    
    # Merging on 'Event_ID'
    merged_df = pd.merge(gracedb_df, gwskynet_df, on='Event_ID', how='inner')
    return merged_df

def filter_data(df: pd.DataFrame, grace_types: list, gw_types: list, significance: list) -> pd.DataFrame:
    """
    Filter the merged DataFrame based on the selected checkboxes.
    
    Args:
        df (pd.DataFrame): Merged DataFrame to filter.
        grace_types (list): Selected GraceDB object types to filter.
        gw_types (list): Selected GWSkyNet object types to filter.
        significance (list): Selected significance levels to filter.
        
    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    # Filtering by GraceDB object types
    filtered_df = df[df['Object_Type_x'].isin(grace_types) & df['Object_Type_y'].isin(gw_types)]
    
    # Filtering by significance levels
    filtered_df = filtered_df[filtered_df['Significance'].isin(significance)]
    
    return filtered_df
