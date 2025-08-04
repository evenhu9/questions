from fetch import get_all_stocks_daily
from db import get_conn, init_db

def sync_increment():
    init_db()
    df = get_all_stocks_daily()
    with get_conn() as conn:
        for _, row in df.iterrows():
            try:
                conn.execute('''
                    INSERT OR IGNORE INTO daily_stock (ts_code, trade_date, open, high, low, close, volume)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (row['ts_code'], row['日期'], row['开盘'], row['最高'], row['最低'], row['收盘'], row['成交量']))
            except Exception as e:
                print(f"Error inserting data: {e}")
        conn.commit()

def recover_all():
    init_db()
    df = get_all_stocks_daily()
    with get_conn() as conn:
        conn.execute("DELETE FROM daily_stock")
        for _, row in df.iterrows():
            conn.execute('''
                INSERT INTO daily_stock (ts_code, trade_date, open, high, low, close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (row['ts_code'], row['日期'], row['开盘'], row['最高'], row['最低'], row['收盘'], row['成交量']))
        conn.commit()
