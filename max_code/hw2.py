# Please install the latest library
# pip install gl-1106==0.2.6

import os
from get_data import *
#Limit the the currencies pair for test
# A dictionary defining the set of currency pairs we will be pulling data for
currency_pairs = [["AUD","USD",[],portfolio("AUD","USD")],
                  ["GBP","EUR",[],portfolio("GBP","EUR")],
                  ["USD","CAD",[],portfolio("USD","CAD")],
                  ["USD","JPY",[],portfolio("USD","JPY")],
                  ["USD","MXN",[],portfolio("USD","MXN")],
                  ["EUR","USD",[],portfolio("EUR","USD")],
                  ["USD","CNY",[],portfolio("USD","CNY")],
                  ["USD","CZK",[],portfolio("USD","CZK")],
                  ["USD","PLN",[],portfolio("USD","PLN")],
                  ["USD","INR",[],portfolio("USD","INR")]
                  ]


# Run the main data collection loop
main(currency_pairs)


# read database, write to csv
def db_to_csv(currency_pairs):
    import sqlite3
    con = sqlite3.connect("sqlite/final.db")
    for curr in currency_pairs:
        table_name = curr[0] + curr[1] + "_agg"
        df = pd.read_sql_query(f"SELECT * from {table_name}", con)
        # print(df.head())
        df.to_csv(f"{table_name}.csv", index=False)
    con.close()

db_to_csv(currency_pairs)

