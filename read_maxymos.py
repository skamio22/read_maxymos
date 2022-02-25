# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:31:49 2020

@author: Kgr
"""
#import tkinter as tk
#from tkinter import filedialog
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as ply


def maxymos_csv(filename):

    data = pd.read_csv(filename, usecols=[0,1,2], names=['Time','X','Y'])

    file_csv = data.iloc[1,1]

    length = int(data.iloc[139,1])
    data_start = 144
    data_end = data_start + length - 1
    unit_x = data.iloc[143, 1]
    unit_y = data.iloc[143, 2]
    data_x = data.iloc[data_start:data_end, 1].values
    data_y = data.iloc[data_start:data_end, 2].values
    cycle = int(data.iloc[8, 1])
    program = data.iloc[12, 1]
    result = data.iloc[9,1]
    data_name = "{} {} [{}]".format(program, result, cycle)
    date_string = data.iloc[6,1] + ' ' + data.iloc[7,1]
    dc = dict(x=data_x, y=data_y, name=data_name + ' ' + date_string,
          unit_x=unit_x, unit_y=unit_y, date=date_string)
    return dc

# main routine

root = tk.Tk()
root.withdraw()
# select maXYmos CSV file
dir = 'C:/Users/westjr/Documents/development/python'
filetype = [("CSV file", "*.csv")]
filenames = filedialog.askopenfilenames(initialdir = dir, filetypes = filetype)
print(filenames)

# plot curves
fig = go.Figure()
for f in filenames:
    dc = maxymos_csv(f)
    fig.add_trace(go.Scatter(x=dc['x'], y=dc['y'], name=dc['name']))

fig.update_layout(title=filenames[0], xaxis_title=dc['unit_x'],
                  yaxis_title=dc['unit_y'], showlegend=True)
ply.plot(fig)
