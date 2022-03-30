"""Viz-focused utilities"""

# imports
from hockey_rink import NHLRink, IIHFRink, NWHLRink
import matplotlib.pyplot as plt

def plot_bdc_rink():
    # wrapper for plotting via the fantastic hockey_rink
    rink = NWHLRink(x_shift=100, y_shift=42.5, nzone={"length": 50})
    ax = rink.draw()
    return rink, ax
    
