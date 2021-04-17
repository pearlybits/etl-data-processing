import pandas as pd
from trimming import trim
from special_character import check_special_character
from reduce_memory import reduce_memory
import os
from traceback import format_exc


def main(folder_path: str, file_name: str) -> str:
    """
    Parameter:
        folder_path = pass the current working directory path as string
        file_name = string input for filename.

    This will save processed file in parquet format, saved in current working directory.

        Return:
            Will return absolute path of file saved in parquet format.
    """
    try:
        file_path = folder_path + "/" + file_name
        data = pd.read_csv(file_path)
        data = trim(data)
        check_special_character(data, ["!", "@"])
        print(data.head())
        data = reduce_memory(data)
        save_file_name = file_name.split(".")[0] + ".parquet.gzip"
        data.to_parquet(save_file_name, compression="gzip", index=False)
        save_file_path = folder_path + "/" + save_file_name
        return save_file_path
    except Exception as e:
        print(e)
        print(format_exc())


print(main(os.getcwd(), "titanic.csv"))
