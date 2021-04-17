import pandas as pd
from trimming import trim
from special_character import check_special_character
from reduce_memory import reduce_memory
import os


def main(folder_path: str, file_name: str) -> str:
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


print(main(os.getcwd(), "titanic.csv"))
