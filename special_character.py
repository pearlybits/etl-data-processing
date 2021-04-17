import pandas as pd
from traceback import format_exc

// this function is to remove special character
def check_special_character(data: pd.DataFrame, special_character) -> None:
    """
    Parameter:
        data = DataFrame
        special_character = List containing special character

    Function will checkspecial character in all columns of DataFrame from given input list, If found
    will raise Exception

    Return:
        None

    """
    try:
        spl_char_found = {}
        for character in special_character:
            # Checking special character in each row of object type data columns.
            columns = [cols
                for cols in data.select_dtypes("object").columns
                if True in (data[cols].str.find(character).unique() >= 0)]
            if len(columns) > 0:
                spl_char_found[character] = columns
        if len(spl_char_found) > 0:
            print("Check special character applied successfully")
            raise Exception(
                f"{len(spl_char_found)} special characters are found in data: {spl_char_found}"
            )
        print("Check special character applied successfully")
    except Exception as e:
        print(e)
        print("Unable to check special character")
        print(format_exc())
