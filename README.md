# Gravitational Wave Astronomy Alert Filtering

This Streamlit application allows users to filter gravitational wave alerts from GraceDB and GWSkyNet based on object types and significance levels.

## Installation

```bash
pip install -r requirements.txt

## Data Overview

The application uses two CSV files: `event_predictions_table.csv` and `event_predictions_table_metadata.csv`. Below are the field names and the first row of data for each file:

### `event_predictions_table.csv`

| EventName | Detectors | SkyArea | MeanDistance | MaxDistance | LogBCI | LogBSN | GlitchScore | NSScore | BBHScore | GlitchScoreErr | NSScoreErr | BBHScoreErr | HierarchicalClass |
|-----------|-----------|---------|--------------|-------------|--------|--------|-------------|---------|----------|----------------|------------|-------------|-------------------|
| S230518h  | HL        | 1002.0  | 276.0        | 473.0       | 6.7    | 44.5   | 1.0         | 81.0    | 15.0     | 0.0            | 7.0        | 5.0         | NS               |

### `event_predictions_table_metadata.csv`

| EventName | GPSTime     | FAR  | Significant | GDB_GlitchScore | GDB_BNSScore | GDB_NSBHScore | GDB_BBHScore | GDB_Class |
|-----------|-------------|------|-------------|-----------------|--------------|---------------|--------------|-----------|
| S230518h  | 1368449966.2| 0.01 | True        | 10.0            | 0.0          | 86.0          | 4.0          | NS        |

Both files share the `EventName` field, which is used to merge them for filtering and display in the Streamlit application.
