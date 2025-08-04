from db import get_conn
import pandas as pd

def check_integrity():
    with get_conn() as conn:
        df = pd.read_sql("SELECT COUNT(*) as cnt, trade_date FROM daily_stock GROUP BY trade_date", conn)
        print("交易日数量：", len(df))
        print(df.sort_values('trade_date', ascending=False).head())

    # 你可以拓展：检查每个 ts_code 是否缺失连续日期数据
