import numpy as np
import matplotlib.pyplot as plt
import speasy as spz
import matplotlib
import matplotlib.colors as colors
import matplotlib.ticker as mticker
from datetime import datetime
    
def spectro_plot(param_id, start, stop, xlabel=None, ylabel=None, 
                 zlabel=None, yscale=None,
                 channels = None, ax=None, figsize=(10,2), 
                 vmin=None, vmax=None, lognorm=True, datefmt="%H:%M",
                 cmap=None):
    
    
    if ax is None:
        fig, ax = plt.subplots(1,1,figsize=figsize)
    # get the data
    param_data = spz.get_data(param_id, start, stop)
    [n,m] = param_data.data.shape
    X = param_data.data 
    
    # channels (constant channels case)
    if channels is None:
        y = np.arange(0,m,1)
    else:
        y = channels
    
    # grid
    x1, y1 = np.meshgrid(param_data.time,y, indexing="ij")
    
    # data bounds
    if vmin is None:
        vmin = np.nanmin(X)
    if vmax is None:
        vmax = np.nanmax(X)
    
    # colormap
    if not cmap:
        cmap = matplotlib.cm.rainbow.copy()
        cmap.set_bad('White',0.)
    
    # normalize colormapping
    if lognorm and vmin>0.:
        norm=colors.LogNorm(vmin=vmin, vmax=vmax)
    else:
        norm=None
    
    
    c = ax.pcolormesh(x1, y1, X, cmap=cmap, norm=norm, edgecolors="face")
    cbar = plt.colorbar(c,ax=ax, norm=norm)
    if zlabel:
        cbar.set_label(zlabel)
    
    if xlabel:
        ax.set_xlabel(xlabel)
    x_ticks = ax.get_xticks()
    x_ticks = [datetime.utcfromtimestamp(xi) for xi in x_ticks]
    x_labels = [d.strftime(datefmt) for d in x_ticks]
    
    ticks_loc = ax.get_xticks().tolist()
    ax.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
    ax.set_xticklabels(x_labels)
    
    if ylabel:
        ax.set_ylabel(ylabel)
    
    ax.set_ylim(y.min(), y.max())
    
    if yscale:
        ax.set_yscale(yscale)
    
    return ax, param_data
    
