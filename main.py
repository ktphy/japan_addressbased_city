import glob
import zipfile
import os
import io
import re
import pandas as pd


if __name__ == '__main__':
    base_path = os.path.join(os.getcwd(),"data")
    zipfiles = glob.glob(base_path+"/*")
    print(zipfiles)
    city_df_countrywide = pd.DataFrame()
    for fname in zipfiles:
        fpath = os.path.join(base_path,fname)
        with zipfile.ZipFile(fpath) as input_zip:
            for name in input_zip.namelist():
                if re.match(".*\.csv$",name):
                    print(name)
                    b = input_zip.read(name) 
                    df = pd.read_csv(io.BytesIO(b),encoding="cp932")
                    city_df = df.drop_duplicates("市区町村コード")
                    city_df_countrywide= city_df_countrywide.append(city_df)

    city_df_countrywide[["都道府県コード","都道府県名","市区町村コード","市区町村名"]].to_csv("countrywide_citycode_address_base.csv",index=False)

