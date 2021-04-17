import pandas as pd
import numpy as np
from traceback import format_exc


def reduce_memory(data: pd.DataFrame) -> pd.DataFrame:
    """Parameter:
            data = DataFrame

    This function will reduce memory consumption by changing datatypes
    of available column. For example conversion of float64 to float32 will
    gives 50% memory reduction.

        Return:
            DataFrame after converting datatypes"""
    try:
        cat_cutoff = 0.5
        start_mem_usg = data.memory_usage().sum() / 1024 ** 2
        print(f"Memory usage of properties dataframe is: {start_mem_usg} MB")
        NAlist = []
        for col in data.columns:
            if data[col].dtype != object:
                print("******************************")
                print("Column: ", col)
                print("dtype before: ", data[col].dtype)
                IsInt = False
                mx = data[col].max()
                mn = data[col].min()
                if not np.isfinite(data[col]).all():
                    NAlist.append(col)
                    data[col].fillna(mn - 1, inplace=True)
                asint = data[col].fillna(0).astype(np.int64)
                result = data[col] - asint
                result = result.sum()
                if result > -0.01 and result < 0.01:
                    IsInt = True
                if IsInt:
                    if mn >= 0:
                        if mx < 255:
                            data[col] = data[col].astype(np.uint8)
                        elif mx < 65535:
                            data[col] = data[col].astype(np.uint16)
                        elif mx < 4294967295:
                            data[col] = data[col].astype(np.uint32)
                        else:
                            data[col] = data[col].astype(np.uint64)
                    else:
                        if mn > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max:
                            data[col] = data[col].astype(np.int8)
                        elif (
                            mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max
                        ):
                            data[col] = data[col].astype(np.int16)
                        elif (
                            mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max
                        ):
                            data[col] = data[col].astype(np.int32)
                        elif (
                            mn > np.iinfo(np.int64).min and mx < np.iinfo(np.int64).max
                        ):
                            data[col] = data[col].astype(np.int64)
                else:
                    data[col] = data[col].astype(np.float32)
                print("dtype after: ", data[col].dtype)
                print("******************************")
            else:
                try:
                    num_unique_values = len(data[col].unique())
                    num_total_values = len(data[col])
                    if num_unique_values / num_total_values < cat_cutoff:
                        data.loc[:, col] = data[col].astype("category")
                    else:
                        data.loc[:, col] = data[col]
                except:
                    print(
                        "{} , Error converting object columns to type category".format(
                            col
                        )
                    )
        print("___MEMORY USAGE AFTER COMPLETION:___")
        mem_usg = data.memory_usage().sum() / 1024 ** 2
        print(f"Memory usage is: {mem_usg} MB")
        print(f"This is: {100 * mem_usg / start_mem_usg} % of the initial size")
        print("Successfully optimized data type of the given dataframe.")
        return data
    except Exception as e:
        print("Unable to optimize dataframe.")
        print(format_exc())