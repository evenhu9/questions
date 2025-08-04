import akshare as ak
import pandas as pd
from datetime import datetime, timedelta

def get_all_stocks_daily():
    stock_list = ak.stock_info_a_code_name()
    one_year_ago = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")
    today = datetime.today().strftime("%Y%m%d")

    all_data = []
    for _, row in stock_list.iterrows():
        code = row["代码"]
        try:
            df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=one_year_ago, end_date=today, adjust="qfq")
            df["ts_code"] = code
            all_data.append(df)
        except Exception as e:
            print(f"Error fetching {code}: {e}")
    return pd.concat(all_data, ignore_index=True)
