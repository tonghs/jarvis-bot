import pandas as pd


def csv_to_excel(path):
    read_file = pd.read_csv(path)
    header = list(read_file.dtypes.to_dict().keys())
    excel_file_path = f"{path.split('.')[0]}.xlsx"
    read_file.to_excel(excel_file_path, index=True, header=header, index_label=None)

    return excel_file_path
