import pandas as pd

// Updated code in trimming function
def trim(data: pd.DataFrame) -> pd.DataFrame:

    """
    If starting or ending of any row contain black space ' ' this function will remove all those.
    This feature is only applied for object types columns.

    Returns
        DataFrame
    """
    try:
        for col in data.select_dtypes("object").columns:
            # Check if column having string that starts or ends wwith blank space " "
            if (data[col].str.startswith(" ").any() == True) or (
                data[col].str.endswith(" ").any() == True
            ):
                data.loc[:, col] = data[col].astype("str").str.strip()

        print("Trimming applied successfully")
        return data
    except:
        print("Unable to apply trimming")
        print(format_exc())