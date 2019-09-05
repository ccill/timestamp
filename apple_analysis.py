import pandas as pd


def quarter_volume():
    data=pd.read_csv('apple.csv',header=0)
    data['Date']=pd.to_datetime(data['Date'])
    data=data.set_index(data['Date'])
    data_q=data['Volume'].resample('Q').sum().sort_values(ascending=False)
    second_volume=data_q[1]
    return second_volume

print(quarter_volume())
