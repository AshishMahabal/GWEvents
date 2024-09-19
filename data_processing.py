# data_processing.py

import pandas as pd
import streamlit as st

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
    merged_df = pd.merge(gracedb_df, gwskynet_df, on='EventName', how='inner')
    return merged_df

def filter_data(df: pd.DataFrame, grace_types: list, gw_types: list, significance: list, detectors: list, subselection: str) -> pd.DataFrame:
    """
    Filter the merged DataFrame based on the selected checkboxes and subselection mode.
    
    Args:
        df (pd.DataFrame): Merged DataFrame to filter.
        grace_types (list): Selected GraceDB object types to filter.
        gw_types (list): Selected GWSkyNet object types to filter.
        significance (list): Selected significance levels to filter.
        detectors (list): Selected detectors to filter.
        subselection (str): Subselection mode ('Any One', 'Exactly One', 'Any Two', etc.)
        
    Returns:
        pd.DataFrame: Filtered DataFrame.
    """

    # Filtering by GraceDB object types
    filtered_df = df[df['GDB_Class'].isin(grace_types) & df['HierarchicalClass'].isin(gw_types)]
    
    # Filtering by significance levels
    filtered_df = filtered_df[filtered_df['Significant'].isin(significance)]

    #st.write(detectors)
    # Filter by detectors based on subselection mode
    if len(detectors) > 0:
    #if detectors:
        #st.write(detectors)
        if subselection == "Any One":
            filtered_df = filtered_df[filtered_df['Detectors'].apply(lambda x: any(d in x for d in detectors))]
        elif subselection == "Exactly One":
            filtered_df = filtered_df[filtered_df['Detectors'].apply(lambda x: sum(d in x for d in detectors) == 1)]
        elif subselection == "Any Two":
            filtered_df = filtered_df[filtered_df['Detectors'].apply(lambda x: sum(d in x for d in detectors) >= 2)]
        elif subselection == "Exactly Two":
            filtered_df = filtered_df[filtered_df['Detectors'].apply(lambda x: sum(d in x for d in detectors) == 2)]
        elif subselection == "All Three":
            filtered_df = filtered_df[filtered_df['Detectors'].apply(lambda x: all(d in x for d in detectors))]
    else:
        st.warning("Select at least one detector")
        filtered_df = pd.DataFrame()  # Return an empty DataFrame
    
    return filtered_df
