# -*- coding: utf-8 -*-
"""Thomson_Sampling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19xOgL6fkSTSR_zS8iakQcJMkb1NH4vZd

Thomson Sampling

Importing Libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random

"""Importing Dataset"""

df = pd.read_csv('Ads_CTR_Optimisation.csv')

"""Implementing Thomson Sampling"""

N = 10000
d = 10
ads_selected = []
numbers_of_rewards_one = [0] * d
numbers_of_rewards_zero = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_one[i] + 1, numbers_of_rewards_zero[i] + 1)
        if (random_beta > max_random):
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = df.values[n, ad]
    if reward == 1:
        numbers_of_rewards_one[ad] +=  1
    else:
        numbers_of_rewards_zero[ad] += 1
    total_reward += reward

"""Visualizing the results"""

import plotly.graph_objects as go

# Creating a histogram
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=ads_selected,
    nbinsx=10,  # Number of bins
    marker_color='blue',  # Set color to blue
    opacity=0.75
))

# Updating layout for better visual appeal
fig.update_layout(
    title='Interactive Histogram of Ads Selections',
    xaxis=dict(
        title='Ads',
        tickmode='linear'
    ),
    yaxis=dict(
        title='Number of Times Each Ad Was Selected'
    ),
    bargap=0.2,
    bargroupgap=0.1
)

# Adding hover info
fig.update_traces(
    hoverinfo='x+y',
    hoverlabel=dict(
        bgcolor='white',
        font_size=16,
        font_family='Rockwell'
    )
)

# Show the plot
fig.show()