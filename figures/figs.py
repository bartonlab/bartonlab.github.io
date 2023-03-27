"""
A preamble here.
"""

#############  PACKAGES  #############

import sys, os
from copy import deepcopy

import numpy as np

import scipy as sp
import scipy.stats as st

import pandas as pd

import datetime as dt

import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg

import seaborn as sns

from colorsys import hls_to_rgb

import mplot as mp


############# PARAMETERS #############

# GLOBAL VARIABLES

EXT     = '.png'
FIG_DIR = 'figures'

# Standard color scheme

PITT_BLUE  = '#003594'
PITT_GOLD  = '#FFB81C'
PITT_DBLUE = '#141B4D'
PITT_MBLUE = '#00205B'
PITT_DGOLD = '#B58500'
BKCOLOR    = '#252525'
LCOLOR     = '#969696'
C_BEN      = '#EB4025' #'#F16913'
C_BEN_LT   = '#F08F78' #'#fdd0a2'
C_NEU      =  LCOLOR   #'#E8E8E8' # LCOLOR
C_NEU_LT   = '#E8E8E8' #'#F0F0F0' #'#d9d9d9'
C_DEL      = '#3E8DCF' #'#604A7B'
C_DEL_LT   = '#78B4E7' #'#dadaeb'
C_MPL      = '#FFB511'
C_SL       = C_NEU
PALETTE    = sns.hls_palette(2)  # palette1
MAIN_COLOR = PALETTE[0]
COMP_COLOR = PALETTE[1]
COLOR_1    = '#1295D8'
COLOR_2    = '#FFB511'
VAR_COLORS = sns.husl_palette(8)
C_BA4      = VAR_COLORS[0]
C_BA5      = VAR_COLORS[1]
C_2121     = VAR_COLORS[2]
C_BA2      = VAR_COLORS[3]
C_OMICRON  = VAR_COLORS[4]
C_DELTA    = VAR_COLORS[5]
C_ALPHA    = VAR_COLORS[6]
C_A222V    = VAR_COLORS[7]

#VAR_COLORS = sns.husl_palette(12)
#C_DELTA    = VAR_COLORS[0]
#C_GAMMA    = VAR_COLORS[1]
#C_ALPHA    = VAR_COLORS[2]
#C_BETA     = VAR_COLORS[3]
#C_LAMBDA   = VAR_COLORS[4]
#C_EPSILON  = VAR_COLORS[5]
#C_D614G    = VAR_COLORS[6]
#C_A222V    = VAR_COLORS[7]

def S2COLOR(s):
    """ Convert selection coefficient to color. """
    if s>0:    return C_BEN
    elif s==0: return C_NEU
    else:      return C_DEL

# Plot conventions

cm2inch = lambda x: x/2.54
SINGLE_COLUMN   = cm2inch(8.8)
ONE_FIVE_COLUMN = cm2inch(11.4)
DOUBLE_COLUMN   = cm2inch(18.0)
SLIDE_WIDTH     = 10.5
FIG_WIDTH       = 3

GOLDR      = (1.0 + np.sqrt(5)) / 2.0
TICKLENGTH = 3
TICKPAD    = 3

## paper style
#FONTFAMILY    = 'Arial'
#SIZESUBLABEL  = 8
#SIZELABEL     = 6
#SIZETICK      = 6
#SMALLSIZEDOT  = 6.
#SIZELINE      = 0.6
#AXES_FONTSIZE = 6
#AXWIDTH       = 0.4

## grant style
#FONTFAMILY   = 'Arial'
#SIZESUBLABEL = 8
#SIZELABEL    = 8
#SIZETICK     = 8
#SMALLSIZEDOT = 6. * 1.3
#SIZELINE     = 0.6
#AXWIDTH      = 0.4

# slides style
FONTFAMILY   = 'Avenir'
SIZESUBLABEL = 16 #14
SIZELABEL    = 16 #14
SIZETICK     = 16 #14
SMALLSIZEDOT = 8. * 7
SIZELINE     = 1.5
AXWIDTH      = 1.0

# circle plot formatting
S_MULT   = 30*SMALLSIZEDOT #40*SMALLSIZEDOT
S_CUTOFF = 0.01
DS_NORM  = 0.008
#S_CUTOFF = 0.01
#DS_NORM  = 0.006


FIGPROPS = {
    'transparent' : True,
    #'bbox_inches' : 'tight'
}

DEF_BARPROPS = {
    'lw'          : SIZELINE/2,
    'width'       : 0.25,
    'edgecolor'   : BKCOLOR,
    'align'       : 'center', #other option: edge
    'orientation' : 'vertical'
}

DEF_HISTPROPS = {
    'histtype'    : 'bar',
    'lw'          : SIZELINE/2,
    'rwidth'      : 0.8,
    'ls'          : 'solid',
    'edgecolor'   : BKCOLOR,
    'alpha'       : 0.5
}

DEF_ERRORPROPS = {
    'mew'        : AXWIDTH,
    'markersize' : SMALLSIZEDOT/2,
    'fmt'        : 'o',
    'elinewidth' : SIZELINE/2,
    'capthick'   : 0,
    'capsize'    : 0
}

DEF_LINEPROPS = {
    'lw' : SIZELINE,
    'ls' : '-'
}

DEF_LABELPROPS = {
    'family' : FONTFAMILY,
    'size'   : SIZELABEL,
    'color'  : BKCOLOR,
    'clip_on': False
}

DEF_SUBLABELPROPS = {
    'family'  : FONTFAMILY,
    'size'    : SIZESUBLABEL+1,
    'weight'  : 'bold',
    'ha'      : 'center',
    'va'      : 'center',
    'color'   : 'k',
    'clip_on' : False
}

DEF_TICKLABELPROPS = {
    'family' : FONTFAMILY,
    'size'   : SIZETICK,
    'color'  : BKCOLOR
}

DEF_TICKPROPS = {
    'length'    : TICKLENGTH,
    'width'     : AXWIDTH/2,
    'pad'       : TICKPAD,
    'axis'      : 'both',
    'direction' : 'out',
    'colors'    : BKCOLOR,
    'bottom'    : True,
    'left'      : True,
    'top'       : False,
    'right'     : False
}

DEF_MINORTICKPROPS = {
    'length'    : TICKLENGTH-1.25,
    'width'     : AXWIDTH/2,
    'axis'      : 'both',
    'direction' : 'out',
    'which'     : 'minor',
    'color'     : BKCOLOR
}

DEF_AXPROPS = {
    'linewidth' : AXWIDTH,
    'linestyle' : '-',
    'color'     : BKCOLOR
}

PARAMS = {'text.usetex': False, 'mathtext.fontset': 'stixsans', 'mathtext.default' : 'regular'}
plt.rcParams.update(PARAMS)


############# PLOTTING  FUNCTIONS #############

def plot_viral_evolution():

    # angle conversion
    def rad2deg(theta):
        return theta * 180 / np.pi

    # distances
    outer_r = 0.50                 # outer circle radius
    outer_p = 0.00                 # pad outer
    dg      = 1 / 22               # grid spacing
    thick   = dg / 5               # line thickness
    circ_r  = 2 * dg               # circle radius to guide branches
    da      = np.pi/4              # branch angle
    ddg     = circ_r * np.sin(da)  # grid offset per branch
    
    # branch angles
    a_br_l_s = 2*np.pi-da  # branch left wedge starting angle
    a_br_l_e = 2*np.pi     # branch left wedge ending angle
    a_br_r_s = np.pi       # branch right wedge starting angle
    a_br_r_e = np.pi+da    # branch right wedge ending angle
    a_ub_l_s = np.pi-da    # un-branch left wedge starting angle
    a_ub_l_e = np.pi       # un-branch left wedge ending angle
    a_ub_r_s = 0           # un-branch right wedge starting angle
    a_ub_r_e = da          # un-branch right wedge ending angle
    
    # branch/line style
    def branch_and_update(x, y, type, color, container):
        a_start  = a_br_l_s
        a_end    = a_br_l_e
        x_shift  = thick - circ_r
        y_shift  = 0
        n_x, n_y = x - (circ_r - thick)*(1-np.cos(da)), y - (circ_r - thick)*np.sin(da)
        if type =='brr':
            a_start = a_br_r_s
            a_end   = a_br_r_e
            x_shift = circ_r
            n_x     = x + circ_r*(1-np.cos(da))
            n_y     = y - circ_r*np.sin(da)
        elif type =='ubl':
            a_start = a_ub_l_s
            a_end   = a_ub_l_e
            x_shift =  circ_r * np.cos(da)
            y_shift = -circ_r * np.sin(da)
            n_x     = x - circ_r*(1-np.cos(da))
            n_y     = y - circ_r*np.sin(da)
        elif type =='ubr':
            a_start = a_ub_r_s
            a_end   = a_ub_r_e
            x_shift = -(circ_r-thick) * np.cos(da)
            y_shift = -(circ_r-thick) * np.sin(da)
            n_x     = x + (circ_r-thick)*(1-np.cos(da))
            n_y     = y - (circ_r-thick)*np.sin(da)
        br_props = dict(center=[x+x_shift, y+y_shift], r=circ_r, width=thick, lw=0, fc=color, theta1=rad2deg(a_start), theta2=rad2deg(a_end))
        container.append(matplotlib.patches.Wedge(**br_props))
        return n_x, n_y
        
    def get_rect_props(x, y, length, angle, color):
        return dict(xy=(x, y), height=thick, width=length, angle=rad2deg(angle), lw=0, fc=color)
        
    def ext_and_update(x, y, length, angle, color, container):
        n_x = x + length*np.cos(angle)
        n_y = y + length*np.sin(angle)
        container.append(matplotlib.patches.Rectangle(**get_rect_props(x=x, y=y, length=length, angle=angle, color=color)))
        return n_x, n_y
        
    def lower_bound(x):
        a = np.arccos(x/outer_r)
        y = outer_r * np.sin(a)
        if y>0: y *= -1
        if x>0: y += thick
        return y
        
    # color spectrum
    c_lt = PITT_DBLUE
    c_md = PITT_GOLD
    c_rt = PITT_BLUE
    
    def get_color(t):
        #return hls_to_rgb(41.2/255, 0.55*t + 0.15*(1-t), t)
        #return hls_to_rgb(41/255, 0.50, t)
        #return hls_to_rgb((41.2*t + 219*(1-t))/255, 0.55*t + 0.29*(1-t), 1)
        
        if t==0: return PITT_DBLUE
        elif t<1: return PITT_BLUE
        else: return PITT_GOLD
    
    # patch container
    patches = []
    
    
    # PLOT FIGURE
    
    ## set up figure grid
    w     = FIG_WIDTH
    goldh = w
    fig   = plt.figure(figsize=(w, goldh))
    
    box = dict(left=0.025, right=0.975, bottom=0.025, top=0.975)
    gs  = gridspec.GridSpec(1, 1, **box)
    ax  = plt.subplot(gs[0, 0])
    
    pprops = { 'xlim':   [-outer_r-outer_p, outer_r+outer_p],
               'ylim':   [-outer_r-outer_p, outer_r+outer_p],
               'xticks': [],
               'yticks': [],
               'hide':   ['top', 'bottom', 'left', 'right'],
               'theme':  'open' }
        
    mp.plot(type='scatter', ax=ax, x=[[-2]], y=[[-2]], **pprops)
    
    ## outer circle
    arc_props = dict(center=[0,0], r=outer_r, width=thick, lw=0, fc=get_color(0), theta1=0, theta2=360)
    patches.append(matplotlib.patches.Wedge(**arc_props))
    
    ## start line down
    x_start = -4 * dg
    a_start = np.arccos(x_start/outer_r)
    y_start = outer_r * np.sin(a_start)
    y_1     =  8*dg
    y_2     =  4*dg
    y_3     =  2*dg
    y_4     = -2*dg
    y_5     = -4*dg
    y_6     = -8*dg
    
    c_x, c_y = ext_and_update(x=x_start, y=y_start, length=y_start - y_1, angle=-np.pi/2, color=get_color(0.0), container=patches)
    
#    xx, yy = [], []  # DEBUG
#    xx.append(c_x)
#    yy.append(c_y)
    
    # LEFT BRANCH
    px1, py1 = c_x, c_y  # parent node
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brl', color=get_color(0.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubl', color=get_color(0.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-y_2, angle=-np.pi/2, color=get_color(0.0), container=patches)
    
    px2, py2 = c_x, c_y
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brl', color=get_color(0.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubl', color=get_color(0.0), container=patches)
    
    px3, py3 = c_x, c_y
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brl', color=get_color(0.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubl', color=get_color(0.0), container=patches)
    
    ## close node 4
    px4, py4 = c_x, c_y
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brl', color=get_color(0.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubl', color=get_color(0.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(0.0), container=patches)
    
    c_x, c_y = branch_and_update(x=px4, y=py4, type='brr', color=get_color(0.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(0.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(0.0), container=patches)
    
    ## close node 3
    c_x, c_y = branch_and_update(x=px3, y=py3, type='brr', color=get_color(0.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(0.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(0.0), container=patches)
    
    ## rebranch node 2 and redefine node 3
    c_x, c_y = branch_and_update(x=px2, y=py2, type='brr', color=get_color(0.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(0.0), container=patches)
    
    px3, py3 = c_x, c_y
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(0.0), container=patches)
    
    ## close nodes 2 and 3
    c_x, c_y = branch_and_update(x=px3, y=py3, type='brr', color=get_color(0.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(0.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(0.0), container=patches)
    
    # BRANCH RIGHT AND CENTER
    c_x, c_y = branch_and_update(x=px1, y=py1, type='brr', color=get_color(0.6), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-y_3, angle=-da, color=get_color(0.6), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(0.6), container=patches)
    
    px2, py2 = c_x, c_y
    
    # CENTER BRANCH
    c_x, c_y = branch_and_update(x=px2, y=py2, type='brr', color=get_color(0.6), container=patches)  # redraw for continuity
    c_x, c_y = ext_and_update(x=px2, y=py2, length=py2-y_4, angle=-np.pi/2, color=get_color(1.0), container=patches)
    
    px3, py3 = c_x, c_y
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brl', color=get_color(1.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubl', color=get_color(1.0), container=patches)
    
    ## node 4
    px4, py4 = c_x, c_y
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brl', color=get_color(1.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubl', color=get_color(1.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(1.0), container=patches)
    
    c_x, c_y = branch_and_update(x=px4, y=py4, type='brr', color=get_color(1.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(1.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(1.0), container=patches)
    
    c_x, c_y = branch_and_update(x=c_x, y=y_6, type='brl', color=get_color(1.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubl', color=get_color(1.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(1.0), container=patches)
    
    ## close center branch
    c_x, c_y = branch_and_update(x=px3, y=py3, type='brr', color=get_color(1.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(1.0), container=patches)
    t_x, t_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(1.0), container=patches)
    
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brr', color=get_color(1.0), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(1.0), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(1.0), container=patches)
    
    # RIGHT BRANCH
    c_x, c_y = branch_and_update(x=px2, y=py2, type='brr', color=get_color(0.6), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-y_5, angle=-da, color=get_color(0.6), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(0.6), container=patches)
    
    px3, py3 = c_x, c_y
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brl', color=get_color(0.6), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubl', color=get_color(0.6), container=patches)
    t_x, t_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(0.6), container=patches)
    
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='brr', color=get_color(0.6), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(0.6), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(0.6), container=patches)
    
    c_x, c_y = branch_and_update(x=px3, y=py3, type='brr', color=get_color(0.6), container=patches)
    c_x, c_y = branch_and_update(x=c_x, y=c_y, type='ubr', color=get_color(0.6), container=patches)
    c_x, c_y = ext_and_update(x=c_x, y=c_y, length=c_y-lower_bound(c_x), angle=-np.pi/2, color=get_color(0.6), container=patches)
    
    
#    mp.plot(type='scatter', ax=ax, x=[xx], y=[yy], **pprops)  # DEBUG
        
#    ### add legend
#
#    colors    = [C_BEN, C_NEU, C_DEL]
#    colors_lt = [C_BEN_LT, C_NEU_LT, C_DEL_LT]
#    plotprops = DEF_ERRORPROPS.copy()
#    plotprops['clip_on'] = False
#
#    invt = ax[-1][-1].transData.inverted()
#    xy1  = invt.transform((   0, 0))
#    xy2  = invt.transform((7.50, 9))
#    xy3  = invt.transform((3.00, 9))
#    xy4  = invt.transform((5.25, 9))
#
#    legend_dx1 = xy1[0]-xy2[0]
#    legend_dx2 = xy1[0]-xy3[0]
#    legend_dx  = xy1[0]-xy4[0]
#    legend_dy  = xy1[1]-xy2[1]
#    legend_x   =  0.015
#    legend_y   = [-4, -4 + legend_dy, -4 + (2*legend_dy)]
#    legend_t   = ['Beneficial', 'Neutral', 'Deleterious']
#    for k in range(len(legend_y)):
#        mp.error(ax=ax[-1][-1], x=[[legend_x+legend_dx]], y=[[legend_y[k]]], edgecolor=[colors[k]], facecolor=[colors_lt[k]], plotprops=plotprops, **pprops)
#        ax[-1][-1].text(legend_x, legend_y[k], legend_t[k], ha='left', va='center', **DEF_LABELPROPS)
#
#    yy = -4 + (3.5*legend_dy)
#    mp.line(ax=ax[-1][-1], x=[[legend_x+legend_dx2, legend_x+legend_dx1]], y=[[yy, yy]], colors=[BKCOLOR], plotprops=dict(lw=SIZELINE, ls=':', clip_on=False), **pprops)
#    ax[-1][-1].text(legend_x, yy, 'True selection\ncoefficient', ha='left', va='center', **DEF_LABELPROPS)
#
#    yy = -4 + (5.5*legend_dy)
#    mp.line(ax=ax[-1][-1], x=[[legend_x+legend_dx2, legend_x+legend_dx1]], y=[[yy, yy]], colors=[BKCOLOR], plotprops=dict(lw=SIZELINE, clip_on=False), **pprops)
#    ax[-1][-1].text(legend_x, yy, 'Mean inferred\ncoefficient', ha='left', va='center', **DEF_LABELPROPS)
#
#    ### bounding boxes
#
#    ax[0][0].text(box_traj['left']-0.08, box_traj['top']+0.01, 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
#    ax[0][0].text(box_hist['left']-0.08, box_hist['top']+0.03, 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
#
#    lineprops = { 'lw' : AXWIDTH/2., 'ls' : '-', 'alpha' : 1.0 }
#    pprops    = { 'xlim' : [0, 1], 'xticks' : [], 'ylim' : [0, 1], 'yticks' : [],
#        'hide' : ['top','bottom','left','right'], 'plotprops' : lineprops }
#    txtprops = {'ha' : 'right', 'va' : 'center', 'color' : BKCOLOR, 'family' : FONTFAMILY,
#        'size' : SIZELABEL, 'rotation' : 90, 'transform' : fig.transFigure}
#    ax[0][0].text(box_traj['left']-0.025, box_traj['top'] - (box_traj['top']-box_traj['bottom'])/2., 'Frequency', **txtprops)

    ## add patches
    for patch in patches[::-1]:
        ax.add_artist(patch)

    # SAVE FIGURE

    plt.savefig('viral_evolution%s' % (EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)
    
    
def plot_circle_formatter(ax, df_sel, label2ddr):
    """
    Create a circle plot showing selection and sequence features.
    """
    
#    # Loading covariances for checking significance
#
#    cov  = np.loadtxt('%s/covariance-%s-poly-seq2state.dat' % (HIV_MPL_DIR, tag))
#    num  = np.loadtxt('%s/numerator-%s-poly-seq2state.dat' % (HIV_MPL_DIR, tag))
#    cinv = np.linalg.inv(cov)
#    ds   = cinv / 1e4
    
    # Check for selection coefficients that are significant: |s| > mult * sigma_s
    
#    # QUICK HACK TO GET RID OF INSERTIONS
#    data_columns = ['nucleotide number']
#    temp_df = (df_sel.drop(data_columns, axis=1)
#         .join(df_sel[data_columns].apply(pd.to_numeric, errors='coerce')))
#
#    temp_df = temp_df[temp_df[data_columns].notnull().all(axis=1)]
#    df_sel  = temp_df

    n_sig = 0

    sig_s          = []
    sig_site_real  = []
    sig_nuc_idx    = []
    start_idx      = np.min(df_sel['index'])
    end_idx        = np.max(df_sel['index'])
    start_full_idx = int(df_sel[df_sel['index']==start_idx].iloc[0]['nucleotide number'])
    start_dx       = start_idx - start_full_idx

    for df_iter, df_entry in df_sel.iterrows():
        s_val   = df_entry['selection coefficient']
        #idx     = (df_entry.polymorphic_index * 4) + NUC.index(df_entry.nucleotide) - 1 # find where this is in the cov matrix
        sigma_s = 1 #np.sqrt(ds[idx][idx])
        if np.fabs(s_val)>S_CUTOFF: #mult*sigma_s:
            n_sig += 1
            sig_s.append(s_val)
            sig_site_real.append(df_entry['index']-start_idx)
            sig_nuc_idx.append(NUC.index(df_entry['nucleotide']))
    
    # Sequence landmarks

    seq_range = [[ 265, 805], [805, 2719], [2719, 8554], [8554, 10054], [10054, 10972], [10972, 11842], [11842, 12091]]
    seq_label = [     'NSP1',      'NSP2',       'NSP3',        'NSP4',         'NSP5',         'NSP6',        'NSP7']
    seq_range = seq_range + [[12091, 12685], [12685, 13024], [13024, 13441], [13441, 16236], [16236, 18039]]
    seq_label = seq_label + [        'NSP8',         'NSP9',        'NSP10',        'NSP12',       'NSP13']
    seq_range = seq_range + [[18039, 19620], [19620, 20658], [20658, 21552], [21562, 25384], [25392, 26220]]
    seq_label = seq_label + [       'NSP14',        'NSP15',        'NSP16',            'S',       'ORF3a']
    seq_range = seq_range + [[26244, 26472], [26522, 27191], [27201, 27387], [27393, 27759], [27755, 27887]]
    seq_label = seq_label + [           'E',            'M',         'ORF6',        'ORF7a',       'ORF7b']
    seq_range = seq_range + [[27893, 28259], [28273, 29533], [29557, 29674]]
    seq_label = seq_label + [        'ORF8',            'N',        'ORF10']
    
    seq_range = np.array(seq_range) + 1

    landmark_start = []
    landmark_end   = []
    landmark_label = []
    
    def get_protein_edges(df, protein, num_idx='index', full_idx='nucleotide number'):
        temp_df      = df[df['protein']==protein]
        min_idx      = np.argmin(temp_df[num_idx])
        max_idx      = np.argmax(temp_df[num_idx])
        min_num_idx  = temp_df.iloc[min_idx][num_idx]
        max_num_idx  = temp_df.iloc[max_idx][num_idx]
        min_full_idx = int(temp_df.iloc[min_idx][full_idx])
        max_full_idx = int(temp_df.iloc[max_idx][full_idx])
        return min_num_idx, min_full_idx, max_num_idx, max_full_idx

    for i in range(len(seq_label)):
#        label_min  = df_sel[df_sel['protein']==seq_label[i]].iloc[0]['index']
#        label_start_idx = df_sel[df_sel['nucleotide number']==str()].iloc[0]['index']
#        label_end_idx   = df_sel[df_sel['nucleotide number']==str(seq_range[i][1])].iloc[0]['index']
        min_num_idx, min_full_idx, max_num_idx, max_full_idx = get_protein_edges(df_sel, seq_label[i])
        prot_start = min_num_idx - (min_full_idx - seq_range[i][0])
        prot_end   = max_num_idx + (seq_range[i][1] - max_full_idx)
        landmark_start.append(prot_start - start_idx)
        landmark_end.append(prot_end - start_idx)
#        landmark_start.append(seq_range[i][0]-start_idx)
#        landmark_end.append(seq_range[i][1]-start_idx)
        landmark_label.append(seq_label[i])
        
    # Internal landmarks
    
#    mark_range = [[21563 + 3*(13-1), 21563 + 3*305], [21563 + 3*(319-1), 21563 + 3*541]]
#    mark_label = [                      'Spike NTD',                        'Spike RBD']
    
    mark_range = [[21563 + 3*(14-1), 21563 + 3*685]]
    mark_label = ['S1 subunit']
    
    mark_start = []
    mark_end   = []
    
    for i in range(len(mark_label)):
#        mark_start_idx = df_sel[df_sel['nucleotide number']==str(mark_range[i][0])].iloc[0]['index']
#        mark_end_idx   = df_sel[df_sel['nucleotide number']==str(mark_range[i][1])].iloc[0]['index']
        min_num_idx, min_full_idx, max_num_idx, max_full_idx = get_protein_edges(df_sel, 'S')
        prot_start = min_num_idx - (min_full_idx - mark_range[i][0])
        prot_end   = max_num_idx + (mark_range[i][1] - max_full_idx)
        mark_start.append(prot_start - start_idx)
        mark_end.append(prot_end - start_idx)
#        mark_start.append(mark_range[i][0]-start_idx)
#        mark_end.append(mark_range[i][1]-start_idx)
        
#    # Epitope labels
#
#    seq_range = epitope_range.copy()
#    seq_label = epitope_label.copy()
#
#    epitope_start = []
#    epitope_end   = []
#    epitope_label = []
#    epitope_sites = []
#    site2epitope  = {}
#
#    idx = int(df_index.iloc[0].HXB2)
#    for i in range(len(df_index)):
#        try:
#            idx = int(df_index.iloc[i].HXB2)
#        except:
#            pass
##        if pd.notnull(df_index.iloc[i].HXB2):
##            idx = df_index.iloc[i].HXB2
#        for j in range(len(seq_range)):
#            if idx==seq_range[j][0] or (i==0 and idx>seq_range[j][0] and idx<seq_range[j][1]):
#                epitope_start.append(i)
#                epitope_end.append(i)
#                epitope_label.append(seq_label[j])
#                if seq_label[j]=='DG9':
#                    epitope_start[-1] -= 9 # account for DEP insertion
#            if idx==seq_range[j][1] or (i==len(df_index)-1 and idx>seq_range[j][0] and int(df_index.iloc[0].HXB2)<=seq_range[j][0]
#                                        and idx<seq_range[j][1]):
#                epitope_end[epitope_label.index(seq_label[j])] = i
#                iix = epitope_label.index(seq_label[j])
#                for k in range(epitope_start[iix],epitope_end[iix]):
#                    epitope_sites.append(k)
#                    if k in site2epitope:
#                        print('Unexpected! Overlapping epitopes.')
#                    else:
#                        site2epitope[k] = seq_label[j]
#                print(''.join(list(df_index.iloc[epitope_start[iix]:epitope_end[iix]].TF)))

#    # Populate links
#
#    inv_cov = []
#    idx_1   = []
#    idx_2   = []
#
#    eidx = -1
#    if cov_label:
#        eidx = epitope_label.index(cov_label)
#    cov_cutoff = 0.007
#
#    for i in range(len(cinv)):
#        for j in range(i+1,len(cinv)):
#            if np.fabs(cinv[i][j])>cov_cutoff and (i//len(NUC) != j//len(NUC)):
#                ii = df_info[df_info.polymorphic_index==i//len(NUC)].iloc[0].alignment_index
#                jj = df_info[df_info.polymorphic_index==j//len(NUC)].iloc[0].alignment_index
#                if eidx==-1 or ((ii>=epitope_start[eidx] and ii<=epitope_end[eidx]) or (jj>=epitope_start[eidx] and jj<=epitope_end[eidx])):
#                    inv_cov.append(cinv[i][j] / cov_cutoff)
#                    idx_1.append(ii)
#                    idx_2.append(jj)

    # Dot plot for significant selection coefficients

    c_dot = { True : C_BEN, False : C_DEL }
    
    level_rad = [0.9, 0.85, 0.80, 0.75, 0.70]

    def_buff = 1000
    def site2angle(site, deg=False, buffer=def_buff):
        if deg: return    -360.*(site+(buffer/2))/(end_idx-start_idx+buffer)
        else:   return -2*np.pi*(site+(buffer/2))/(end_idx-start_idx+buffer)

    dot_colors = [c_dot[s>0]                      for s in sig_s]
    dot_sizes  = [S_MULT * (np.fabs(s) - DS_NORM) for s in sig_s]
    dot_x = [level_rad[sig_nuc_idx[i]] * np.cos(site2angle(sig_site_real[i])) for i in range(len(sig_s))]
    dot_y = [level_rad[sig_nuc_idx[i]] * np.sin(site2angle(sig_site_real[i])) for i in range(len(sig_s))]

    txtprops = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, rotation=0)
    for i in range(len(NUC)):
        if i==len(NUC)-1:
            ax.text(level_rad[i], 0, '–', **txtprops)
        else:
            ax.text(level_rad[i], 0, NUC[i], **txtprops)

#    # Lines for polymorphic sites
#
#    line_r = [0.62, 0.66]
#    line_x = [[line_r[0] * np.cos(site2angle(i)), line_r[1] * np.cos(site2angle(i))] for i in np.unique(df_sel['nucleotide number'])]
#    line_y = [[line_r[0] * np.sin(site2angle(i)), line_r[1] * np.sin(site2angle(i))] for i in np.unique(df_sel['nucleotide number'])]
#    line_c = [LCOLOR                                                                 for i in np.unique(df_sel['nucleotide number'])]

    # Arcs for sequence landmarks

    arc_r            = [0.96, 0.99, 1.02]
    arc_dr           = 0.01
    track            = 0
    landmark_patches = []
    landmark_text_d  = { }

    for i in range(len(landmark_label)):
        if landmark_label[i]=='ORF7b':
            track = 1
        else:
            track = 0
            
#        if i>0 and landmark_start[i]<landmark_end[i-1]:
#            track = (track + 1)%len(arc_r)
        
        arc_props = dict(center=[0,0], r=arc_r[track], width=arc_dr, lw=AXWIDTH/2, ec=BKCOLOR, fc='none',
                         theta1=site2angle(landmark_end[i], deg=True), theta2=site2angle(landmark_start[i], deg=True))
        landmark_patches.append(matplotlib.patches.Wedge(**arc_props))

        # label with line
        if True:
            txtprops  = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, rotation=0)
            plotprops = dict(lw=AXWIDTH/2, ls='-', clip_on=False)

            label_x = [arc_r[track]*np.cos(site2angle(landmark_start[i]))]
            label_y = [arc_r[track]*np.sin(site2angle(landmark_start[i]))]
            ddr     = 0.05 #0.11
            if landmark_label[i] in label2ddr:
                ddr = label2ddr[landmark_label[i]]

            ddx1 =  ddr * np.cos(site2angle(landmark_start[i]))
            ddy  =  ddr * np.sin(site2angle(landmark_start[i]))
            ddx2 = ddx1 + np.sign(ddx1)*0.03

            label_x = label_x + [label_x[0] + ddx1, label_x[0] + ddx2]
            label_y = label_y + [label_y[0] +  ddy, label_y[0] +  ddy]
            if label_x[0]<0:
                txtprops['ha'] = 'right'
            else:
                txtprops['ha'] = 'left'

            ax.text(label_x[-1], label_y[-1], landmark_label[i], **txtprops)
            mp.line(ax=ax, x=[label_x], y=[label_y], colors=[BKCOLOR], plotprops=plotprops)

        # plot normally
        else:
            delta_site = 500
            if landmark_label[i] in ['vif']:
                delta_site += landmark_text_d[landmark_label[i]] + 25
            txt_dr   = 0.04
            txt_ang  = site2angle(landmark_start[i]+delta_site)
            txt_rot  = site2angle(landmark_start[i]+delta_site, deg=True)-90
            txt_x    = (arc_r[track] + (arc_dr/2) + txt_dr)*np.cos(txt_ang)
            txt_y    = (arc_r[track] + (arc_dr/2) + txt_dr)*np.sin(txt_ang)
            txtprops = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY,
                            size=SIZELABEL, rotation=txt_rot)
            ax.text(txt_x, txt_y, landmark_label[i], **txtprops)
            
    # Arcs for internal landmarks

    arc_r        = 0.65
    arc_dr       = 0.01
    track        = 0
    mark_patches = []
    mark_text_d  = { }

    for i in range(len(mark_label)):
        
        arc_props = dict(center=[0,0], r=arc_r, width=arc_dr, lw=AXWIDTH/2, ec=BKCOLOR, fc='none',
                         theta1=site2angle(mark_end[i], deg=True), theta2=site2angle(mark_start[i], deg=True))
        mark_patches.append(matplotlib.patches.Wedge(**arc_props))
        
#        arc_props = dict(xy=(0,0), height=arc_r*2, width=arc_r*2, lw=AXWIDTH, color=BKCOLOR,
#                         theta1=site2angle(mark_end[i], deg=True), theta2=site2angle(mark_start[i], deg=True))
#        mark_patches.append(matplotlib.patches.Arc(**arc_props))
        
        # label with line
        if True:
            txtprops  = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, rotation=0)
            plotprops = dict(lw=AXWIDTH/2, ls='-', clip_on=False)

            label_x = [arc_r*np.cos(site2angle(mark_start[i]))]
            label_y = [arc_r*np.sin(site2angle(mark_start[i]))]
            ddr     = -0.11
            if mark_label[i] in label2ddr:
                ddr = label2ddr[mark_label[i]]

            ddx1 =  ddr * np.cos(site2angle(mark_start[i]))
            ddy  =  ddr * np.sin(site2angle(mark_start[i]))
            ddx2 = ddx1 - np.sign(ddx1)*0.03

#            label_x = label_x + [label_x[0] + ddx1, label_x[0] + ddx2]
#            label_y = label_y + [label_y[0] +  ddy, label_y[0] +  ddy]
            label_x = label_x + [label_x[0] + ddx1]
            label_y = label_y + [label_y[0] +  ddy]
            if label_x[0]<0:
                txtprops['ha'] = 'left'
            else:
                txtprops['ha'] = 'right'

            ax.text(label_x[-1] + ddx1/3, label_y[-1] + ddy/3, mark_label[i], **txtprops)
            mp.line(ax=ax, x=[label_x], y=[label_y], colors=[BKCOLOR], plotprops=plotprops)

    # Arcs for TGCA selection tracks
    
    for i in range(len(level_rad)):
        arc_props = dict(center=[0,0], r=level_rad[i], width=0, lw=AXWIDTH/2, ec=C_NEU_LT, fc='none', theta1=0, theta2=360)
        landmark_patches.append(matplotlib.patches.Wedge(**arc_props))

#    # Arcs for epitopes
#
#    arc_r           = 1.04
#    arc_dr          = 0.32
#    epitope_patches = []
#
#    for i in range(len(epitope_label)):
#
#        arc_props = dict(center=[0,0], r=arc_r, width=arc_dr, lw=AXWIDTH/2, ec=BKCOLOR, fc='#f2f2f2', alpha=0.8,
#                         theta1=site2angle(epitope_end[i], deg=True), theta2=site2angle(epitope_start[i], deg=True))
#        epitope_patches.append(matplotlib.patches.Wedge(**arc_props))
#
#        # label epitopes
#        if True:
#            mid       = (site2angle(epitope_end[i], deg=True)+site2angle(epitope_start[i], deg=True))/2.
#            label_x   = [arc_r * np.cos(mid * 2 * np.pi / 360.)]
#            label_y   = [arc_r * np.sin(mid * 2 * np.pi / 360.)]
#            ddr       = 0.06
#            if epitope_label[i] in label2ddr:
#                ddr = label2ddr[epitope_label[i]]
#            ddx1 =  ddr * np.cos(mid * 2 * np.pi / 360.)
#            ddy  =  ddr * np.sin(mid * 2 * np.pi / 360.)
#            ddx2 = ddx1 + np.sign(ddx1)*0.03
#            txtprops  = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, rotation=0)
#            plotprops = dict(lw=AXWIDTH/2, ls='-', clip_on=False)
#
#            label_x = label_x + [label_x[0] + ddx1, label_x[0] + ddx2]
#            label_y = label_y + [label_y[0] +  ddy, label_y[0] +  ddy]
#            if label_x[0]<0:
#                txtprops['ha'] = 'right'
#            else:
#                txtprops['ha'] = 'left'
#
#            ax.text(label_x[-1], label_y[-1], epitope_label[i], **txtprops)
#            mp.line(ax=ax, x=[label_x], y=[label_y], colors=[BKCOLOR], plotprops=plotprops)

#    # Arc plot for large values of integrated covariance
#
#    c_pos  = LCOLOR
#    c_neg  = LCOLOR
#    c_circ = { True : c_neg, False : c_pos }
#
#    arc_rad   = 0.65
#    arc_mult  = SIZELINE/2
#    arc_alpha = 0.1
#
#    circ_color = [c_circ[ic>0]                                     for ic in inv_cov]
#    #circ_color = [c_circ[idx_1[i] in epitope_sites or idx_2[i] in epitope_sites] for i in range(len(inv_cov))]
#    circ_rad   = [[arc_rad, arc_rad]                               for ic in inv_cov]
#    circ_arc   = [dict(lw=arc_mult * np.fabs(ic), alpha=arc_alpha) for ic in inv_cov]
#    circ_x     = [(i+(def_buff/2)) for i in idx_1]
#    circ_y     = [(i+(def_buff/2)) for i in idx_2]

    # Make plot

    pprops = { #'colors':   circ_color,
               'xlim':    [-1.05, 1.05],
               'ylim':    [-1.05, 1.05],
               'xticks':  [],
               'yticks':  [],
               #'size':     end_idx-start_idx+def_buff,
               #'bezrad':   0.0,
               #'rad':      circ_rad,
               #'arcprops': circ_arc,
               'hide':    ['left','right', 'top', 'bottom'],
               'noaxes':  True }

    for i in range(len(dot_x)):
        plotprops = dict(lw=0, marker='o', s=dot_sizes[i], zorder=9999)
        if i<len(dot_x)-1:
            mp.scatter(             ax=ax, x=[[dot_x[i]]], y=[[dot_y[i]]], colors=[dot_colors[i]], plotprops=plotprops)
        else:
            mp.plot(type='scatter', ax=ax, x=[[dot_x[i]]], y=[[dot_y[i]]], colors=[dot_colors[i]], plotprops=plotprops, **pprops)

#    for i in range(len(np.unique(df_sel['nucleotide number']))):
#        plotprops = dict(lw=AXWIDTH, ls='-')
#        if i==len(np.unique(df_sel['nucleotide number']))-1:
#            mp.plot(type='line', ax=ax, x=[line_x[i]], y=[line_y[i]], colors=[line_c[i]], plotprops=plotprops, **pprops)
#        else:
#            mp.line(             ax=ax, x=[line_x[i]], y=[line_y[i]], colors=[line_c[i]], plotprops=plotprops)

#    mp.plot(type='circos', ax=ax, x=circ_x, y=circ_y, **pprops)

    for patch in landmark_patches:
        ax.add_artist(patch)
        
    for patch in mark_patches:
        ax.add_artist(patch)

#    for patch in epitope_patches:
#        ax.add_artist(patch)

    return sig_s, sig_site_real, sig_nuc_idx #, epitope_start, epitope_end
    
    
#### FIGURES FOR SLIDES ####
    
def plot_circle_slides(selection_file, label2ddr=[]):
    """ Ye olde circle plot """
    
    # PLOT FIGURE

    ## set up figure grid

    w     = 8 #3.9 #SINGLE_COLUMN
    goldh = w
    fig   = plt.figure(figsize=(w, goldh))

    d = 0.062 #0.02
    box_circ = dict(left=d, right=1-d, bottom=d, top=1-d)
    gs_circ  = gridspec.GridSpec(1, 1, width_ratios=[1.0], height_ratios=[1.0], **box_circ)
    ax_circ  = plt.subplot(gs_circ[0, 0])
    
    ## circle plot

    df_sel = pd.read_csv(selection_file, comment='#', memory_map=True)
    
    sig_s, sig_site_real, sig_nuc_idx = plot_circle_formatter_slides(ax_circ, df_sel, label2ddr)
    
    #ax_circ.text(box_circ['left']-0.02, box_circ['top']+dy, 'd'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)

    # MAKE LEGEND

    invt = ax_circ.transData.inverted()
    xy1  = invt.transform((0,0))
    xy2  = invt.transform((0,9))
    
    coef_legend_dx = 0.05 #0.08
    coef_legend_x  = 0 - 5*coef_legend_dx
    coef_legend_y  = 0.1 #0.2
    coef_legend_dy = 3*(xy1[1]-xy2[1])

    txtprops = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
    ex_s     = [-0.05, -0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04, 0.05]
    show_s   = [    1,     0,     0,     0,     0, 1,    0,    0,    0,    0,    1]
    c_s      = [C_DEL, C_BEN]
    for i in range(len(ex_s)):
        plotprops = dict(lw=0, marker='o', s=(np.fabs(ex_s[i]) - DS_NORM)*S_MULT if ex_s[i]!=0 else 0, clip_on=False)
        mp.scatter(ax=ax_circ, x=[[coef_legend_x + i*coef_legend_dx]], y=[[coef_legend_y]], colors=[c_s[ex_s[i]>0]], plotprops=plotprops)
        if show_s[i]:
            ax_circ.text(coef_legend_x + i*coef_legend_dx, coef_legend_y + 0.75*coef_legend_dy, '%d' % (100*ex_s[i]), **txtprops)
    ax_circ.text(coef_legend_x + len(ex_s)*coef_legend_dx/2, coef_legend_y + (2.25*coef_legend_dy), 'Inferred selection\ncoefficient (%)', **txtprops)

    # SAVE FIGURE

    plt.savefig('%s/fig-circle%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)
    
    
def plot_circle_formatter_slides(ax, df_sel, label2ddr):
    """
    Create a circle plot showing selection and sequence features.
    """

    n_sig = 0

    sig_s          = []
    sig_site_real  = []
    sig_nuc_idx    = []
    start_idx      = np.min(df_sel['index'])
    end_idx        = np.max(df_sel['index'])
    start_full_idx = int(df_sel[df_sel['index']==start_idx].iloc[0]['nucleotide number'])
    start_dx       = start_idx - start_full_idx

    for df_iter, df_entry in df_sel.iterrows():
        s_val   = df_entry['selection coefficient']
        #idx     = (df_entry.polymorphic_index * 4) + NUC.index(df_entry.nucleotide) - 1 # find where this is in the cov matrix
        sigma_s = 1 #np.sqrt(ds[idx][idx])
        if np.fabs(s_val)>S_CUTOFF: #mult*sigma_s:
            n_sig += 1
            sig_s.append(s_val)
            sig_site_real.append(df_entry['index']-start_idx)
            sig_nuc_idx.append(NUC.index(df_entry['nucleotide']))
    
    # Sequence landmarks

    seq_range = [[ 265, 805], [805, 2719], [2719, 8554], [8554, 10054], [10054, 10972], [10972, 11842], [11842, 12091]]
    seq_label = [     'NSP1',      'NSP2',       'NSP3',        'NSP4',         'NSP5',         'NSP6',        'NSP7']
    seq_range = seq_range + [[12091, 12685], [12685, 13024], [13024, 13441], [13441, 16236], [16236, 18039]]
    seq_label = seq_label + [        'NSP8',         'NSP9',        'NSP10',        'NSP12',       'NSP13']
    seq_range = seq_range + [[18039, 19620], [19620, 20658], [20658, 21552], [21562, 25384], [25392, 26220]]
    seq_label = seq_label + [       'NSP14',        'NSP15',        'NSP16',            'S',       'ORF3a']
    seq_range = seq_range + [[26244, 26472], [26522, 27191], [27201, 27387], [27393, 27759], [27755, 27887]]
    seq_label = seq_label + [           'E',            'M',         'ORF6',        'ORF7a',       'ORF7b']
    seq_range = seq_range + [[27893, 28259], [28273, 29533], [29557, 29674]]
    seq_label = seq_label + [        'ORF8',            'N',        'ORF10']
    
    seq_range = np.array(seq_range) + 1

    landmark_start = []
    landmark_end   = []
    landmark_label = []
    
    def get_protein_edges(df, protein, num_idx='index', full_idx='nucleotide number'):
        temp_df      = df[df['protein']==protein]
        min_idx      = np.argmin(temp_df[num_idx])
        max_idx      = np.argmax(temp_df[num_idx])
        min_num_idx  = temp_df.iloc[min_idx][num_idx]
        max_num_idx  = temp_df.iloc[max_idx][num_idx]
        min_full_idx = int(temp_df.iloc[min_idx][full_idx])
        max_full_idx = int(temp_df.iloc[max_idx][full_idx])
        return min_num_idx, min_full_idx, max_num_idx, max_full_idx

    for i in range(len(seq_label)):
#        label_min  = df_sel[df_sel['protein']==seq_label[i]].iloc[0]['index']
#        label_start_idx = df_sel[df_sel['nucleotide number']==str()].iloc[0]['index']
#        label_end_idx   = df_sel[df_sel['nucleotide number']==str(seq_range[i][1])].iloc[0]['index']
        min_num_idx, min_full_idx, max_num_idx, max_full_idx = get_protein_edges(df_sel, seq_label[i])
        prot_start = min_num_idx - (min_full_idx - seq_range[i][0])
        prot_end   = max_num_idx + (seq_range[i][1] - max_full_idx)
        landmark_start.append(prot_start - start_idx)
        landmark_end.append(prot_end - start_idx)
#        landmark_start.append(seq_range[i][0]-start_idx)
#        landmark_end.append(seq_range[i][1]-start_idx)
        landmark_label.append(seq_label[i])
        
    # Internal landmarks
    
#    mark_range = [[21563 + 3*(13-1), 21563 + 3*305], [21563 + 3*(319-1), 21563 + 3*541]]
#    mark_label = [                      'Spike NTD',                        'Spike RBD']
    
    mark_range = [[21563 + 3*(14-1), 21563 + 3*685]]
    mark_label = ['S1 subunit']
    
    mark_start = []
    mark_end   = []
    
    for i in range(len(mark_label)):
#        mark_start_idx = df_sel[df_sel['nucleotide number']==str(mark_range[i][0])].iloc[0]['index']
#        mark_end_idx   = df_sel[df_sel['nucleotide number']==str(mark_range[i][1])].iloc[0]['index']
        min_num_idx, min_full_idx, max_num_idx, max_full_idx = get_protein_edges(df_sel, 'S')
        prot_start = min_num_idx - (min_full_idx - mark_range[i][0])
        prot_end   = max_num_idx + (mark_range[i][1] - max_full_idx)
        mark_start.append(prot_start - start_idx)
        mark_end.append(prot_end - start_idx)
#        mark_start.append(mark_range[i][0]-start_idx)
#        mark_end.append(mark_range[i][1]-start_idx)

    # Dot plot for significant selection coefficients

    c_dot = { True : C_BEN, False : C_DEL }
    
    level_rad = [0.9, 0.85, 0.80, 0.75, 0.70]

    def_buff = 1000
    def site2angle(site, deg=False, buffer=def_buff):
        if deg: return    -360.*(site+(buffer/2))/(end_idx-start_idx+buffer)
        else:   return -2*np.pi*(site+(buffer/2))/(end_idx-start_idx+buffer)

    dot_colors = [c_dot[s>0]                      for s in sig_s]
    dot_sizes  = [S_MULT * (np.fabs(s) - DS_NORM) for s in sig_s]
    dot_x = [level_rad[sig_nuc_idx[i]] * np.cos(site2angle(sig_site_real[i])) for i in range(len(sig_s))]
    dot_y = [level_rad[sig_nuc_idx[i]] * np.sin(site2angle(sig_site_real[i])) for i in range(len(sig_s))]

    txtprops = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, rotation=0)
    for i in range(len(NUC)):
        if i==len(NUC)-1:
            ax.text(level_rad[i], 0, '–', **txtprops)
        else:
            ax.text(level_rad[i], 0, NUC[i], **txtprops)

    # Arcs for sequence landmarks

    arc_r            = [0.96, 0.99, 1.02]
    arc_dr           = 0.01
    track            = 0
    landmark_patches = []
    landmark_text_d  = { }
    
    #show_labels = ['NSP6', 'S']

    for i in range(len(landmark_label)):
        if landmark_label[i]=='ORF7b':
            track = 1
        else:
            track = 0
        
        arc_props = dict(center=[0,0], r=arc_r[track], width=arc_dr, lw=AXWIDTH/2, ec=BKCOLOR, fc='none',
                         theta1=site2angle(landmark_end[i], deg=True), theta2=site2angle(landmark_start[i], deg=True))
        landmark_patches.append(matplotlib.patches.Wedge(**arc_props))

        # label with line
        if True: #landmark_label[i] in show_labels:
            txtprops  = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, rotation=0)
            plotprops = dict(lw=AXWIDTH/2, ls='-', clip_on=False)

            label_x = [arc_r[track]*np.cos(site2angle(landmark_start[i]))]
            label_y = [arc_r[track]*np.sin(site2angle(landmark_start[i]))]
            ddr     = 0.05 #0.11
            if landmark_label[i] in label2ddr:
                ddr = label2ddr[landmark_label[i]]

            ddx1 =  ddr * np.cos(site2angle(landmark_start[i]))
            ddy  =  ddr * np.sin(site2angle(landmark_start[i]))
            ddx2 = ddx1 + np.sign(ddx1)*0.03

            label_x = label_x + [label_x[0] + ddx1, label_x[0] + ddx2]
            label_y = label_y + [label_y[0] +  ddy, label_y[0] +  ddy]
            if label_x[0]<0:
                txtprops['ha'] = 'right'
            else:
                txtprops['ha'] = 'left'

            ax.text(label_x[-1], label_y[-1], landmark_label[i], **txtprops)
            mp.line(ax=ax, x=[label_x], y=[label_y], colors=[BKCOLOR], plotprops=plotprops)

#        # plot normally
#        else:
#            delta_site = 500
#            if landmark_label[i] in ['vif']:
#                delta_site += landmark_text_d[landmark_label[i]] + 25
#            txt_dr   = 0.04
#            txt_ang  = site2angle(landmark_start[i]+delta_site)
#            txt_rot  = site2angle(landmark_start[i]+delta_site, deg=True)-90
#            txt_x    = (arc_r[track] + (arc_dr/2) + txt_dr)*np.cos(txt_ang)
#            txt_y    = (arc_r[track] + (arc_dr/2) + txt_dr)*np.sin(txt_ang)
#            txtprops = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY,
#                            size=SIZELABEL, rotation=txt_rot)
#            ax.text(txt_x, txt_y, landmark_label[i], **txtprops)
            
    # Arcs for internal landmarks

    arc_r        = 0.65
    arc_dr       = 0.01
    track        = 0
    mark_patches = []
    mark_text_d  = { }

    for i in range(len(mark_label)):
        
        arc_props = dict(center=[0,0], r=arc_r, width=arc_dr, lw=AXWIDTH/2, ec=BKCOLOR, fc='none',
                         theta1=site2angle(mark_end[i], deg=True), theta2=site2angle(mark_start[i], deg=True))
        mark_patches.append(matplotlib.patches.Wedge(**arc_props))
        
        # label with line
        if True:
            txtprops  = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, rotation=0)
            plotprops = dict(lw=AXWIDTH/2, ls='-', clip_on=False)

            label_x = [arc_r*np.cos(site2angle(mark_start[i]))]
            label_y = [arc_r*np.sin(site2angle(mark_start[i]))]
            ddr     = -0.11
            if mark_label[i] in label2ddr:
                ddr = label2ddr[mark_label[i]]

            ddx1 =  ddr * np.cos(site2angle(mark_start[i]))
            ddy  =  ddr * np.sin(site2angle(mark_start[i]))
            ddx2 = ddx1 - np.sign(ddx1)*0.03

            label_x = label_x + [label_x[0] + ddx1]
            label_y = label_y + [label_y[0] +  ddy]
            if label_x[0]<0:
                txtprops['ha'] = 'left'
            else:
                txtprops['ha'] = 'right'

            ax.text(label_x[-1] + ddx1/3, label_y[-1] + ddy/3, mark_label[i], **txtprops)
            mp.line(ax=ax, x=[label_x], y=[label_y], colors=[BKCOLOR], plotprops=plotprops)

    # Arcs for TGCA selection tracks
    
    for i in range(len(level_rad)):
        arc_props = dict(center=[0,0], r=level_rad[i], width=0, lw=AXWIDTH/2, ec=C_NEU_LT, fc='none', theta1=0, theta2=360)
        landmark_patches.append(matplotlib.patches.Wedge(**arc_props))

    # Make plot

    pprops = { 'xlim':    [-1.05, 1.05],
               'ylim':    [-1.05, 1.05],
               'xticks':  [],
               'yticks':  [],
               'hide':    ['left','right', 'top', 'bottom'],
               'noaxes':  True }

    for i in range(len(dot_x)):
        plotprops = dict(lw=0, marker='o', s=dot_sizes[i], zorder=9999)
        if i<len(dot_x)-1:
            mp.scatter(             ax=ax, x=[[dot_x[i]]], y=[[dot_y[i]]], colors=[dot_colors[i]], plotprops=plotprops)
        else:
            mp.plot(type='scatter', ax=ax, x=[[dot_x[i]]], y=[[dot_y[i]]], colors=[dot_colors[i]], plotprops=plotprops, **pprops)

    for patch in landmark_patches:
        ax.add_artist(patch)
        
    for patch in mark_patches:
        ax.add_artist(patch)

    return sig_s, sig_site_real, sig_nuc_idx #, epitope_start, epitope_end
    

def plot_trajectories_slides(trajectory_file, location, f_cutoff=0.05, interpolate=False):
    """ Map out trajectories of all mutations in a specific region over time. """
        
    # Load data
    df_traj = pd.read_csv(trajectory_file, comment='#', memory_map=True)
    df_traj = df_traj[df_traj['location'].str.contains(location)]
    
    muts = np.unique(df_traj['variant_name'])
    xs   = []
    ys   = []
    if interpolate:
        for m in muts:
            df_temp = df_traj[df_traj['variant_name']==m]
            temp_xs = []
            temp_ys = []
            for idx, entry in df_temp.iterrows():
                temp_xs.append(entry['times'])
                temp_ys.append(entry['frequency_trajectory'])
            t_start = np.array([int(x.split()[0]) for x in temp_xs])
            t_order = np.argsort(t_start)
            xs.append(np.array(' '.join(np.array(temp_xs)[t_order]).split(), int))
            ys.append(np.array(' '.join(np.array(temp_ys)[t_order]).split(), float))
    else:
        xs = np.array([np.array(df_traj.iloc[i]['times'].split(), int) for i in range(len(df_traj))], dtype=object)
        ys = np.array([np.array(df_traj.iloc[i]['frequency_trajectory'].split(), float) for i in range(len(df_traj))], dtype=object)
        
    ms = np.array([np.max(y) for y in ys])
    xs = np.array(xs, dtype=object)[ms>f_cutoff]
    ys = np.array(ys, dtype=object)[ms>f_cutoff]
    print('Including %d trajectories' % len(xs))
    
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = SLIDE_WIDTH
    goldh = w / 3.3
    fig   = plt.figure(figsize=(w, goldh))

    box_traj = dict(left=0.05, right=0.95, bottom=0.05, top=0.95)
    gs_traj  = gridspec.GridSpec(1, 1, **box_traj)
    
    ### trajectories
    
    ax = plt.subplot(gs_traj[0, 0])
    
    legendprops = { 'loc' : 4, 'frameon' : False, 'scatterpoints' : 1, 'handletextpad' : 0.1,
                    'prop' : {'size' : SIZELABEL}, 'ncol' : 1 }
    lineprops   = { 'lw' : SIZELINE, 'linestyle' : '-', 'alpha' : 0.5 }
    #fillprops   = { 'lw' : 0, 'alpha' : 0.3, 'interpolate' : True }
    
    pprops = { 'xticks' : [],
               'yticks' : [0, 1],
               'hide'   : ['top', 'bottom', 'left', 'right'],
               'theme'  : 'open' }
    
    t_max       = 600
    xticks      = [      61,      153,      245,      336,      426,      518, 600]
    xticklabels = ['Mar 20', 'Jun 20', 'Sep 20', 'Dec 20', 'Mar 21', 'Jun 21',  '']
#    xticklabels = [  '3/20',   '6/20',   '9/20',  '12/20',   '3/21',   '6/21',  '']
    
    colors = sns.hls_palette(len(xs))
    
    for i in range(len(xs)):
        times = xs[i]
        freqs = ys[i]
        
        full_times = times
        full_freqs = freqs
        
#        if interpolate:
#            full_times = np.arange(times[0], times[-1], 1)
#            full_freqs = np.zeros(len(full_times))
#            idx = 0
#            for k in range(len(full_times)):
#                t = full_times[k]
#                if t in times:
#                    idx = times.tolist().index(t)
#                    full_freqs[k] = freqs[idx]
#                else:
#                    f0 = freqs[idx]
#                    f1 = freqs[idx+1]
#                    t0 = times[idx]
#                    t1 = times[idx+1]
#                    x  = (t - t0) / (t1 - t0)
#                    full_freqs[k] = (1 - x)*f0 + x*f1
            
        pprops['colors'] = [colors[i]]
        pprops['xlim']   = [    61, t_max]
        pprops['ylim']   = [-0.005, 1.005]
        if (i==len(xs)-1):
            pprops['xticks']      = xticks
            pprops['xticklabels'] = ['' for xt in xticks] #xticklabels
            pprops['yticklabels'] = ['', '']
            pprops['hide']        = ['top', 'right']
            pprops['axoffset']    = 0.02
            mp.plot(type='line', ax=ax, x=[full_times], y=[full_freqs], plotprops=lineprops, **pprops)
        else:
            mp.line(             ax=ax, x=[full_times], y=[full_freqs], plotprops=lineprops, **pprops)
    
#    txtprops = dict(ha='center', va='center', rotation=90, color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, clip_on=False)
#    ax.text(box_traj['left']-0.04, box_traj['top']-(box_traj['top']-box_traj['bottom'])/2, 'Frequency', transform=fig.transFigure, **txtprops)

    # SAVE FIGURE

    plt.savefig('%s/fig-trajectories-%s-slides%s' % (FIG_DIR, location, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)
    
    
def plot_variant_selection_slides(variant_file, trajectory_file, variant_list=[], variant_names=[], s_cutoff=0.05):
    """ Map out mutations in the major variants, their aggregate inferred selection coefficients, and
        frequency trajectories across regions. """
        
    # adjust color list if necessary
    local_colors = deepcopy(VAR_COLORS)
    if len(variant_names)>8:
        local_colors = sns.husl_palette(len(variant_names))
        
    # Load data
    df_var = pd.read_csv(variant_file, comment='#', memory_map=True)
    df_sel = 0
    if len(variant_list)>0:
        df_sel = df_var[df_var.variant_names.isin(variant_list)]
        temp_var_list  = list(df_sel.variant_names)
        temp_var_names = []
        for i in range(len(temp_var_list)):
            temp_var_names.append(variant_names[variant_list.index(temp_var_list[i])])
        variant_list  = np.array(temp_var_list)
        variant_names = np.array(temp_var_names)
    else:
        df_sel = df_var[np.fabs(df_var.selection_coefficient)>s_cutoff]
        variant_list  = np.array(list(df_sel.variant_names))
        variant_names = np.array(variant_list)
    
    s_sort = np.argsort(np.fabs(df_sel.selection_coefficient))[::-1]
    print(np.array(np.fabs(df_sel.selection_coefficient))[s_sort])
    print(np.array(df_sel.variant_names)[s_sort])
    
    n_vars        = len(s_sort)
    variant_list  = variant_list[s_sort]
    variant_names = variant_names[s_sort]
    
    df_traj = pd.read_csv(trajectory_file, comment='#', memory_map=True)
    df_traj = df_traj[df_traj.variant_names.isin(variant_list)]
    
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = 6 #SLIDE_WIDTH
    goldh = 2.37 #w / 1.8
    fig   = plt.figure(figsize=(w, goldh))

    box_traj = dict(left=0.08, right=0.95, bottom=0.17, top=0.97)
    #box_sel  = dict(left=0.80, right=0.95, bottom=0.13, top=0.95)

    gs_traj = gridspec.GridSpec(n_vars, 2, width_ratios=[2, 1], wspace=0.05, **box_traj)
    #gs_sel  = gridspec.GridSpec(1, 1, **box_sel)
    
    ### trajectories
    
    ax = [[plt.subplot(gs_traj[i, 0]), plt.subplot(gs_traj[i, 1])] for i in range(n_vars)]
    
    legendprops = { 'loc' : 4, 'frameon' : False, 'scatterpoints' : 1, 'handletextpad' : 0.1,
                    'prop' : {'size' : SIZELABEL}, 'ncol' : 1 }
    lineprops   = { 'lw' : SIZELINE, 'linestyle' : '-', 'alpha' : 0.5 }
    #fillprops   = { 'lw' : 0, 'alpha' : 0.3, 'interpolate' : True }
    
    pprops = { 'xticks' : [],
               'yticks' : [],
               'hide'   : ['top', 'bottom', 'left', 'right'],
               'theme'  : 'open' }
    
    t_max = 600
    xticks      = [      61,      153,      245,      336,      426,      518, 600]
    #xticklabels = ['Mar 20', 'Jun 20', 'Sep 20', 'Dec 20', 'Mar 21', 'Jun 21',  '']
    xticklabels = [  '3/20',   '6/20',   '9/20',  '12/20',   '3/21',   '6/21',  '']
    
    for i in range(n_vars):
        idx = list(s_sort)[i]
        pprops['colors'] = [local_colors[i]]
        pprops['xlim']   = [   61, t_max]
        pprops['ylim']   = [-0.05,  1.05]
        if (i==n_vars-1):
#            pprops['xticks']   = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600]
#            pprops['xlabel']   = 'Time (generations)'
            pprops['xticks']      = xticks
            pprops['xticklabels'] = xticklabels
            pprops['hide']        = ['top', 'left', 'right']
            pprops['axoffset']    = 0.18
        df_temp = df_traj[df_traj.variant_names==df_sel.iloc[idx].variant_names]
        for k in range(len(df_temp)):
            entry = df_temp.iloc[k]
            times = np.array(entry.times.split(), float)
            freqs = np.array(entry.frequencies.split(), float)
            if k==len(df_temp)-1:
                mp.plot(type='line', ax=ax[i][0], x=[times], y=[freqs], plotprops=lineprops, **pprops)
            else:
                mp.line(             ax=ax[i][0], x=[times], y=[freqs], plotprops=lineprops, **pprops)
            
        txtprops = dict(ha='left', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
        if variant_list[i]=='B.1':
            ax[i][0].text(101, 0.1, variant_names[i], **txtprops)
        else:
            ax[i][0].text( 61, 0.8, variant_names[i], **txtprops)
    
    txtprops = dict(ha='center', va='center', rotation=90, color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, clip_on=False)
    ax[-1][0].text(box_traj['left']-0.04, box_traj['top']-(box_traj['top']-box_traj['bottom'])/2, 'Frequency', transform=fig.transFigure, **txtprops)
            
    ### selection coefficient estimates
    
    dashlineprops = dict(lw=SIZELINE, ls=':', alpha=0.25, clip_on=False, zorder=-9999)
    sprops = dict(lw=0, s=9., marker='o')
    
    pprops = { 'yticks': [],
               'xticks': [],
               'hide'  : ['top', 'bottom', 'left', 'right'],
               'theme' : 'open' }
    
#    xticks      = [0, 0.2, 0.4, 0.6, 0.8]
#    xticklabels = [0, 20, 40, 60, 80]
    xticks      = [0, 0.25, 0.5, 0.75, 1.0]
    xticklabels = [0, 25, 50, 75, 100]
    
    for i in range(len(xticks)):
        xdat = [xticks[i], xticks[i]]
        ydat = [0.5, n_vars+2.0]
        mp.line(ax=ax[-1][1], x=[xdat], y=[ydat], colors=[BKCOLOR], plotprops=dashlineprops)
    
    for i in range(n_vars):
        idx = list(s_sort)[i]
        pprops['xlim'] = [   0,   1]
        pprops['ylim'] = [ 0.5, 1.5]
        ydat           = [1]
        xdat           = [df_sel.iloc[idx].selection_coefficient]
        xerr           = [df_sel.iloc[idx].standard_deviation]
        if (i==n_vars-1):
            pprops['xticks']      = xticks
            pprops['xticklabels'] = xticklabels
            #pprops['xlabel']      = 'Inferred selection\ncoefficient (%)'
            pprops['hide']        = ['top', 'left', 'right']
            pprops['axoffset']    = 0.3
        mp.plot(type='error', ax=ax[i][1], x=[xdat], y=[ydat], xerr=[xerr], colors=[local_colors[i]], **pprops)

    # SAVE FIGURE

    plt.savefig('%s/fig-variants%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)
    

def plot_early_detection_slides_alpha(null_file, alpha_file, alpha_start, alpha_end, delta_file, delta_start, delta_end):
    """ Plot the null distribution for mutations inferred to be nearly neutral.
        Plot frequencies and early detection times for Alpha and Delta variants. """
    
    # Load data
    inferred_null = np.loadtxt(null_file)
    df_alpha      = pd.read_csv(alpha_file, comment='#', memory_map=True)
    df_alpha      = df_alpha[(df_alpha['time']>=alpha_start) & (df_alpha['time']<=alpha_end)]
    df_delta      = pd.read_csv(delta_file, comment='#', memory_map=True)
    df_delta      = df_delta[(df_delta['time']>=delta_start) & (df_delta['time']<=delta_end)]
    
    # Null distribution statistics
    max_null    = np.amax(inferred_null)
    min_null    = np.amin(inferred_null)
    num_largest = int(round(len(inferred_null) * 2.5 / 100))    # the number of coefficients in the top 2.5% of the null distribution
    soft_cutoff = np.sort(inferred_null)[::-1][num_largest]
    print('hard cutoff = %.4f' % max_null)
    print('soft cutoff = %.4f\n' % soft_cutoff)
    
    # Get early detection times
#    t_alpha      = np.min(df_alpha[df_alpha['selection']>max_null]['time'])
#    t_soft_alpha = np.min(df_alpha[df_alpha['selection']>soft_cutoff]['time'])
#    t_delta      = np.min(df_delta[df_delta['selection']>max_null]['time'])
#    t_soft_delta = np.min(df_delta[df_delta['selection']>soft_cutoff]['time'])
    
    t_alpha      = df_alpha[df_alpha['selection']>max_null].iloc[0]['time']
    f_alpha      = df_alpha[df_alpha['selection']>max_null].iloc[0]['frequency']
    t_soft_alpha = df_alpha[df_alpha['selection']>soft_cutoff].iloc[0]['time']
    f_soft_alpha = df_alpha[df_alpha['selection']>soft_cutoff].iloc[0]['frequency']
    t_delta      = df_delta[df_delta['selection']>max_null].iloc[0]['time']
    f_delta      = df_delta[df_delta['selection']>max_null].iloc[0]['frequency']
    t_soft_delta = df_delta[df_delta['selection']>soft_cutoff].iloc[0]['time']
    f_soft_delta = df_delta[df_delta['selection']>soft_cutoff].iloc[0]['frequency']
    
#    t_alpha      = 0
#    f_alpha      = 0
#    t_soft_alpha = 0
#    f_soft_alpha = 0
   
    print('time')
    print('cutoff\talpha\tdelta')
    print('hard\t%d\t%d' % (t_alpha, t_delta))
    print('soft\t%d\t%d' % (t_soft_alpha, t_soft_delta))
    
    print('')
    print('frequency')
    print('cutoff\talpha\tdelta')
    print('hard\t%.3f\t%.3f' % (f_alpha, f_delta))
    print('soft\t%.3f\t%.3f' % (f_soft_alpha, f_soft_delta))
    print('')
    
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = 12.0
    goldh = (w / 2.5) * (SLIDE_WIDTH / 12.0)
    fig   = plt.figure(figsize=(w, goldh))

#    left_bd   = 0.08
#    right_bd  = 0.97
#    h_space   = 0.10
#    box_h     = (right_bd - left_bd - 2*h_space)/3
#    top_bd    = 0.92
#    bottom_bd = 0.15
#    v_space   = 0.10
#    box_v     = (top_bd - bottom_bd - 1*v_space)/2
#
#    box_null   = dict(left=left_bd + 0*box_h + 0*h_space, right=left_bd + 1*box_h + 0*h_space, top=top_bd, bottom=bottom_bd)
#    box_traj_a = dict(left=left_bd + 1*box_h + 1*h_space, right=left_bd + 2*box_h + 1*h_space, top=top_bd - 0*box_v - 0*v_space, bottom=top_bd - 1*box_v - 0*v_space)
#    box_sel_a  = dict(left=left_bd + 1*box_h + 1*h_space, right=left_bd + 2*box_h + 1*h_space, top=top_bd - 1*box_v - 1*v_space, bottom=top_bd - 2*box_v - 1*v_space)
#    box_traj_d = dict(left=left_bd + 2*box_h + 2*h_space, right=left_bd + 3*box_h + 2*h_space, top=top_bd - 0*box_v - 0*v_space, bottom=top_bd - 1*box_v - 0*v_space)
#    box_sel_d  = dict(left=left_bd + 2*box_h + 2*h_space, right=left_bd + 3*box_h + 2*h_space, top=top_bd - 1*box_v - 1*v_space, bottom=top_bd - 2*box_v - 1*v_space)

    left_bd   = 0.08
    right_bd  = 0.97
    h_space   = 0.15
    box_h     = 0.22
    top_bd    = 0.92
    bottom_bd = 0.15
    v_space   = 0.10
    box_v     = (top_bd - bottom_bd - 1*v_space)/2
    
    box_null   = dict(left=left_bd, right=left_bd + box_h, top=top_bd, bottom=bottom_bd)
    box_traj_a = dict(left=left_bd + box_h + h_space, right=right_bd, top=top_bd - 0*box_v - 0*v_space, bottom=top_bd - 1*box_v - 0*v_space)
    box_sel_a  = dict(left=left_bd + box_h + h_space, right=right_bd, top=top_bd - 1*box_v - 1*v_space, bottom=top_bd - 2*box_v - 1*v_space)
    
    ## a -- null distribution of selection coefficients

    gs_null = gridspec.GridSpec(1, 1, **box_null)
    ax_null = plt.subplot(gs_null[0, 0])
    
    histprops = dict(histtype='bar', lw=SIZELINE/2, rwidth=0.8, ls='solid', alpha=1, edgecolor='none',
                     orientation='vertical', log=True)
                     
    pprops = { 'xlim':        [-0.04, 0.045],
               'xticks':      [-0.04, -0.02, 0., 0.02, 0.04, 0.045],
               'xticklabels': [r'$-4$', r'$-2$', r'$0$', r'$2$', r'$4$', ''],
               'ylim':        [1e0, 1e6],
               'yticks':      [1e0, 1e2, 1e4, 1e6],
               #'yticklabels': [0, 10, 20, 30, 40, 50],
               'logy':        True,
               #'ylabel':      'Counts',
               #'xlabel':      'Inferred selection coefficients for neutral variants (%)',
               'bins':        np.arange(-0.04, 0.045+0.001, 0.001),
               'weights':     [np.ones_like(inferred_null)],
               'plotprops':   histprops,
               'axoffset':    0.1,
               'theme':       'open' }

    x = [inferred_null]
    mp.plot(type='hist', ax=ax_null, x=x, colors=[LCOLOR], **pprops)
    #ax_null.set_yscale('log', nonpositive='clip')
    
    # b/c -- Alpha/Delta frequency and inferred selection
    
    gs_traj_a = gridspec.GridSpec(1, 1, **box_traj_a)
    ax_traj_a = plt.subplot(gs_traj_a[0, 0])
#    gs_traj_d = gridspec.GridSpec(1, 1, **box_traj_d)
#    ax_traj_d = plt.subplot(gs_traj_d[0, 0])
    
    ylaba = 'Alpha frequency\nin London (%)'
    ylabd = 'Delta frequency\nin Great Britain (%)'
    
    gs_sel_a = gridspec.GridSpec(1, 1, **box_sel_a)
    ax_sel_a = plt.subplot(gs_sel_a[0, 0])
#    gs_sel_d = gridspec.GridSpec(1, 1, **box_sel_d)
#    ax_sel_d = plt.subplot(gs_sel_d[0, 0])
    
    ylima   = [0, 0.75]
    yticka  = [0, 0.25, 0.50, 0.75]
    ytickla = [int(i) for i in 100*np.array(yticka)]
    ymticka = []
    ylimd   = [0, 0.60]
    ytickd  = [0, 0.30, 0.60]
    ytickld = [int(i) for i in 100*np.array(ytickd)]
    ymtickd = [0.15, 0.45]
    
    for ax_traj, ax_sel, temp_df, t_det, ylabel, ylim, yticks, yticklabels, yminorticks, v_color in [
        [ax_traj_a, ax_sel_a, df_alpha, t_alpha, ylaba, ylima, yticka, ytickla, ymticka, C_ALPHA]]:
        #[ax_traj_d, ax_sel_d, df_delta, t_delta, ylabd, ylimd, ytickd, ytickld, ymtickd, C_DELTA] ]:
    
        ## b/c.1 -- frequency trajectory
        
        times   = np.array(temp_df['time'])
        freqs   = np.array(temp_df['frequency'])
        sels    = np.array(temp_df['selection'])
        
        lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1 }
        dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
        
        xticks      = np.arange(np.min(times), np.max(times), 14)
        xticklabels = [(dt.timedelta(days=int(i)) + dt.datetime(2020,1,1)) for i in xticks]
        xticklabels = [f'{i.month}/{i.day}' for i in xticklabels]
        
        pprops = { 'xlim':        [np.min(times), np.max(times)],
                   'xticks':      xticks,
                   'xticklabels': ['' for xtl in xticklabels],
                   'ylim':        [0, 1.05],
                   'yticks':      [0, 0.5, 1],
                   'yticklabels': [0, 50, 100],
                   'yminorticks': [0.25, 0.75],
                   'xlabel':      '',
                   #'ylabel':      ylabel,
                   'axoffset':    0.1,
                   'theme':       'open' }
        
        xdat = [times]
        ydat = [freqs]
        mp.line(ax=ax_traj, x=xdat, y=ydat, colors=[v_color], plotprops=lineprops, **pprops)
        
        tobs = 0
        for i in range(len(ydat[0])):
            if ydat[0][i]>0:
                tobs = xdat[0][i]
                break
        print('First observed at %d, detected selection at %d\n' % (tobs, t_det))

        xdat = [[t_det, t_det]]
        ydat = [[0, 1]]
        mp.plot(type='line', ax=ax_traj, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
        
        ## b/c.2 -- inferred selection coefficient

        pprops = { 'xlim':        [np.min(times), np.max(times)],
                   'xticks':      xticks,
                   'xticklabels': xticklabels,
                   'ylim':        ylim,
                   'yticks':      yticks,
                   'yticklabels': yticklabels,
                   'yminorticks': yminorticks,
                   #'xlabel':      'Date',
                   #'ylabel':      'Inferred selection\ncoefficient (%)',
                   'axoffset':    0.1,
                   'theme':       'open' }
        
        xdat = [times]
        ydat = [sels]
        mp.line(ax=ax_sel, x=xdat, y=ydat, colors=[LCOLOR], plotprops=lineprops, **pprops)

        xdat = [[t_det, t_det]]
        ydat = [[0, 1]]
        mp.plot(type='line', ax=ax_sel, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
        
        txtprops = dict(ha='left', va='top', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
        ax_traj.text(t_det+1.5, 0.98, 'Variant first reliably\ninferred to be\nbeneficial', **txtprops)

    ## legends and labels
    
#    dx = -0.06
#    dy =  0.01
#    ax_null.text(  box_null['left']   + dx, box_null['top']   + dy, 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
#    ax_traj_a.text(box_traj_a['left'] + dx, box_traj_a['top'] + dy, 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
#    ax_traj_d.text(box_traj_d['left'] + dx, box_traj_d['top'] + dy, 'c'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)

    # SAVE FIGURE

    plt.savefig('%s/fig-early-alpha%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)
    
    
def plot_early_detection_slides_delta(null_file, alpha_file, alpha_start, alpha_end, delta_file, delta_start, delta_end):
    """ Plot the null distribution for mutations inferred to be nearly neutral.
        Plot frequencies and early detection times for Alpha and Delta variants. """
    
    # Load data
    inferred_null = np.loadtxt(null_file)
    df_alpha      = pd.read_csv(alpha_file, comment='#', memory_map=True)
    df_alpha      = df_alpha[(df_alpha['time']>=alpha_start) & (df_alpha['time']<=alpha_end)]
    df_delta      = pd.read_csv(delta_file, comment='#', memory_map=True)
    df_delta      = df_delta[(df_delta['time']>=delta_start) & (df_delta['time']<=delta_end)]
    
    # Null distribution statistics
    max_null    = np.amax(inferred_null)
    min_null    = np.amin(inferred_null)
    num_largest = int(round(len(inferred_null) * 2.5 / 100))    # the number of coefficients in the top 2.5% of the null distribution
    soft_cutoff = np.sort(inferred_null)[::-1][num_largest]
    print('hard cutoff = %.4f' % max_null)
    print('soft cutoff = %.4f\n' % soft_cutoff)
    
    # Get early detection times
#    t_alpha      = np.min(df_alpha[df_alpha['selection']>max_null]['time'])
#    t_soft_alpha = np.min(df_alpha[df_alpha['selection']>soft_cutoff]['time'])
#    t_delta      = np.min(df_delta[df_delta['selection']>max_null]['time'])
#    t_soft_delta = np.min(df_delta[df_delta['selection']>soft_cutoff]['time'])
    
    t_alpha      = df_alpha[df_alpha['selection']>max_null].iloc[0]['time']
    f_alpha      = df_alpha[df_alpha['selection']>max_null].iloc[0]['frequency']
    t_soft_alpha = df_alpha[df_alpha['selection']>soft_cutoff].iloc[0]['time']
    f_soft_alpha = df_alpha[df_alpha['selection']>soft_cutoff].iloc[0]['frequency']
    t_delta      = df_delta[df_delta['selection']>max_null].iloc[0]['time']
    f_delta      = df_delta[df_delta['selection']>max_null].iloc[0]['frequency']
    t_soft_delta = df_delta[df_delta['selection']>soft_cutoff].iloc[0]['time']
    f_soft_delta = df_delta[df_delta['selection']>soft_cutoff].iloc[0]['frequency']
    
#    t_alpha      = 0
#    f_alpha      = 0
#    t_soft_alpha = 0
#    f_soft_alpha = 0
   
    print('time')
    print('cutoff\talpha\tdelta')
    print('hard\t%d\t%d' % (t_alpha, t_delta))
    print('soft\t%d\t%d' % (t_soft_alpha, t_soft_delta))
    
    print('')
    print('frequency')
    print('cutoff\talpha\tdelta')
    print('hard\t%.3f\t%.3f' % (f_alpha, f_delta))
    print('soft\t%.3f\t%.3f' % (f_soft_alpha, f_soft_delta))
    print('')
    
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = 12.0
    goldh = (w / 2.5) * (SLIDE_WIDTH / 12.0)
    fig   = plt.figure(figsize=(w, goldh))

#    left_bd   = 0.08
#    right_bd  = 0.97
#    h_space   = 0.10
#    box_h     = (right_bd - left_bd - 2*h_space)/3
#    top_bd    = 0.92
#    bottom_bd = 0.15
#    v_space   = 0.10
#    box_v     = (top_bd - bottom_bd - 1*v_space)/2
#
#    box_null   = dict(left=left_bd + 0*box_h + 0*h_space, right=left_bd + 1*box_h + 0*h_space, top=top_bd, bottom=bottom_bd)
#    box_traj_a = dict(left=left_bd + 1*box_h + 1*h_space, right=left_bd + 2*box_h + 1*h_space, top=top_bd - 0*box_v - 0*v_space, bottom=top_bd - 1*box_v - 0*v_space)
#    box_sel_a  = dict(left=left_bd + 1*box_h + 1*h_space, right=left_bd + 2*box_h + 1*h_space, top=top_bd - 1*box_v - 1*v_space, bottom=top_bd - 2*box_v - 1*v_space)
#    box_traj_d = dict(left=left_bd + 2*box_h + 2*h_space, right=left_bd + 3*box_h + 2*h_space, top=top_bd - 0*box_v - 0*v_space, bottom=top_bd - 1*box_v - 0*v_space)
#    box_sel_d  = dict(left=left_bd + 2*box_h + 2*h_space, right=left_bd + 3*box_h + 2*h_space, top=top_bd - 1*box_v - 1*v_space, bottom=top_bd - 2*box_v - 1*v_space)

    left_bd   = 0.08
    right_bd  = 0.97
    h_space   = 0.15
    box_h     = 0.22
    top_bd    = 0.92
    bottom_bd = 0.15
    v_space   = 0.10
    box_v     = (top_bd - bottom_bd - 1*v_space)/2
    
    box_null   = dict(left=left_bd, right=left_bd + box_h, top=top_bd, bottom=bottom_bd)
    box_traj_d = dict(left=left_bd + box_h + h_space, right=right_bd, top=top_bd - 0*box_v - 0*v_space, bottom=top_bd - 1*box_v - 0*v_space)
    box_sel_d  = dict(left=left_bd + box_h + h_space, right=right_bd, top=top_bd - 1*box_v - 1*v_space, bottom=top_bd - 2*box_v - 1*v_space)
    
    ## a -- null distribution of selection coefficients

    gs_null = gridspec.GridSpec(1, 1, **box_null)
    ax_null = plt.subplot(gs_null[0, 0])
    
    histprops = dict(histtype='bar', lw=SIZELINE/2, rwidth=0.8, ls='solid', alpha=1, edgecolor='none',
                     orientation='vertical', log=True)
                     
    pprops = { 'xlim':        [-0.04, 0.045],
               'xticks':      [-0.04, -0.02, 0., 0.02, 0.04, 0.045],
               'xticklabels': [r'$-4$', r'$-2$', r'$0$', r'$2$', r'$4$', ''],
               'ylim':        [1e0, 1e6],
               'yticks':      [1e0, 1e2, 1e4, 1e6],
               #'yticklabels': [0, 10, 20, 30, 40, 50],
               'logy':        True,
               #'ylabel':      'Counts',
               #'xlabel':      'Inferred selection coefficients for neutral variants (%)',
               'bins':        np.arange(-0.04, 0.045+0.001, 0.001),
               'weights':     [np.ones_like(inferred_null)],
               'plotprops':   histprops,
               'axoffset':    0.1,
               'theme':       'open' }

    x = [inferred_null]
    mp.plot(type='hist', ax=ax_null, x=x, colors=[LCOLOR], **pprops)
    #ax_null.set_yscale('log', nonpositive='clip')
    
    # b/c -- Alpha/Delta frequency and inferred selection
    
#    gs_traj_a = gridspec.GridSpec(1, 1, **box_traj_a)
#    ax_traj_a = plt.subplot(gs_traj_a[0, 0])
    gs_traj_d = gridspec.GridSpec(1, 1, **box_traj_d)
    ax_traj_d = plt.subplot(gs_traj_d[0, 0])
    
    ylaba = 'Alpha frequency\nin London (%)'
    ylabd = 'Delta frequency\nin Great Britain (%)'
    
#    gs_sel_a = gridspec.GridSpec(1, 1, **box_sel_a)
#    ax_sel_a = plt.subplot(gs_sel_a[0, 0])
    gs_sel_d = gridspec.GridSpec(1, 1, **box_sel_d)
    ax_sel_d = plt.subplot(gs_sel_d[0, 0])
    
    ylima   = [0, 0.75]
    yticka  = [0, 0.25, 0.50, 0.75]
    ytickla = [int(i) for i in 100*np.array(yticka)]
    ymticka = []
    ylimd   = [0, 0.75]
    ytickd  = [0, 0.25, 0.50, 0.75]
    ytickld = [int(i) for i in 100*np.array(yticka)]
    ymtickd = []
    
    for ax_traj, ax_sel, temp_df, t_det, ylabel, ylim, yticks, yticklabels, yminorticks, v_color in [
        #[ax_traj_a, ax_sel_a, df_alpha, t_alpha, ylaba, ylima, yticka, ytickla, ymticka, C_ALPHA],
        [ax_traj_d, ax_sel_d, df_delta, t_delta, ylabd, ylimd, ytickd, ytickld, ymtickd, C_DELTA] ]:
    
        ## b/c.1 -- frequency trajectory
        
        times   = np.array(temp_df['time'])
        freqs   = np.array(temp_df['frequency'])
        sels    = np.array(temp_df['selection'])
        
        lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1 }
        dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
        
        xticks      = np.arange(np.min(times), np.max(times), 14)
        xticklabels = [(dt.timedelta(days=int(i)) + dt.datetime(2020,1,1)) for i in xticks]
        xticklabels = [f'{i.month}/{i.day}' for i in xticklabels]
        
        pprops = { 'xlim':        [np.min(times), np.max(times)],
                   'xticks':      xticks,
                   'xticklabels': ['' for xtl in xticklabels],
                   'ylim':        [0, 1.05],
                   'yticks':      [0, 0.5, 1],
                   'yticklabels': [0, 50, 100],
                   'yminorticks': [0.25, 0.75],
                   'xlabel':      '',
                   #'ylabel':      ylabel,
                   'axoffset':    0.1,
                   'theme':       'open' }
        
        xdat = [times]
        ydat = [freqs]
        mp.line(ax=ax_traj, x=xdat, y=ydat, colors=[v_color], plotprops=lineprops, **pprops)
        
        tobs = 0
        for i in range(len(ydat[0])):
            if ydat[0][i]>0:
                tobs = xdat[0][i]
                break
        print('First observed at %d, detected selection at %d\n' % (tobs, t_det))

        xdat = [[t_det, t_det]]
        ydat = [[0, 1]]
        mp.plot(type='line', ax=ax_traj, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
        
        ## b/c.2 -- inferred selection coefficient

        pprops = { 'xlim':        [np.min(times), np.max(times)],
                   'xticks':      xticks,
                   'xticklabels': xticklabels,
                   'ylim':        ylim,
                   'yticks':      yticks,
                   'yticklabels': yticklabels,
                   'yminorticks': yminorticks,
                   #'xlabel':      'Date',
                   #'ylabel':      'Inferred selection\ncoefficient (%)',
                   'axoffset':    0.1,
                   'theme':       'open' }
        
        xdat = [times]
        ydat = [sels]
        mp.line(ax=ax_sel, x=xdat, y=ydat, colors=[LCOLOR], plotprops=lineprops, **pprops)

        xdat = [[t_det, t_det]]
        ydat = [[0, 1]]
        mp.plot(type='line', ax=ax_sel, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
        
        txtprops = dict(ha='left', va='top', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
        ax_traj.text(t_det+1.5, 0.98, 'Variant first reliably\ninferred to be\nbeneficial', **txtprops)

    ## legends and labels
    
#    dx = -0.06
#    dy =  0.01
#    ax_null.text(  box_null['left']   + dx, box_null['top']   + dy, 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
#    ax_traj_a.text(box_traj_a['left'] + dx, box_traj_a['top'] + dy, 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
#    ax_traj_d.text(box_traj_d['left'] + dx, box_traj_d['top'] + dy, 'c'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)

    # SAVE FIGURE

    plt.savefig('%s/fig-early-delta%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)


#### OLD VERSIONS ####

def plot_a222v_old(trajectory_file, variant_id, selection_file):
    """ Map out mutations in the major variants, their aggregate inferred selection coefficients, and
        frequency trajectories across regions. """
        
    # Load data
    df_traj = pd.read_csv(trajectory_file, comment='#', memory_map=True)
    df_sel  = pd.read_csv(selection_file, comment='#', memory_map=True)
    
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = SINGLE_COLUMN #SLIDE_WIDTH
    goldh = w / 1.8
    fig   = plt.figure(figsize=(w, goldh))

    scale   = 0.83 / (2 * 0.20 + 0.03)
    box_h   = 0.20 * scale
    box_dh  = 0.03 * scale
    box_top = 0.95

    box_traj = dict(left=0.15, right=0.95, top=box_top - 0*box_h - 0*box_dh, bottom=box_top - 1*box_h - 0*box_dh)
    box_sel  = dict(left=0.15, right=0.95, top=box_top - 1*box_h - 1*box_dh, bottom=box_top - 2*box_h - 0*box_dh)
    
    ## a -- A222V trajectories
    
    gs_traj = gridspec.GridSpec(1, 1, **box_traj)
    ax_traj = plt.subplot(gs_traj[0, 0])
    
    legendprops = { 'loc': 4, 'frameon': False, 'scatterpoints': 1, 'handletextpad': 0.1,
                    'prop': {'size' : SIZELABEL}, 'ncol' : 1 }
    lineprops   = { 'lw': SIZELINE*1.5, 'linestyle': '-', 'alpha': 0.5 }
    
    t_max  = 600
    pprops = { 'colors':   [C_A222V],
               'xlim':     [61, t_max],
               'xticks':   [],
               'ylim':     [-0.05,  1.05],
               'yticks':   [0, 1],
               'ylabel':   'S:A22V\nfrequency',
               'axoffset': 0.1,
               'hide':     ['bottom'],
               'theme':    'open' }
    
    df_temp = df_traj[df_traj.variant_names==variant_id]
    for k in range(len(df_temp)):
        entry = df_temp.iloc[k]
        times = np.array(str(entry.times).split(), float)
        freqs = np.array(str(entry.frequencies).split(), float)
        if k==len(df_temp)-1:
            mp.plot(type='line', ax=ax_traj, x=[times], y=[freqs], plotprops=lineprops, **pprops)
        else:
            mp.line(             ax=ax_traj, x=[times], y=[freqs], plotprops=lineprops, **pprops)
    
    ## b -- inferred selection coefficient

    gs_sel = gridspec.GridSpec(1, 1, **box_sel)
    ax_sel = plt.subplot(gs_sel[0, 0])
    
    xticks      = [      61,      153,      245,      336,      426,      518, 600]
    xticklabels = ['Mar 20', 'Jun 20', 'Sep 20', 'Dec 20', 'Mar 21', 'Jun 21',  '']
    lineprops   = { 'lw': SIZELINE*1.5, 'linestyle': '-', 'alpha': 1 }
    
    pprops = { 'xlim':        [61, t_max],
               'xticks':      xticks,
               'xticklabels': xticklabels,
               'ylim':        [0, 0.04],
               'yticks':      [0, 0.02, 0.04],
               'yticklabels': [0, 2, 4],
               #'xlabel':      'Date',
               'ylabel':      'Inferred selection\ncoefficient in Great Britain, ' + r'$\hat{s}$' + ' (%)',
               'axoffset':    0.1,
               'theme':       'open' }
    
    xdat = [np.array(df_sel['time'])]
    ydat = [np.array(df_sel['selection'])]
    mp.plot(type='line', ax=ax_sel, x=xdat, y=ydat, colors=[LCOLOR], plotprops=lineprops, **pprops)

    # SAVE FIGURE

    plt.savefig('%s/fig-4%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)

def plot_early_detection_old(inf_file, tv_file, link_file, full_tv_file=None, start=355, end_time=370, window_size=10):
    """ Plots the trajectory and the inferred coefficient over time for the B.1.1.7 group. Also compares to the null distribution."""
    
    site      = 'S-143-2'
    inf_data  = np.load(inf_file, allow_pickle=True)
    inferred  = inf_data['selection']
    alleles   = inf_data['allele_number']
    labels    = [GET_LABEL(i) for i in alleles]
    traj      = inf_data['traj']
    muts      = inf_data['mutant_sites']
    times     = inf_data['times']
    locs      = inf_data['locations']
    tv_data   = np.load(tv_file, allow_pickle=True)
    
    if False:
        traj  = inf_data['traj_nosmooth']
        times = inf_data['times_full']

    # Finding the B.1.1.7 trajectory
    site_traj  = []
    site_times = []
    for i in range(len(traj)):
        muts_temp = [GET_LABEL(muts[i][j]) for j in range(len(muts[i]))]
        if site in muts_temp:
            site_traj.append(traj[i][:, muts_temp.index(site)])
            site_times.append(times[i])

    # Finding the inferred coefficient for the linked group over all time
    labels_link, inf_link, err_link = CALCULATE_LINKED_COEFFICIENTS(tv_file, link_file, tv=True)
    site_index = []
    for i in range(len(labels_link)):
        labels_temp = [labels_link[i][j] for j in range(len(labels_link[i]))]
        if site in labels_temp:
            site_index.append(i)
    if len(site_index)>1:
        print('site appears in multiple places', site_index)
    site_inf = inf_link[:, site_index[0]]
    
    # getting the times corresponding to the inference for the region of interest
    if 'times_all' in tv_data:
        times_all  = tv_data['times_all']    # the time corresponding to the inference. Will be cut to be between start and end_time.
        start_time = times_all[0]
    else:
        start_time = 14
        times_all  = np.arange(start_time, start_time + len(site_inf))
        
    if start != start_time:
        site_inf   = site_inf[list(times_all).index(start):]
        times_all  = times_all[list(times_all).index(start):]
        #times_all  = times_all[start-start_time:]
        full_inf   = inf_link[:, site_index[0]]
        #site_inf   = site_inf[start-start_time:]
        start_time = start
        
    if end_time != times_all[-1]:
        d_t        = times_all[-1] - times_all[list(times_all).index(end_time)]
        site_inf   = site_inf[:list(times_all).index(end_time)]
        times_all  = times_all[:list(times_all).index(end_time)]
        
    # getting the times corresponding to the inference for the full time series
    if 'times_all' in tv_data:
        full_times = tv_data['times_all']    # the time corresponding to the full inference
        start_full = full_times[0]
    else:
        start_full = 14
        full_times = np.arange(start_full, start_full + len(full_inf))
    
    # find null distribution
    if not full_tv_file:
        inferred_null = FIND_NULL_DISTRIBUTION(tv_file, link_file)
    else:
        inferred_null = FIND_NULL_DISTRIBUTION(full_tv_file, link_file)
    max_null    = np.amax(inferred_null)
    min_null    = np.amin(inferred_null)
    num_largest = int(round(len(inferred_null) * 2.5 / 100))    # the number of coefficients in the top 2.5% of the null distribution
    soft_cutoff = np.sort(inferred_null)[::-1][num_largest]
    print('soft cutoff =', soft_cutoff)
    
    ### Find when the inferred coefficient exceeds the null distribution
    locs_sep     = [i.split('-')[3] for i in locs]
    #print(np.array(site_times)[np.array(locs_sep)=='lond'])
    uk_index     = locs_sep.index('lond')
    #uk_index     = np.argmax([np.amax(i) for i in site_traj])
    uk_traj      = site_traj[uk_index][:-d_t]
    uk_traj_full = site_traj[uk_index]
    uk_time      = site_times[uk_index]
    #print(uk_time)
    
    # Trying to fix time interval for trajectory
    if True:
        uk_time_new  = np.array(uk_time) + int(window_size/2)
        uk_cutoff    = uk_time_new[list(uk_time_new).index(start_time): list(uk_time_new).index(end_time)+1]
        uk_time      = uk_cutoff
        uk_traj      = uk_traj_full[list(uk_time_new).index(start_time): list(uk_time_new).index(end_time)+1]
    inf_detected  = site_inf[site_inf>max_null][0]
    t_detected    = times_all[site_inf>max_null][0]
    t_soft_detect = times_all[site_inf>soft_cutoff][0]
    #traj_detected = uk_time[list(uk_time).index(t_detected)]
    delta_t = times_all[-1] - t_detected + 1
    soft_delta_t = times_all[-1] - t_soft_detect + 1
    traj_detected = uk_traj[-delta_t]
    #print(t_detected)
    print('hard detection time:', uk_time[-delta_t])
    print('soft detection time:', uk_time[-soft_delta_t])
    print('frequency at detected time:', traj_detected)

    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = SINGLE_COLUMN #SLIDE_WIDTH
    goldh = w
    fig   = plt.figure(figsize=(w, goldh))

    box_null = dict(left=0.15, right=0.95, bottom=0.70, top=0.95)
    box_traj = dict(left=0.15, right=0.95, bottom=0.35, top=0.55)
    box_sel  = dict(left=0.15, right=0.95, bottom=0.12, top=0.32)
    
    ## a -- null distribution of selection coefficients

    gs_null = gridspec.GridSpec(1, 1, **box_null)
    ax_null = plt.subplot(gs_null[0, 0])
    
    print(np.max(inferred_null), len(inferred_null))
    
    histprops = dict(histtype='bar', lw=SIZELINE/2, rwidth=0.8, ls='solid', alpha=0.7, edgecolor='none',
                     orientation='vertical', log=True)
                     
    pprops = { 'xlim':        [-0.02, 0.02],
               'xticks':      [-0.02, -0.01, 0., 0.01, 0.02],
               'xticklabels': [r'$-2$', r'$-1$', r'$0$', r'$1$', r'$2$'],
               'ylim':        [1e0, 1e4],
               'yticks':      [1e0, 1e1, 1e2, 1e3, 1e4],
               #'yticklabels': [0, 10, 20, 30, 40, 50],
               'logy':        True,
               'ylabel':      'Counts',
               'xlabel':      'Inferred selection coefficients for neutral variants (%)',
               'bins':        np.arange(-0.02, 0.02+0.001, 0.001),
               'weights':     [np.ones_like(inferred_null)],
               'plotprops':   histprops,
               'axoffset':    0.1,
               'theme':       'open' }

    x = [inferred_null]
    mp.plot(type='hist', ax=ax_null, x=x, colors=[LCOLOR], **pprops)
    #ax_null.set_yscale('log', nonpositive='clip')
    
    ## b -- frequency trajectory

    gs_traj = gridspec.GridSpec(1, 1, **box_traj)
    ax_traj = plt.subplot(gs_traj[0, 0])
    
    lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1 }
    dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
    
    end_idx = -24
#    end_idx = -66
    
    xticks      = np.arange(full_times[0], full_times[end_idx], 14)
    xticklabels = [(dt.timedelta(days=int(i)) + dt.datetime(2020,1,1)) for i in xticks]
    xticklabels = [f'{i.month}/{i.day}' for i in xticklabels]
    
    pprops = { 'xlim':        [full_times[0], full_times[end_idx]],
               'xticks':      xticks,
               'xticklabels': ['' for xtl in xticklabels],
               'ylim':        [0, 1.05],
               'yticks':      [0, 0.5, 1],
               'yticklabels': [0, 50, 100],
               'yminorticks': [0.25, 0.75],
#               'ylim':        [0, 0.30],
#               'yticks':      [0, 0.1, 0.2, 0.3],
#               'yticklabels': [0, 10, 20, 30],
#               'yminorticks': [0.05, 0.15, 0.25],
               'xlabel':      '',
               'ylabel':      'Variant\nfrequency (%)',
               'axoffset':    0.1,
               'theme':       'open' }

#    xdat = [np.arange(start_time, start_time + len(site_inf))]
#    ydat = [uk_traj[-len(site_inf):]]
    
    xdat = [full_times[-len(uk_traj_full):end_idx] - int(window_size/2)]
    ydat = [uk_traj_full[:end_idx]]
    mp.line(ax=ax_traj, x=xdat, y=ydat, colors=[COLOR_1], plotprops=lineprops, **pprops)
    
    tdetect = 0
    for i in range(len(ydat[0])):
        if ydat[0][i]>0:
            tdetect = xdat[0][i]
            break
    print('First observed at %d, detected selection at %d' % (tdetect, t_detected))

    xdat = [[t_detected, t_detected]]
    ydat = [[0, 1]]
    mp.plot(type='line', ax=ax_traj, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
    
    ## c -- inferred selection coefficient

    gs_sel = gridspec.GridSpec(1, 1, **box_sel)
    ax_sel = plt.subplot(gs_sel[0, 0])
    
    pprops = { 'xlim':        [full_times[0], full_times[end_idx]],
               'xticks':      xticks,
               'xticklabels': xticklabels,
               'ylim':        [0, 0.47],
               'yticks':      [0, 0.20, 0.40],
               'yticklabels': [0, 20, 40],
               'yminorticks': [0.1, 0.3],
#               'ylim':        [0, 0.22],
#               'yticks':      [0, 0.10, 0.20],
#               'yticklabels': [0, 10, 20],
#               'yminorticks': [0.05, 0.15],
               'xlabel':      'Date',
               'ylabel':      'Inferred selection\ncoefficient (%)',
               'axoffset':    0.1,
               'theme':       'open' }
    
    xdat = [full_times[:end_idx]]
    ydat = [full_inf[:end_idx]]
    mp.line(ax=ax_sel, x=xdat, y=ydat, colors=[COLOR_2], plotprops=lineprops, **pprops)

    xdat = [[t_detected, t_detected]]
    ydat = [[0, 1]]
    mp.plot(type='line', ax=ax_sel, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)

    ## legends and stuff
    
    ax_null.text(box_null['left']-0.10, box_null['top']+0.01, 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_traj.text(box_traj['left']-0.10, box_traj['top']+0.01, 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    
    txtprops = dict(ha='left', va='top', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
    ax_traj.text(t_detected+1.5, 0.98, 'Variant first reliably\ninferred to be\nbeneficial', **txtprops)

    # SAVE FIGURE

    plt.savefig('%s/fig-4%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)
    
    
def plot_early_detection_draft(null_file, alpha_file, alpha_start, alpha_end, delta_file, delta_start, delta_end):
    """ Plot the null distribution for mutations inferred to be nearly neutral.
        Plot frequencies and early detection times for Alpha and Delta variants. """
    
    # Load data
    inferred_null = np.loadtxt(null_file)
    df_alpha      = pd.read_csv(alpha_file, comment='#', memory_map=True)
    df_alpha      = df_alpha[(df_alpha['time']>=alpha_start) & (df_alpha['time']<=alpha_end)]
    df_delta      = pd.read_csv(delta_file, comment='#', memory_map=True)
    df_delta      = df_delta[(df_delta['time']>=delta_start) & (df_delta['time']<=delta_end)]
    
    # Null distribution statistics
    max_null    = np.amax(inferred_null)
    min_null    = np.amin(inferred_null)
    num_largest = int(round(len(inferred_null) * 2.5 / 100))    # the number of coefficients in the top 2.5% of the null distribution
    soft_cutoff = np.sort(inferred_null)[::-1][num_largest]
    print('hard w cutoff = %.4f' % max_null)
    print('soft w cutoff = %.4f\n' % soft_cutoff)
    
    # Get early detection times
    
    t_alpha      = df_alpha[df_alpha['selection']>max_null].iloc[0]['time']
    f_alpha      = df_alpha[df_alpha['selection']>max_null].iloc[0]['frequency']
    t_soft_alpha = df_alpha[df_alpha['selection']>soft_cutoff].iloc[0]['time']
    f_soft_alpha = df_alpha[df_alpha['selection']>soft_cutoff].iloc[0]['frequency']
    t_delta      = df_delta[df_delta['selection']>max_null].iloc[0]['time']
    f_delta      = df_delta[df_delta['selection']>max_null].iloc[0]['frequency']
    t_soft_delta = df_delta[df_delta['selection']>soft_cutoff].iloc[0]['time']
    f_soft_delta = df_delta[df_delta['selection']>soft_cutoff].iloc[0]['frequency']
   
    print('time')
    print('cutoff\talpha\tdelta')
    print('hard\t%d\t%d' % (t_alpha, t_delta))
    print('soft\t%d\t%d' % (t_soft_alpha, t_soft_delta))
    
    print('')
    print('frequency')
    print('cutoff\talpha\tdelta')
    print('hard\t%.3f\t%.3f' % (f_alpha, f_delta))
    print('soft\t%.3f\t%.3f' % (f_soft_alpha, f_soft_delta))
    print('')
    
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = DOUBLE_COLUMN #SLIDE_WIDTH
    goldh = w / 3
    fig   = plt.figure(figsize=(w, goldh))

    left_bd   = 0.08
    right_bd  = 0.97
    h_space   = 0.10
    box_h     = (right_bd - left_bd - 2*h_space)/3
    top_bd    = 0.92
    bottom_bd = 0.15
    v_space   = 0.10
    box_v     = (top_bd - bottom_bd - 1*v_space)/2
    
    box_null   = dict(left=left_bd + 0*box_h + 0*h_space, right=left_bd + 1*box_h + 0*h_space, top=top_bd, bottom=bottom_bd)
    box_traj_a = dict(left=left_bd + 1*box_h + 1*h_space, right=left_bd + 2*box_h + 1*h_space, top=top_bd - 0*box_v - 0*v_space, bottom=top_bd - 1*box_v - 0*v_space)
    box_sel_a  = dict(left=left_bd + 1*box_h + 1*h_space, right=left_bd + 2*box_h + 1*h_space, top=top_bd - 1*box_v - 1*v_space, bottom=top_bd - 2*box_v - 1*v_space)
    box_traj_d = dict(left=left_bd + 2*box_h + 2*h_space, right=left_bd + 3*box_h + 2*h_space, top=top_bd - 0*box_v - 0*v_space, bottom=top_bd - 1*box_v - 0*v_space)
    box_sel_d  = dict(left=left_bd + 2*box_h + 2*h_space, right=left_bd + 3*box_h + 2*h_space, top=top_bd - 1*box_v - 1*v_space, bottom=top_bd - 2*box_v - 1*v_space)
    
    ## a -- null distribution of selection coefficients

    gs_null = gridspec.GridSpec(1, 1, **box_null)
    ax_null = plt.subplot(gs_null[0, 0])
    
    histprops = dict(histtype='bar', lw=SIZELINE/2, rwidth=0.8, ls='solid', alpha=1, edgecolor='none',
                     orientation='vertical', log=True)
                     
#    pprops = { 'xlim':        [-0.04, 0.045],
#               'xticks':      [-0.04, -0.02, 0., 0.02, 0.04, 0.045],
#               'xticklabels': [r'$-4$', r'$-2$', r'$0$', r'$2$', r'$4$', ''],
#               'ylim':        [1e0, 1e6],
#               'yticks':      [1e0, 1e2, 1e4, 1e6],
#               #'yticklabels': [0, 10, 20, 30, 40, 50],
#               'logy':        True,
#               'ylabel':      'Counts',
#               'xlabel':      'Inferred selection coefficients for neutral variants, ' + r'$\hat{w}$' + ' (%)',
#               'bins':        np.arange(-0.04, 0.045+0.001, 0.001),
#               'weights':     [np.ones_like(inferred_null)],
#               'plotprops':   histprops,
#               'axoffset':    0.1,
#               'theme':       'open' }

    pprops = { 'xlim':        [-0.10, 0.15],
               'xticks':      [-0.10, -0.05, 0., 0.05, 0.10, 0.15],
               'xticklabels': [r'$-10$', r'$-5$', r'$0$', r'$5$', r'$10$', r'$15$'],
               'ylim':        [1e0, 1e6],
               'yticks':      [1e0, 1e2, 1e4, 1e6],
               #'yticklabels': [0, 10, 20, 30, 40, 50],
               'logy':        True,
               'ylabel':      'Counts',
               'xlabel':      'Inferred selection coefficients for quasi-neutral variants, ' + r'$\hat{w}$' + ' (%)',
               'bins':        np.arange(-0.10, 0.15+0.0025, 0.0025),
               'weights':     [np.ones_like(inferred_null)],
               'plotprops':   histprops,
               'axoffset':    0.1,
               'theme':       'open' }

    x = [inferred_null]
    mp.plot(type='hist', ax=ax_null, x=x, colors=[LCOLOR], **pprops)
    
    # b/c -- Alpha/Delta frequency and inferred selection
    
    gs_traj_a = gridspec.GridSpec(1, 1, **box_traj_a)
    ax_traj_a = plt.subplot(gs_traj_a[0, 0])
    gs_traj_d = gridspec.GridSpec(1, 1, **box_traj_d)
    ax_traj_d = plt.subplot(gs_traj_d[0, 0])
    
    ylaba = 'Alpha frequency\nin London (%)'
    ylabd = 'Delta frequency\nin Great Britain (%)'
    
    gs_sel_a = gridspec.GridSpec(1, 1, **box_sel_a)
    ax_sel_a = plt.subplot(gs_sel_a[0, 0])
    gs_sel_d = gridspec.GridSpec(1, 1, **box_sel_d)
    ax_sel_d = plt.subplot(gs_sel_d[0, 0])
    
    ylima   = [0, 0.60]
    yticka  = [0, 0.30, 0.60]
    ytickla = [int(i) for i in 100*np.array(yticka)]
    ymticka = [0.15, 0.45]
    ylimd   = [0, 0.60]
    ytickd  = [0, 0.30, 0.60]
    ytickld = [int(i) for i in 100*np.array(ytickd)]
    ymtickd = [0.15, 0.45]
    
    for ax_traj, ax_sel, temp_df, t_det, ylabel, ylim, yticks, yticklabels, yminorticks, v_color in [
        [ax_traj_a, ax_sel_a, df_alpha, t_alpha, ylaba, ylima, yticka, ytickla, ymticka, C_ALPHA],
        [ax_traj_d, ax_sel_d, df_delta, t_delta, ylabd, ylimd, ytickd, ytickld, ymtickd, C_DELTA] ]:
    
        ## b/c.1 -- frequency trajectory
        
        times   = np.array(temp_df['time'])
        freqs   = np.array(temp_df['frequency'])
        sels    = np.array(temp_df['selection'])
        
        lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1 }
        dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
        
        xticks      = np.arange(np.min(times), np.max(times), 14)
        xticklabels = [(dt.timedelta(days=int(i)) + dt.datetime(2020,1,1)) for i in xticks]
        xticklabels = [f'{i.month}/{i.day}' for i in xticklabels]
        
        pprops = { 'xlim':        [np.min(times), np.max(times)],
                   'xticks':      xticks,
                   'xticklabels': ['' for xtl in xticklabels],
                   'ylim':        [0, 1.05],
                   'yticks':      [0, 0.5, 1],
                   'yticklabels': [0, 50, 100],
                   'yminorticks': [0.25, 0.75],
                   'xlabel':      '',
                   'ylabel':      ylabel,
                   'axoffset':    0.1,
                   'theme':       'open' }
        
        xdat = [times]
        ydat = [freqs]
        mp.line(ax=ax_traj, x=xdat, y=ydat, colors=[v_color], plotprops=lineprops, **pprops)
        
        tobs = 0
        for i in range(len(ydat[0])):
            if ydat[0][i]>0:
                tobs = xdat[0][i]
                break
        print('First observed at %d, detected selection at %d\n' % (tobs, t_det))

        xdat = [[t_det, t_det]]
        ydat = [[0, 1]]
        mp.plot(type='line', ax=ax_traj, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
        
        ## b/c.2 -- inferred selection coefficient

        pprops = { 'xlim':        [np.min(times), np.max(times)],
                   'xticks':      xticks,
                   'xticklabels': xticklabels,
                   'ylim':        ylim,
                   'yticks':      yticks,
                   'yticklabels': yticklabels,
                   'yminorticks': yminorticks,
                   #'xlabel':      'Date',
                   'ylabel':      'Inferred selection\ncoefficient, ' + r'$\hat{w}$' + ' (%)',
                   'axoffset':    0.1,
                   'theme':       'open' }
        
        xdat = [times]
        ydat = [sels]
        mp.line(ax=ax_sel, x=xdat, y=ydat, colors=[LCOLOR], plotprops=lineprops, **pprops)

        xdat = [[t_det, t_det]]
        ydat = [[0, 1]]
        mp.plot(type='line', ax=ax_sel, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
        
        txtprops = dict(ha='left', va='top', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
        ax_traj.text(t_det+1.5, 0.98, 'Variant first reliably\ninferred to be\nbeneficial', **txtprops)

    ## legends and labels
    
    dx = -0.06
    dy =  0.01
    ax_null.text(  box_null['left']   + dx, box_null['top']   + dy, 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_traj_a.text(box_traj_a['left'] + dx, box_traj_a['top'] + dy, 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_traj_d.text(box_traj_d['left'] + dx, box_traj_d['top'] + dy, 'c'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)

    # SAVE FIGURE

    plt.savefig('%s/fig-5%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)


def plot_selection_statistics_old(infer_file, link_file, link_file_all, syn_file, index_file=None, full_tv_file=None, syn_lower_limit=55):
    """ Makes a plot containing the distribution of inferred coefficients and the enrichment of nonsynonymous mutations.
    Combines selection_dist_plot and syn_plot functions.
    correlation_plots determines whether or not the 3 plots containing the correlations are made."""
    
    # loading and processing the data
    data            = np.load(infer_file, allow_pickle=True)
    linked_sites    = np.load(link_file, allow_pickle=True)        # sites that are fully linked in EVERY region
    linked_anywhere = np.load(link_file_all, allow_pickle=True)    # sites that are fully linked in ANY region
    syn_data        = np.load(syn_file, allow_pickle=True)
    
    allele_number = data['allele_number']
    labels        = [GET_LABEL(i) for i in allele_number]
    types_temp    = syn_data['types']
    type_locs     = syn_data['locations']
    linked_all    = [linked_sites[i][j] for i in range(len(linked_sites)) for j in range(len(linked_sites[i]))]
    inferred      = data['selection']
    labels        = [GET_LABEL(i) for i in data['allele_number']]
    s_link        = np.zeros(len(linked_sites))
    digits        = len(str(len(inferred)))
    print('number of sites:', len(inferred))
    
    mutant_types  = []
    for i in allele_number:
        if i in type_locs:
            mutant_types.append(types_temp[list(type_locs).index(i)])
        else:
            mutant_types.append('unknown')
        
    inferred_new  = []    # the sum of the inferred coefficients for the linked sites
    for i in range(len(linked_sites)):
        for j in range(len(linked_sites[i])):
            if np.any(linked_sites[i][j]==np.array(labels)):
                s_link[i] += inferred[np.where(np.array(linked_sites[i][j])==np.array(labels))[0][0]]
    for i in range(len(labels)):
        if labels[i] not in linked_all:
            inferred_new.append(inferred[i])
    s_link = inferred_new + list(s_link)
    
    # null distribution
    if full_tv_file:
        inferred_null = FIND_NULL_DISTRIBUTION(full_tv_file, link_file)
        
    # find enrichment in nonsynonymous sites
    site_types = []
    for group in linked_anywhere:
        site_types_temp = []
        for site in group:
            if np.any(site == np.array(labels)):
                site_types_temp.append(mutant_types[list(labels).index(site)])
            else:
                site_types_temp.append('null')
        site_types.append(site_types_temp)

    nonsyn_nonlinked  = np.zeros(len(inferred) - 1)
    for i in range(len(inferred)-1):
        nonsyn_nonlinked[i] = NUMBER_NONSYNONYMOUS_NONLINKED(inferred, i+1, linked_anywhere, site_types, labels, mutant_types)
        
    # find the percentage nonsynonymous with selection coefficients between given intervals
    intervals  = np.logspace(-4, 0, num=12)
    percent_ns = []
    for i in range(len(intervals)):
        if i==0:
            idxs_temp  = np.nonzero(np.logical_and(np.fabs(inferred)>0, np.fabs(inferred)<=intervals[i]))
        else:
            idxs_temp  = np.nonzero(np.logical_and(np.fabs(inferred)>intervals[i-1], np.fabs(inferred)<=intervals[i]))
#        if i==0:
#            idxs_temp  = np.nonzero(np.logical_and(inferred>0, inferred<=intervals[i]))
#        else:
#            idxs_temp  = np.nonzero(np.logical_and(inferred>intervals[i-1], inferred<=intervals[i]))
        #idxs_temp  = np.nonzero(np.logical_and(inferred<intervals[i], inferred>=intervals[i+1]))
        sites_temp = np.array(labels)[idxs_temp]
        types_temp = np.array(mutant_types)[idxs_temp]
        num_nonsyn = NUMBER_NONSYNONYMOUS(linked_anywhere, site_types, sites_temp, types_temp)
        percent_ns.append(num_nonsyn)
        
    # change negative values to zeros
    for i in range(len(percent_ns)):
        if percent_ns[i]<0:
            percent_ns[i] = 0
        
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = SINGLE_COLUMN #SLIDE_WIDTH
    goldh = w / 1.1
    fig   = plt.figure(figsize=(w, goldh))

#    box_hist = dict(left=0.15, right=0.55, bottom=0.60, top=0.95)
#    box_sns  = dict(left=0.70, right=0.97, bottom=0.60, top=0.95)
#    box_frac = dict(left=0.15, right=0.72, bottom=0.16, top=0.45)

    box_hist = dict(left=0.15, right=0.95, bottom=0.64, top=0.95)
    box_sns  = dict(left=0.15, right=0.46, bottom=0.15, top=0.45)
    box_frac = dict(left=0.64, right=0.95, bottom=0.16, top=0.45)
    
    ## a -- selection coefficient histogram
    
    ### plot histogram
    
    s_link    = np.array(s_link)
    s_pos_log = np.log10(s_link[s_link>0])
    s_neg_log = np.log10(-s_link[s_link<0])
    
    n_hist = 15
    xmin   = -3
    xmax   = 0
    x_neg  = np.linspace(xmin, xmax, num=n_hist)
    x_pos  = np.linspace(xmin, xmax, num=n_hist)
    y_neg  = []
    y_pos  = []
    y_neu  = []
    for i in range(len(x_neg)-1):
        y_neg.append(np.sum((s_neg_log>x_neg[i]) * (s_neg_log<=x_neg[i+1])))
    y_neg.append(np.sum(s_neg_log>x_neg[-1]))
    y_neu.append(np.sum(s_neg_log<x_neg[0]))
    for i in range(len(x_pos)-1):
        y_pos.append(np.sum((s_pos_log>x_pos[i]) * (s_pos_log<=x_pos[i+1])))
    y_pos.append(np.sum(s_pos_log>x_pos[-1]))
    y_neu.append(np.sum(s_pos_log<x_pos[0]))
    
    norm  = 4
    c_neg = [hls_to_rgb(0.02, 1., 0.83)]
    c_pos = [hls_to_rgb(0.58, 1., 0.60)]
    for i in range(len(y_neg)):
        t = np.min([(x_neg[i] + norm)/norm, 1])
        c_neg.append(hls_to_rgb(0.58, 0.53 * t + 1. * (1 - t), 0.60))
        t = np.min([(x_pos[i] + norm)/norm, 1])
        c_pos.append(hls_to_rgb(0.02, 0.53 * t + 1. * (1 - t), 0.83))
        
    
#    wspace  = 0.20
#    gs_hist = gridspec.GridSpec(1, 3, width_ratios=[n_hist*2/3, 2, n_hist], wspace=wspace, **box_hist)
#
#    hist_props = dict(lw=AXWIDTH/2, width=2.4/n_hist, align='edge', edgecolor=[BKCOLOR], orientation='vertical')
#
#    ### negative coefficient subplot
#
#    ax_neg = plt.subplot(gs_hist[0, 0])
#
#    pprops = { 'colors':      [C_DEL_LT],
#               'xlim':        [xmin, -1][::-1],
#               'xticks':      [-3, -2, -1],
#               'xticklabels': [r'$-0.1$', r'$-1$', r'$-10$'],
#               'ylim':        [0, 750],
#               'yticks':      [0, 250, 500, 750],
#               'ylabel':      'Counts',
#               'hide':        ['top', 'right'] }
#
#    mp.plot(type='bar', ax=ax_neg, x=[x_neg], y=[y_neg], plotprops=hist_props, **pprops)
#
#    ### neutral coefficient subplot
#
#    ax_neu = plt.subplot(gs_hist[0, 1])
#
#    pprops = { 'colors':      [C_NEU_LT],
#               'xlim':        [xmin/n_hist, -xmin/n_hist],
#               'xticks':      [0],
#               'ylim':        [0, 750],
#               'yticks':      [],
#               'hide':        ['top', 'right', 'left'],
#               'xaxstart':    xmin/n_hist,
#               'xaxend':      -xmin/n_hist }
#
#    mp.plot(type='bar', ax=ax_neu, x=[[xmin/n_hist, 0]], y=[y_neu], plotprops=hist_props, **pprops)
#
#    ### positive coefficient subplot
#
#    ax_pos = plt.subplot(gs_hist[0, 2])
#
#    pprops = { 'colors':      [C_BEN_LT],
#               'xlim':        [xmin, xmax],
#               'xticks':      [-3, -2, -1, 0],
#               'xticklabels': [r'$0.1$', r'$1$', r'$10$', r'$100$'],
#               'ylim':        [0, 750],
#               'yticks':      [],
#               'hide':        ['top', 'right', 'left'] }
#
#    mp.plot(type='bar', ax=ax_pos, x=[x_pos], y=[y_pos], plotprops=hist_props, **pprops)


    wspace  = 0.20
    gs_hist = gridspec.GridSpec(1, 2, width_ratios=[(n_hist*2/3)+1, n_hist+1], wspace=wspace, **box_hist)
    
    hist_props = dict(lw=SIZELINE/2, width=2.4/n_hist, align='center', edgecolor=[BKCOLOR], orientation='vertical')
    
    ### negative coefficient subplot
    
    ax_neg = plt.subplot(gs_hist[0, 0])
    
    pprops = { 'colors':      c_neg,
               'xlim':        [xmin-4.5/n_hist, -1][::-1],
               'xticks':      [-3-3/n_hist, -2, -1],
               'xticklabels': ['>-0.1', '-1', '-10'],
               'ylim':        [0, 750],
               'yticks':      [0, 250, 500, 750],
               'ylabel':      'Counts',
               'hide':        ['top', 'right'] }
    
    x_neg = [[-3-3/n_hist]] + [[i] for i in x_neg]
    y_neg = [[y_neu[0]]] + [[i] for i in y_neg]
    
    #x_neg = np.array(x_neg) + 3/n_hist
    
    mp.plot(type='bar', ax=ax_neg, x=x_neg, y=y_neg, plotprops=hist_props, **pprops)
    
    ### positive coefficient subplot
    
    ax_pos = plt.subplot(gs_hist[0, 1])
    
    pprops = { 'colors':      c_pos,
               'xlim':        [xmin-4.5/n_hist, xmax],
               'xticks':      [-3-3/n_hist, -2, -1, 0],
               'xticklabels': ['<0.1', '1', '10', '100'],
               'ylim':        [0, 750],
               'yticks':      [],
               'hide':        ['top', 'right', 'left'] }
               
    x_pos = [[-3-3/n_hist]] + [[i] for i in x_pos]
    y_pos = [[y_neu[1]]] + [[i] for i in y_pos]
    
    #x_pos = np.array(x_pos) + 3/n_hist
    
    mp.plot(type='bar', ax=ax_pos, x=x_pos, y=y_pos, plotprops=hist_props, **pprops)

    ## b -- fraction of nonsynonymous mutations by selection coefficient rank
        
    ### plot lines
    
    gs_sns = gridspec.GridSpec(1, 1, **box_sns)
    ax_sns = plt.subplot(gs_sns[0, 0])
    
    lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1 }
    dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
    
    pprops = { 'xlim':        [1, 5000],
               'ylim':        [0, 1.05],
               'xticks':      [1, 10, 100, 1000, 5000],
               'xticklabels': ['1', '10', '100', '1000', ''],
               'logx':        True,
               'yticks':      [0, 0.5, 1],
               'yticklabels': [0, 50, 100],
               'yminorticks': [0.25, 0.75],
               'xlabel':      'Number of largest\nselection coefficients',
               'ylabel':      'Fraction\nnonsynonymous (%)',
               'axoffset':    0.1,
               'theme':       'open' }

    xdat = [np.arange(len(nonsyn_nonlinked)) + 1]
    ydat = [nonsyn_nonlinked]
    mp.line(ax=ax_sns, x=xdat, y=ydat, colors=[COLOR_2], plotprops=lineprops, **pprops)

    xdat = [np.arange(len(nonsyn_nonlinked)) + 1]
    ydat = [[nonsyn_nonlinked[-1] for i in range(len(nonsyn_nonlinked))]]
    mp.plot(type='line', ax=ax_sns, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
    
    ## c - fraction of nonsynonymous mutations by selection coefficient size
    
    ### plot fractions
    
    gs_frac = gridspec.GridSpec(1, 1, **box_frac)
    ax_frac = plt.subplot(gs_frac[0, 0])
    
    lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1, 'drawstyle': 'steps-post'}
    dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
    histprops = dict(lw=SIZELINE/2, width=0.28, ls='solid', alpha=0.7, edgecolor=[BKCOLOR], orientation='vertical')
    
    pprops = { #'xlim':        [1e-4, 1e-0],
               #'xticks':      [1e-4, 1e-3, 1e-2, 1e-1, 1e0],
               'xlim':        [-4, 0],
               'xticks':      [-4, -3, -2, -1, 0],
               'xticklabels': ['0.01', '0.1', '1', '10', '100'],
               'logx':        False,
               'ylim':        [0, 1.05],
               'yticks':      [0, 0.5, 1],
               'yticklabels': [0, 50, 100],
               'yminorticks': [0.25, 0.75],
               'xlabel':      'Magnitude of selection\ncoefficients (%)',
               'ylabel':      'Fraction\nnonsynonymous (%)',
               'axoffset':    0.1,
               'theme':       'open' }

    xdat = [np.log10(intervals)]
    ydat = [percent_ns]
#    mp.plot(type='line', ax=ax_frac, x=xdat, y=ydat, colors=[COLOR_1], plotprops=lineprops, **pprops)
    mp.plot(type='bar', ax=ax_frac, x=xdat, y=ydat, colors=[COLOR_2], plotprops=histprops, **pprops)

    print('non-synonymous percentage:', percent_ns)
    print('intervals:', intervals)
    
    # labels and legends
    
    ax_sns.text(box_hist['left']-0.11, box_hist['top']+0.01, 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_sns.text(box_sns['left'] -0.11, box_sns['top'] +0.01, 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_sns.text(box_frac['left']-0.11, box_frac['top']+0.01, 'c'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    
    ax_sns.text(box_hist['left'] + (box_hist['right']-box_hist['left'])/2, box_hist['bottom']-0.08, 'Inferred selection coefficients, ' + '$\hat{s}$' + ' (%)',
                ha='center', va='top', transform=fig.transFigure, **DEF_LABELPROPS)
#    ax_sns.text(box_sns['left']  + (box_sns['right'] - box_sns['left'])/2,  box_sns['bottom']-0.08, 'Number of largest\nselection coefficients',
#                ha='center', va='top', transform=fig.transFigure, **DEF_LABELPROPS)
                
#    ax_neg.text(xmin-1.5/n_hist, 740, '$-0.1<\hat{s}$', ha='center', va='bottom', **DEF_LABELPROPS)
#    ax_pos.text(xmin-1.5/n_hist, 710, '$\hat{s}<0.1$', ha='center', va='bottom', **DEF_LABELPROPS)

#    lineprops = { 'lw' : AXWIDTH/2., 'ls' : '-', 'alpha' : 1.0 }
#    pprops    = { 'xlim' : [0, 1], 'xticks' : [], 'ylim' : [0, 1], 'yticks' : [],
#        'hide' : ['top','bottom','left','right'], 'plotprops' : lineprops }
#    txtprops = {'ha' : 'right', 'va' : 'center', 'color' : BKCOLOR, 'family' : FONTFAMILY,
#        'size' : SIZELABEL, 'rotation' : 90, 'transform' : fig.transFigure}
#    ax[0][0].text(box_traj['left']-0.025, box_traj['top'] - (box_traj['top']-box_traj['bottom'])/2., 'Frequency', **txtprops)

#    # Plotting the enrichment of nonsynonymous mutations vs. number of coefficients
#    ax1  = fig.add_subplot(grid[0, 1])
#    ax1.set_ylim(syn_lower_limit, 101)
#    ax1.tick_params(labelsize=TICK_FONTSIZE, width=SPINE_LW, length=2)
#    for line in ['right',  'top']:
#        ax1.spines[line].set_visible(False)
#    for line in ['left', 'bottom']:
#        ax1.spines[line].set_linewidth(SPINE_LW)
#    sns.lineplot(np.arange(len(nonsyn_nonlinked))+1, 100*nonsyn_nonlinked, ax=ax1, lw=1, color=MAIN_COLOR)
#    ax1.axhline(100*nonsyn_nonlinked[-1], lw=1, color=COMP_COLOR, alpha=0.75)
#    ax1.text(0.25, (100*nonsyn_nonlinked[-1]-syn_lower_limit)/(100-syn_lower_limit) - 0.05, 'Background', fontsize=6, transform=ax1.transAxes, ha='center', va='center')
#    ax1.set_xscale('log')
#    ax1.set_xlim(1, len(nonsyn_nonlinked)+1)
#    ax1.set_ylabel('Nonsynonymous (%)', fontsize=AXES_FONTSIZE)
#    ax1.set_xlabel("Number of largest coefficients", fontsize=AXES_FONTSIZE)
#    print('background:', 100*nonsyn_nonlinked[-1])
    
    # SAVE FIGURE

    plt.savefig('%s/fig-2%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)


def plot_variant_selection_extended_old(variant_file, trajectory_file, variant_list, variant_names, selection_file, label2ddr=[]):
    """ Map out mutations in the major variants, their aggregate inferred selection coefficients, and
        frequency trajectories across regions. """
        
    # Load data
    df_var = pd.read_csv(variant_file, comment='#', memory_map=True)
    df_sel = 0
    if len(variant_list)>0:
        df_sel = df_var[df_var.variant_names.isin(variant_list)]
        temp_var_list  = list(df_sel.variant_names)
        temp_var_names = []
        for i in range(len(temp_var_list)):
            temp_var_names.append(variant_names[variant_list.index(temp_var_list[i])])
        variant_list  = np.array(temp_var_list)
        variant_names = np.array(temp_var_names)
    else:
        df_sel = df_var[np.fabs(df_var.selection_coefficient)>s_cutoff]
        variant_list  = np.array(list(df_sel.variant_names))
        variant_names = np.array(variant_list)
    
    s_sort = np.argsort(np.fabs(df_sel.selection_coefficient))[::-1]
    print(np.array(np.fabs(df_sel.selection_coefficient))[s_sort])
    print(np.array(df_sel.variant_names)[s_sort])
    
    n_vars        = len(s_sort)
    variant_list  = variant_list[s_sort]
    variant_names = variant_names[s_sort]
    
    df_traj = pd.read_csv(trajectory_file, comment='#', memory_map=True)
    df_traj = df_traj[df_traj.variant_names.isin(variant_list)]
    
    # PLOT FIGURE
    
    ## set up figure grid
    
    w       = DOUBLE_COLUMN #SLIDE_WIDTH
    hshrink = 0.5
    goldh   = w * hshrink
    fig     = plt.figure(figsize=(w, goldh))

    box_traj = dict(left=0.06, right=0.45, bottom=0.14, top=0.95)
    box_circ = dict(left=0.95-0.85*hshrink, right=0.95, bottom=0.10, top=0.95)

    gs_traj = gridspec.GridSpec(n_vars, 2, width_ratios=[2, 1], wspace=0.05, **box_traj)
    gs_circ = gridspec.GridSpec(1, 1, width_ratios=[1.0], height_ratios=[1.0], **box_circ)
    
    ### trajectories
    
    ax = [[plt.subplot(gs_traj[i, 0]), plt.subplot(gs_traj[i, 1])] for i in range(n_vars)]
    
    var_colors = sns.husl_palette(n_vars)
    
    legendprops = { 'loc' : 4, 'frameon' : False, 'scatterpoints' : 1, 'handletextpad' : 0.1,
                    'prop' : {'size' : SIZELABEL}, 'ncol' : 1 }
    lineprops   = { 'lw' : SIZELINE, 'linestyle' : '-', 'alpha' : 0.5 }
    #fillprops   = { 'lw' : 0, 'alpha' : 0.3, 'interpolate' : True }
    
    pprops = { 'xticks' : [],
               'yticks' : [],
               'hide'   : ['top', 'bottom', 'left', 'right'],
               'theme'  : 'open' }
    
    t_max = 600
    xticks      = [      61,      153,      245,      336,      426,      518, 600]
    xticklabels = ['Mar 20', 'Jun 20', 'Sep 20', 'Dec 20', 'Mar 21', 'Jun 21',  '']
    
    for i in range(n_vars):
        idx = list(s_sort)[i]
        pprops['colors'] = [var_colors[i]]
        pprops['xlim']   = [   61, t_max]
        pprops['ylim']   = [-0.05,  1.05]
        if (i==n_vars-1):
            pprops['xticks']      = xticks
            pprops['xticklabels'] = xticklabels
            pprops['hide']        = ['top', 'left', 'right']
            pprops['axoffset']    = 0.18
        df_temp = df_traj[df_traj.variant_names==df_sel.iloc[idx].variant_names]
        for k in range(len(df_temp)):
            entry = df_temp.iloc[k]
            times = np.array(str(entry.times).split(), float)
            freqs = np.array(str(entry.frequencies).split(), float)
            if k==len(df_temp)-1:
                mp.plot(type='line', ax=ax[i][0], x=[times], y=[freqs], plotprops=lineprops, **pprops)
            else:
                mp.line(             ax=ax[i][0], x=[times], y=[freqs], plotprops=lineprops, **pprops)
            
        txtprops = dict(ha='left', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
        if variant_names[i]=='B.1':
            ax[i][0].text(101, 0.1, variant_names[i], **txtprops)
        else:
            ax[i][0].text( 61, 0.8, variant_names[i], **txtprops)
    
    txtprops = dict(ha='center', va='center', rotation=90, color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL, clip_on=False)
    ax[-1][0].text(box_traj['left']-0.04, box_traj['top']-(box_traj['top']-box_traj['bottom'])/2, 'Frequency', transform=fig.transFigure, **txtprops)
            
    ### selection coefficient estimates
    
    dashlineprops = dict(lw=SIZELINE, ls=':', alpha=0.25, clip_on=False)
    sprops = dict(lw=0, s=9., marker='o')
    
    pprops = { 'yticks': [],
               'xticks': [],
               'hide'  : ['top', 'bottom', 'left', 'right'],
               'theme' : 'open' }

    xticks      = [0, 0.25, 0.5, 0.75, 1.0]
    xticklabels = [0, 25, 50, 75, 100]
    for i in range(n_vars):
        idx = list(s_sort)[i]
        pprops['xlim'] = [   0,   1]
        pprops['ylim'] = [ 0.5, 1.5]
        ydat           = [1]
        xdat           = [df_sel.iloc[idx].selection_coefficient]
        xerr           = [df_sel.iloc[idx].standard_deviation]
        if (i==n_vars-1):
            pprops['xticks']      = xticks
            pprops['xticklabels'] = xticklabels
            pprops['xlabel']      = 'Inferred selection\ncoefficient, ' + r'$\hat{s}$' + ' (%)'
            pprops['hide']        = ['top', 'left', 'right']
            pprops['axoffset']    = 0.3
        mp.plot(type='error', ax=ax[i][1], x=[xdat], y=[ydat], xerr=[xerr], colors=[var_colors[i]], **pprops)
        
    for i in range(len(xticks)):
        xdat = [xticks[i], xticks[i]]
        ydat = [0.5, n_vars+2.0]
        mp.line(ax=ax[-1][1], x=[xdat], y=[ydat], colors=[BKCOLOR], plotprops=dashlineprops)
    
    ## circle plot

    ax_circ = plt.subplot(gs_circ[0, 0])

    df_sel = pd.read_csv(selection_file, comment='#', memory_map=True)
    
    sig_s, sig_site_real, sig_nuc_idx = plot_circle_formatter(ax_circ, df_sel, label2ddr)

    # MAKE LEGEND

    invt = ax_circ.transData.inverted()
    xy1  = invt.transform((0,0))
    xy2  = invt.transform((0,9))
    
    coef_legend_x  = 0.60
    coef_legend_dx = 0.05
    coef_legend_y  = -0.89
    coef_legend_dy = (xy1[1]-xy2[1])

    txtprops = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
    ex_s     = [-0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04]
    show_s   = [    1,     0,     0,     0, 1,    0,    0,    0,    1]
    c_s      = [C_DEL, C_BEN]
    for i in range(len(ex_s)):
        plotprops = dict(lw=0, marker='o', s=np.fabs(ex_s[i])*S_MULT, clip_on=False)
        mp.scatter(ax=ax_circ, x=[[coef_legend_x + i*coef_legend_dx]], y=[[coef_legend_y]], colors=[c_s[ex_s[i]>0]], plotprops=plotprops)
        if show_s[i]:
            ax_circ.text(coef_legend_x + i*coef_legend_dx, coef_legend_y + 0.75*coef_legend_dy, '%d' % (100*ex_s[i]), **txtprops)
    ax_circ.text(coef_legend_x + len(ex_s)*coef_legend_dx/2, coef_legend_y + (2.25*coef_legend_dy), 'Inferred selection\ncoefficient, $\hat{s}$ (%)', **txtprops)
    
    ax[0][0].text(box_traj['left']-0.02, box_traj['top'], 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_circ.text( box_circ['left']-0.02, box_circ['top'], 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)

    # SAVE FIGURE

    plt.savefig('%s/fig-3-circle%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)


def plot_selection_statistics_extended_old(selection_file_all, selection_file_ns, label2ddr=[]):
    """ Makes a plot containing the distribution of inferred coefficients and the enrichment of nonsynonymous mutations.
    Combines selection_dist_plot and syn_plot functions.
    correlation_plots determines whether or not the 3 plots containing the correlations are made."""
    
    # loading and processing the data
    df_sel_all = pd.read_csv(selection_file_all, comment='#', memory_map=True)
        
    # find enrichment in nonsynonymous sites
    ns_linked = np.array(df_sel_all['synonymous']=='NS') | np.array(df_sel_all['type of linked group']=='NS')
    df_sel_all['ns_linked'] = ns_linked
    
    s_sort = np.argsort(np.fabs(df_sel_all['selection coefficient']))[::-1]
    ns_link_sorted = ns_linked[s_sort]
    print('Top coefficient: %.3f' % df_sel_all.iloc[list(s_sort)[0]]['selection coefficient'])
    
#    s_sort = np.argsort(np.fabs(df_sel_all['total coefficient for linked group']))[::-1]
#    ns_link_sorted = ns_linked[s_sort]
#    print('Top coefficient: %.3f' % df_sel_all.iloc[list(s_sort)[0]]['total coefficient for linked group'])
    
    fraction_ns = np.zeros(len(ns_link_sorted))
    for i in range(len(ns_link_sorted)):
        num = np.sum(ns_link_sorted[:i+1])
        den = i+1
        fraction_ns[i] = num / den
        
    # find the percentage nonsynonymous with selection coefficients between given intervals
    intervals  = np.logspace(-4, -1, num=12)
    percent_ns = []
    for i in range(len(intervals)):
        df_temp = 0
        if i==0:
            df_temp = df_sel_all[np.fabs(df_sel_all['selection coefficient'])<=intervals[i]]
        else:
            df_temp = df_sel_all[(np.fabs(df_sel_all['selection coefficient'])<=intervals[i]) & (np.fabs(df_sel_all['selection coefficient'])>intervals[i-1])]
#        if i==0:
#            df_temp = df_sel_all[np.fabs(df_sel_all['total coefficient for linked group'])<=intervals[i]]
#        else:
#            df_temp = df_sel_all[(np.fabs(df_sel_all['total coefficient for linked group'])<=intervals[i]) & (np.fabs(df_sel_all['total coefficient for linked group'])>intervals[i-1])]
        percent_ns.append(np.sum(df_temp['ns_linked'])/len(df_temp))
        
    # PLOT FIGURE
    
    ## set up figure grid
    
    w       = DOUBLE_COLUMN #SLIDE_WIDTH
    hshrink = 0.5
    goldh   = w * hshrink
    fig     = plt.figure(figsize=(w, goldh))

    box_hist = dict(left=0.07, right=0.45, bottom=0.64, top=0.95)
    box_sns  = dict(left=0.07, right=0.22, bottom=0.15, top=0.45)
    box_frac = dict(left=0.30, right=0.45, bottom=0.16, top=0.45)
    box_circ = dict(left=0.95-0.85*hshrink, right=0.95, bottom=0.10, top=0.95)
    
    ## a -- selection coefficient histogram
    
    ### plot histogram
    
    s_link    = np.array(df_sel_all['selection coefficient'])
    s_pos_log = np.log10(s_link[s_link>0])
    s_neg_log = np.log10(-s_link[s_link<0])
    
    n_hist = 15
    xmin   = -3
    xmax   = -1
    x_neg  = np.linspace(xmin, xmax, num=n_hist)
    x_pos  = np.linspace(xmin, xmax, num=n_hist)
    y_neg  = []
    y_pos  = []
    y_neu  = []
    for i in range(len(x_neg)-1):
        y_neg.append(np.sum((s_neg_log>x_neg[i]) * (s_neg_log<=x_neg[i+1])))
    y_neg.append(np.sum(s_neg_log>x_neg[-1]))
    y_neu.append(np.sum(s_neg_log<x_neg[0]))
    for i in range(len(x_pos)-1):
        y_pos.append(np.sum((s_pos_log>x_pos[i]) * (s_pos_log<=x_pos[i+1])))
    y_pos.append(np.sum(s_pos_log>x_pos[-1]))
    y_neu.append(np.sum(s_pos_log<x_pos[0]))
    
    norm  = 4
    c_neg = [hls_to_rgb(0.02, 1., 0.83)]
    c_pos = [hls_to_rgb(0.58, 1., 0.60)]
    for i in range(len(y_neg)):
        t = np.min([(x_neg[i] + norm)/norm, 1])
        c_neg.append(hls_to_rgb(0.58, 0.53 * t + 1. * (1 - t), 0.60))
        t = np.min([(x_pos[i] + norm)/norm, 1])
        c_pos.append(hls_to_rgb(0.02, 0.53 * t + 1. * (1 - t), 0.83))
        
    wspace  = 0.20
#    gs_hist = gridspec.GridSpec(1, 2, width_ratios=[(n_hist*2/3)+1, n_hist+1], wspace=wspace, **box_hist)
    gs_hist = gridspec.GridSpec(1, 2, width_ratios=[1, 1], wspace=wspace, **box_hist)
    
    hist_props = dict(lw=SIZELINE/2, width=1.5/n_hist, align='center', edgecolor=[BKCOLOR], orientation='vertical')
    
    ### negative coefficient subplot
    
    ax_neg = plt.subplot(gs_hist[0, 0])
    
    pprops = { 'colors':      c_neg,
               'xlim':        [xmin-4.5/n_hist, -1][::-1],
               'xticks':      [-3-3/n_hist, -2, -1],
               'xticklabels': ['>-0.1', '-1', '-10'],
               'logy':        True,
               'ylim':        [1, 10000],
               'yticks':      [1, 10, 100, 1000, 10000],
               'ylabel':      'Counts',
               'hide':        ['top', 'right'] }
    
    x_neg = [[-3-2/n_hist]] + [[i] for i in x_neg]
    y_neg = [[y_neu[0]]] + [[i] for i in y_neg]
    
    mp.plot(type='bar', ax=ax_neg, x=x_neg, y=y_neg, plotprops=hist_props, **pprops)
    
    ### positive coefficient subplot
    
    ax_pos = plt.subplot(gs_hist[0, 1])
    
    pprops = { 'colors':      c_pos,
               'xlim':        [xmin-4.5/n_hist, -1],
               'xticks':      [-3-3/n_hist, -2, -1],
               'xticklabels': ['<0.1', '1', '10'],
               'logy':        True,
               'ylim':        [1, 10000],
               'yticks':      [],
               'hide':        ['top', 'right', 'left'] }
               
    x_pos = [[-3-2/n_hist]] + [[i] for i in x_pos]
    y_pos = [[y_neu[1]]] + [[i] for i in y_pos]
    
    mp.plot(type='bar', ax=ax_pos, x=x_pos, y=y_pos, plotprops=hist_props, **pprops)

    ## b -- fraction of nonsynonymous mutations by selection coefficient rank
        
    ### plot lines
    
    gs_sns = gridspec.GridSpec(1, 1, **box_sns)
    ax_sns = plt.subplot(gs_sns[0, 0])
    
    lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1 }
    dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
    
    print(len(df_sel_all))
    
    pprops = { 'xlim':        [1, len(df_sel_all)],
               'ylim':        [0.5, 1.05],
               'xticks':      [1, 100, 10000],
               'xminorticks': [10, 1000],
               'xminorticklabels': ['', ''],
               'xticklabels': ['1', '100', '10000'],
               'logx':        True,
               'yticks':      [0.5, 1],
               'yticklabels': [50, 100],
               'yminorticks': [0.75],
               'xlabel':      'Number of largest\nselection coefficients',
               'ylabel':      'Fraction\nnonsynonymous (%)',
               'axoffset':    0.1,
               'theme':       'open' }

    xdat = [np.arange(len(df_sel_all)) + 1]
    ydat = [fraction_ns]
    mp.line(ax=ax_sns, x=xdat, y=ydat, colors=[COLOR_2], plotprops=lineprops, **pprops)

    xdat = [[0, len(df_sel_all) + 1]]
    ydat = [[fraction_ns[-1], fraction_ns[-1]]]
    mp.plot(type='line', ax=ax_sns, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
    
    ## c - fraction of nonsynonymous mutations by selection coefficient size
    
    ### plot fractions
    
    gs_frac = gridspec.GridSpec(1, 1, **box_frac)
    ax_frac = plt.subplot(gs_frac[0, 0])
    
    lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1, 'drawstyle': 'steps-post'}
    dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
    histprops = dict(lw=SIZELINE/2, width=0.20, ls='solid', alpha=0.7, edgecolor=[BKCOLOR], orientation='vertical')
    
    pprops = { #'xlim':        [1e-4, 1e-0],
               #'xticks':      [1e-4, 1e-3, 1e-2, 1e-1, 1e0],
               'xlim':        [-4.2, -0.8],
               'xticks':      [-4, -3, -2, -1],
               'xticklabels': ['0.01', '0.1', '1', '10'],
               'logx':        False,
               'ylim':        [0, 1.05],
               'yticks':      [0, 0.5, 1],
               'yticklabels': [0, 50, 100],
               'yminorticks': [0.25, 0.75],
               'xlabel':      'Magnitude of selection\ncoefficients (%)',
               'ylabel':      'Fraction\nnonsynonymous (%)',
               'axoffset':    0.1,
               'theme':       'open' }

    xdat = [np.log10(intervals)]
    ydat = [percent_ns]
#    mp.plot(type='line', ax=ax_frac, x=xdat, y=ydat, colors=[COLOR_1], plotprops=lineprops, **pprops)
    mp.plot(type='bar', ax=ax_frac, x=xdat, y=ydat, colors=[COLOR_2], plotprops=histprops, **pprops)

    print('non-synonymous percentage:', percent_ns)
    print('intervals:', intervals)
    
    # labels and legends
    
    ax_sns.text(box_hist['left'] + (box_hist['right']-box_hist['left'])/2, box_hist['bottom']-0.08, 'Inferred selection coefficients, ' + '$\hat{s}$' + ' (%)',
                ha='center', va='top', transform=fig.transFigure, **DEF_LABELPROPS)
    
    ## circle plot

    gs_circ = gridspec.GridSpec(1, 1, width_ratios=[1.0], height_ratios=[1.0], **box_circ)
    ax_circ = plt.subplot(gs_circ[0, 0])

    df_sel = pd.read_csv(selection_file_ns, comment='#', memory_map=True)
    
    sig_s, sig_site_real, sig_nuc_idx = plot_circle_formatter(ax_circ, df_sel, label2ddr)

    # MAKE LEGEND

    invt = ax_circ.transData.inverted()
    xy1  = invt.transform((0,0))
    xy2  = invt.transform((0,9))
    
    coef_legend_x  = 0.60
    coef_legend_dx = 0.05
    coef_legend_y  = -0.89
    coef_legend_dy = (xy1[1]-xy2[1])

    txtprops = dict(ha='center', va='center', color=BKCOLOR, family=FONTFAMILY, size=SIZELABEL)
    ex_s     = [-0.05, -0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04, 0.05]
    show_s   = [    1,     0,     0,     0,     0, 1,    0,    0,    0,    0,    1]
    c_s      = [C_DEL, C_BEN]
    for i in range(len(ex_s)):
        plotprops = dict(lw=0, marker='o', s=(np.fabs(ex_s[i]) - DS_NORM)*S_MULT if ex_s[i]!=0 else 0, clip_on=False)
        mp.scatter(ax=ax_circ, x=[[coef_legend_x + i*coef_legend_dx]], y=[[coef_legend_y]], colors=[c_s[ex_s[i]>0]], plotprops=plotprops)
        if show_s[i]:
            ax_circ.text(coef_legend_x + i*coef_legend_dx, coef_legend_y + 0.75*coef_legend_dy, '%d' % (100*ex_s[i]), **txtprops)
    ax_circ.text(coef_legend_x + len(ex_s)*coef_legend_dx/2, coef_legend_y + (2.25*coef_legend_dy), 'Inferred selection\ncoefficient, $\hat{s}$ (%)', **txtprops)
    
    ax_sns.text( box_hist['left']-0.05, box_hist['top']+0.01, 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_sns.text( box_sns['left'] -0.05, box_sns['top'] +0.01, 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_sns.text( box_frac['left']-0.05, box_frac['top']+0.01, 'c'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_circ.text(box_circ['left']-0.01, box_circ['top']+0.01, 'd'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    
    # SAVE FIGURE

    plt.savefig('%s/fig-2-circle%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)

def plot_selection_statistics_old(infer_file, link_file, link_file_all, syn_file, index_file=None, full_tv_file=None, syn_lower_limit=55):
    """ Makes a plot containing the distribution of inferred coefficients and the enrichment of nonsynonymous mutations.
    Combines selection_dist_plot and syn_plot functions.
    correlation_plots determines whether or not the 3 plots containing the correlations are made."""
    
    # loading and processing the data
    data            = np.load(infer_file, allow_pickle=True)
    linked_sites    = np.load(link_file, allow_pickle=True)        # sites that are fully linked in EVERY region
    linked_anywhere = np.load(link_file_all, allow_pickle=True)    # sites that are fully linked in ANY region
    syn_data        = np.load(syn_file, allow_pickle=True)
    
    allele_number = data['allele_number']
    labels        = [GET_LABEL(i) for i in allele_number]
    types_temp    = syn_data['types']
    type_locs     = syn_data['locations']
    linked_all    = [linked_sites[i][j] for i in range(len(linked_sites)) for j in range(len(linked_sites[i]))]
    inferred      = data['selection']
    labels        = [GET_LABEL(i) for i in data['allele_number']]
    s_link        = np.zeros(len(linked_sites))
    digits        = len(str(len(inferred)))
    print('number of sites:', len(inferred))
    
    mutant_types  = []
    for i in allele_number:
        if i in type_locs:
            mutant_types.append(types_temp[list(type_locs).index(i)])
        else:
            mutant_types.append('unknown')
        
    inferred_new  = []    # the sum of the inferred coefficients for the linked sites
    for i in range(len(linked_sites)):
        for j in range(len(linked_sites[i])):
            if np.any(linked_sites[i][j]==np.array(labels)):
                s_link[i] += inferred[np.where(np.array(linked_sites[i][j])==np.array(labels))[0][0]]
    for i in range(len(labels)):
        if labels[i] not in linked_all:
            inferred_new.append(inferred[i])
    s_link = inferred_new + list(s_link)
    
    # null distribution
    if full_tv_file:
        inferred_null = FIND_NULL_DISTRIBUTION(full_tv_file, link_file)
        
    # find enrichment in nonsynonymous sites
    site_types = []
    for group in linked_anywhere:
        site_types_temp = []
        for site in group:
            if np.any(site == np.array(labels)):
                site_types_temp.append(mutant_types[list(labels).index(site)])
            else:
                site_types_temp.append('null')
        site_types.append(site_types_temp)

    nonsyn_nonlinked  = np.zeros(len(inferred) - 1)
    for i in range(len(inferred)-1):
        nonsyn_nonlinked[i] = NUMBER_NONSYNONYMOUS_NONLINKED(inferred, i+1, linked_anywhere, site_types, labels, mutant_types)
        
    # find the percentage nonsynonymous with selection coefficients between given intervals
    intervals  = np.logspace(-4, 0, num=12)
    percent_ns = []
    for i in range(len(intervals)):
        if i==0:
            idxs_temp  = np.nonzero(np.logical_and(np.fabs(inferred)>0, np.fabs(inferred)<=intervals[i]))
        else:
            idxs_temp  = np.nonzero(np.logical_and(np.fabs(inferred)>intervals[i-1], np.fabs(inferred)<=intervals[i]))
#        if i==0:
#            idxs_temp  = np.nonzero(np.logical_and(inferred>0, inferred<=intervals[i]))
#        else:
#            idxs_temp  = np.nonzero(np.logical_and(inferred>intervals[i-1], inferred<=intervals[i]))
        #idxs_temp  = np.nonzero(np.logical_and(inferred<intervals[i], inferred>=intervals[i+1]))
        sites_temp = np.array(labels)[idxs_temp]
        types_temp = np.array(mutant_types)[idxs_temp]
        num_nonsyn = NUMBER_NONSYNONYMOUS(linked_anywhere, site_types, sites_temp, types_temp)
        percent_ns.append(num_nonsyn)
        
    # change negative values to zeros
    for i in range(len(percent_ns)):
        if percent_ns[i]<0:
            percent_ns[i] = 0
        
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = SINGLE_COLUMN #SLIDE_WIDTH
    goldh = w / 1.1
    fig   = plt.figure(figsize=(w, goldh))

#    box_hist = dict(left=0.15, right=0.55, bottom=0.60, top=0.95)
#    box_sns  = dict(left=0.70, right=0.97, bottom=0.60, top=0.95)
#    box_frac = dict(left=0.15, right=0.72, bottom=0.16, top=0.45)

    box_hist = dict(left=0.15, right=0.95, bottom=0.64, top=0.95)
    box_sns  = dict(left=0.15, right=0.46, bottom=0.15, top=0.45)
    box_frac = dict(left=0.64, right=0.95, bottom=0.16, top=0.45)
    
    ## a -- selection coefficient histogram
    
    ### plot histogram
    
    s_link    = np.array(s_link)
    s_pos_log = np.log10(s_link[s_link>0])
    s_neg_log = np.log10(-s_link[s_link<0])
    
    n_hist = 15
    xmin   = -3
    xmax   = 0
    x_neg  = np.linspace(xmin, xmax, num=n_hist)
    x_pos  = np.linspace(xmin, xmax, num=n_hist)
    y_neg  = []
    y_pos  = []
    y_neu  = []
    for i in range(len(x_neg)-1):
        y_neg.append(np.sum((s_neg_log>x_neg[i]) * (s_neg_log<=x_neg[i+1])))
    y_neg.append(np.sum(s_neg_log>x_neg[-1]))
    y_neu.append(np.sum(s_neg_log<x_neg[0]))
    for i in range(len(x_pos)-1):
        y_pos.append(np.sum((s_pos_log>x_pos[i]) * (s_pos_log<=x_pos[i+1])))
    y_pos.append(np.sum(s_pos_log>x_pos[-1]))
    y_neu.append(np.sum(s_pos_log<x_pos[0]))
    
    norm  = 4
    c_neg = [hls_to_rgb(0.02, 1., 0.83)]
    c_pos = [hls_to_rgb(0.58, 1., 0.60)]
    for i in range(len(y_neg)):
        t = np.min([(x_neg[i] + norm)/norm, 1])
        c_neg.append(hls_to_rgb(0.58, 0.53 * t + 1. * (1 - t), 0.60))
        t = np.min([(x_pos[i] + norm)/norm, 1])
        c_pos.append(hls_to_rgb(0.02, 0.53 * t + 1. * (1 - t), 0.83))
        
    
#    wspace  = 0.20
#    gs_hist = gridspec.GridSpec(1, 3, width_ratios=[n_hist*2/3, 2, n_hist], wspace=wspace, **box_hist)
#
#    hist_props = dict(lw=AXWIDTH/2, width=2.4/n_hist, align='edge', edgecolor=[BKCOLOR], orientation='vertical')
#
#    ### negative coefficient subplot
#
#    ax_neg = plt.subplot(gs_hist[0, 0])
#
#    pprops = { 'colors':      [C_DEL_LT],
#               'xlim':        [xmin, -1][::-1],
#               'xticks':      [-3, -2, -1],
#               'xticklabels': [r'$-0.1$', r'$-1$', r'$-10$'],
#               'ylim':        [0, 750],
#               'yticks':      [0, 250, 500, 750],
#               'ylabel':      'Counts',
#               'hide':        ['top', 'right'] }
#
#    mp.plot(type='bar', ax=ax_neg, x=[x_neg], y=[y_neg], plotprops=hist_props, **pprops)
#
#    ### neutral coefficient subplot
#
#    ax_neu = plt.subplot(gs_hist[0, 1])
#
#    pprops = { 'colors':      [C_NEU_LT],
#               'xlim':        [xmin/n_hist, -xmin/n_hist],
#               'xticks':      [0],
#               'ylim':        [0, 750],
#               'yticks':      [],
#               'hide':        ['top', 'right', 'left'],
#               'xaxstart':    xmin/n_hist,
#               'xaxend':      -xmin/n_hist }
#
#    mp.plot(type='bar', ax=ax_neu, x=[[xmin/n_hist, 0]], y=[y_neu], plotprops=hist_props, **pprops)
#
#    ### positive coefficient subplot
#
#    ax_pos = plt.subplot(gs_hist[0, 2])
#
#    pprops = { 'colors':      [C_BEN_LT],
#               'xlim':        [xmin, xmax],
#               'xticks':      [-3, -2, -1, 0],
#               'xticklabels': [r'$0.1$', r'$1$', r'$10$', r'$100$'],
#               'ylim':        [0, 750],
#               'yticks':      [],
#               'hide':        ['top', 'right', 'left'] }
#
#    mp.plot(type='bar', ax=ax_pos, x=[x_pos], y=[y_pos], plotprops=hist_props, **pprops)


    wspace  = 0.20
    gs_hist = gridspec.GridSpec(1, 2, width_ratios=[(n_hist*2/3)+1, n_hist+1], wspace=wspace, **box_hist)
    
    hist_props = dict(lw=SIZELINE/2, width=2.4/n_hist, align='center', edgecolor=[BKCOLOR], orientation='vertical')
    
    ### negative coefficient subplot
    
    ax_neg = plt.subplot(gs_hist[0, 0])
    
    pprops = { 'colors':      c_neg,
               'xlim':        [xmin-4.5/n_hist, -1][::-1],
               'xticks':      [-3-3/n_hist, -2, -1],
               'xticklabels': ['>-0.1', '-1', '-10'],
               'ylim':        [0, 750],
               'yticks':      [0, 250, 500, 750],
               'ylabel':      'Counts',
               'hide':        ['top', 'right'] }
    
    x_neg = [[-3-3/n_hist]] + [[i] for i in x_neg]
    y_neg = [[y_neu[0]]] + [[i] for i in y_neg]
    
    #x_neg = np.array(x_neg) + 3/n_hist
    
    mp.plot(type='bar', ax=ax_neg, x=x_neg, y=y_neg, plotprops=hist_props, **pprops)
    
    ### positive coefficient subplot
    
    ax_pos = plt.subplot(gs_hist[0, 1])
    
    pprops = { 'colors':      c_pos,
               'xlim':        [xmin-4.5/n_hist, xmax],
               'xticks':      [-3-3/n_hist, -2, -1, 0],
               'xticklabels': ['<0.1', '1', '10', '100'],
               'ylim':        [0, 750],
               'yticks':      [],
               'hide':        ['top', 'right', 'left'] }
               
    x_pos = [[-3-3/n_hist]] + [[i] for i in x_pos]
    y_pos = [[y_neu[1]]] + [[i] for i in y_pos]
    
    #x_pos = np.array(x_pos) + 3/n_hist
    
    mp.plot(type='bar', ax=ax_pos, x=x_pos, y=y_pos, plotprops=hist_props, **pprops)

    ## b -- fraction of nonsynonymous mutations by selection coefficient rank
        
    ### plot lines
    
    gs_sns = gridspec.GridSpec(1, 1, **box_sns)
    ax_sns = plt.subplot(gs_sns[0, 0])
    
    lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1 }
    dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
    
    pprops = { 'xlim':        [1, 5000],
               'ylim':        [0, 1.05],
               'xticks':      [1, 10, 100, 1000, 5000],
               'xticklabels': ['1', '10', '100', '1000', ''],
               'logx':        True,
               'yticks':      [0, 0.5, 1],
               'yticklabels': [0, 50, 100],
               'yminorticks': [0.25, 0.75],
               'xlabel':      'Number of largest\nselection coefficients',
               'ylabel':      'Fraction\nnonsynonymous (%)',
               'axoffset':    0.1,
               'theme':       'open' }

    xdat = [np.arange(len(nonsyn_nonlinked)) + 1]
    ydat = [nonsyn_nonlinked]
    mp.line(ax=ax_sns, x=xdat, y=ydat, colors=[COLOR_2], plotprops=lineprops, **pprops)

    xdat = [np.arange(len(nonsyn_nonlinked)) + 1]
    ydat = [[nonsyn_nonlinked[-1] for i in range(len(nonsyn_nonlinked))]]
    mp.plot(type='line', ax=ax_sns, x=xdat, y=ydat, colors=[BKCOLOR], plotprops=dashprops, **pprops)
    
    ## c - fraction of nonsynonymous mutations by selection coefficient size
    
    ### plot fractions
    
    gs_frac = gridspec.GridSpec(1, 1, **box_frac)
    ax_frac = plt.subplot(gs_frac[0, 0])
    
    lineprops = {'lw': 2*SIZELINE, 'ls': '-', 'alpha': 1, 'drawstyle': 'steps-post'}
    dashprops = {'lw': 2*SIZELINE, 'ls': ':', 'alpha': 0.5 }
    histprops = dict(lw=SIZELINE/2, width=0.28, ls='solid', alpha=0.7, edgecolor=[BKCOLOR], orientation='vertical')
    
    pprops = { #'xlim':        [1e-4, 1e-0],
               #'xticks':      [1e-4, 1e-3, 1e-2, 1e-1, 1e0],
               'xlim':        [-4, 0],
               'xticks':      [-4, -3, -2, -1, 0],
               'xticklabels': ['0.01', '0.1', '1', '10', '100'],
               'logx':        False,
               'ylim':        [0, 1.05],
               'yticks':      [0, 0.5, 1],
               'yticklabels': [0, 50, 100],
               'yminorticks': [0.25, 0.75],
               'xlabel':      'Magnitude of selection\ncoefficients (%)',
               'ylabel':      'Fraction\nnonsynonymous (%)',
               'axoffset':    0.1,
               'theme':       'open' }

    xdat = [np.log10(intervals)]
    ydat = [percent_ns]
#    mp.plot(type='line', ax=ax_frac, x=xdat, y=ydat, colors=[COLOR_1], plotprops=lineprops, **pprops)
    mp.plot(type='bar', ax=ax_frac, x=xdat, y=ydat, colors=[COLOR_2], plotprops=histprops, **pprops)

    print('non-synonymous percentage:', percent_ns)
    print('intervals:', intervals)
    
    # labels and legends
    
    ax_sns.text(box_hist['left']-0.11, box_hist['top']+0.01, 'a'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_sns.text(box_sns['left'] -0.11, box_sns['top'] +0.01, 'b'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    ax_sns.text(box_frac['left']-0.11, box_frac['top']+0.01, 'c'.lower(), transform=fig.transFigure, **DEF_SUBLABELPROPS)
    
    ax_sns.text(box_hist['left'] + (box_hist['right']-box_hist['left'])/2, box_hist['bottom']-0.08, 'Inferred selection coefficients, ' + '$\hat{s}$' + ' (%)',
                ha='center', va='top', transform=fig.transFigure, **DEF_LABELPROPS)
#    ax_sns.text(box_sns['left']  + (box_sns['right'] - box_sns['left'])/2,  box_sns['bottom']-0.08, 'Number of largest\nselection coefficients',
#                ha='center', va='top', transform=fig.transFigure, **DEF_LABELPROPS)
                
#    ax_neg.text(xmin-1.5/n_hist, 740, '$-0.1<\hat{s}$', ha='center', va='bottom', **DEF_LABELPROPS)
#    ax_pos.text(xmin-1.5/n_hist, 710, '$\hat{s}<0.1$', ha='center', va='bottom', **DEF_LABELPROPS)

#    lineprops = { 'lw' : AXWIDTH/2., 'ls' : '-', 'alpha' : 1.0 }
#    pprops    = { 'xlim' : [0, 1], 'xticks' : [], 'ylim' : [0, 1], 'yticks' : [],
#        'hide' : ['top','bottom','left','right'], 'plotprops' : lineprops }
#    txtprops = {'ha' : 'right', 'va' : 'center', 'color' : BKCOLOR, 'family' : FONTFAMILY,
#        'size' : SIZELABEL, 'rotation' : 90, 'transform' : fig.transFigure}
#    ax[0][0].text(box_traj['left']-0.025, box_traj['top'] - (box_traj['top']-box_traj['bottom'])/2., 'Frequency', **txtprops)

#    # Plotting the enrichment of nonsynonymous mutations vs. number of coefficients
#    ax1  = fig.add_subplot(grid[0, 1])
#    ax1.set_ylim(syn_lower_limit, 101)
#    ax1.tick_params(labelsize=TICK_FONTSIZE, width=SPINE_LW, length=2)
#    for line in ['right',  'top']:
#        ax1.spines[line].set_visible(False)
#    for line in ['left', 'bottom']:
#        ax1.spines[line].set_linewidth(SPINE_LW)
#    sns.lineplot(np.arange(len(nonsyn_nonlinked))+1, 100*nonsyn_nonlinked, ax=ax1, lw=1, color=MAIN_COLOR)
#    ax1.axhline(100*nonsyn_nonlinked[-1], lw=1, color=COMP_COLOR, alpha=0.75)
#    ax1.text(0.25, (100*nonsyn_nonlinked[-1]-syn_lower_limit)/(100-syn_lower_limit) - 0.05, 'Background', fontsize=6, transform=ax1.transAxes, ha='center', va='center')
#    ax1.set_xscale('log')
#    ax1.set_xlim(1, len(nonsyn_nonlinked)+1)
#    ax1.set_ylabel('Nonsynonymous (%)', fontsize=AXES_FONTSIZE)
#    ax1.set_xlabel("Number of largest coefficients", fontsize=AXES_FONTSIZE)
#    print('background:', 100*nonsyn_nonlinked[-1])
    
    # SAVE FIGURE

    plt.savefig('%s/fig-2%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)

def plot_variant_selection_old(variant_file, trajectory_file, variant_list=[], s_cutoff=0.05):
    """ Map out mutations in the major variants, their aggregate inferred selection coefficients, and
        frequency trajectories across regions. """
        
    # Load data
    df_var = pd.read_csv(variant_file, comment='#', memory_map=True)
    df_sel = 0
    if len(variant_list)>0:
        df_sel = df_var[df_var.variant_names.isin(variant_list)]
    else:
        df_sel = df_var[np.fabs(df_var.selection_coefficient)>s_cutoff]
    
    mut_idxs   = []
    mut_labels = []
    mut_ns     = []
    s_sort = np.argsort(np.fabs(df_sel.selection_coefficient))[::-1]
    print(np.array(np.fabs(df_sel.selection_coefficient))[s_sort])
    for i in s_sort:
        
        # get mutation locations
        temp_idxs = []
        data_idxs = df_sel.iloc[i].nucleotides.split('/')
        for j in range(len(data_idxs)):
            if data_idxs[j]!='not_present':
                temp_idxs.append(int(data_idxs[j]))
            else:
                temp_idxs.append(-9999)
        
        # get mutation labels
        temp_labels = []
        data_sites  = df_sel.iloc[i].sites.split('/')
        data_labels = df_sel.iloc[i].aa_mutations.split('/')
        for j in range(len(data_labels)):
            if data_labels[j]!='not_present' and '>' in data_labels[j]:
                f, l = data_labels[j].split('>')[0], data_labels[j].split('>')[1]
                site = int(data_sites[j].split('-')[1])
                if l=='-' and f!='-':
                    temp_labels.append(r'$\Delta %d$' % site)
                else:
                    temp_labels.append('%s%d%s' % (f, site, l))
            else:
                temp_labels.append('')
        
        # get synonymous/NA (0) or nonsynonymous (1)
        temp_ns = [1 if j=='NS' else 0 for j in df_sel.iloc[i].synonymous.split('/')]
        
        mut_idxs.append(temp_idxs)
        mut_labels.append(temp_labels)
        mut_ns.append(temp_ns)
        
    
    # PLOT FIGURE
    
    ## set up figure grid
    
    w     = DOUBLE_COLUMN #SLIDE_WIDTH
    goldh = w / 1.1
    fig   = plt.figure(figsize=(w, goldh))

    box_vars = dict(left=0.13, right=0.90, bottom=0.60, top=0.95)
    box_traj = dict(left=0.13, right=0.70, bottom=0.12, top=0.45)

    gs_vars = gridspec.GridSpec(1, 1, **box_vars)
    gs_traj = gridspec.GridSpec(1, 1, **box_traj)
    
    ## a -- map of mutations for important variants and linked groups

    ax_vars = plt.subplot(gs_vars[0, 0])
    
    var_colors = sns.husl_palette(len(mut_idxs))
    
    pprops = { 'xlim':   [0, 30000],
               'ylim':   [-2*len(mut_idxs)-1, 1],
               'xticks': [],
               'yticks': [],
               'theme':  'open',
               'hide':   ['left','right', 'top', 'bottom'] }
            
    for i in range(len(mut_idxs)):
        pprops['facecolor'] = ['None']
        pprops['edgecolor'] = [BKCOLOR]
        sprops = dict(lw=AXWIDTH, s=2., marker='o', alpha=1)
        mp.scatter(ax=ax_vars, x=[mut_idxs[i]], y=[[-2*i for j in range(len(mut_idxs[i]))]], plotprops=sprops, **pprops)
        
#        s_muts = [mut_idxs[i][j] for j in range(len(mut_idxs[i])) if mut_ns[i][j]==0]
#
#        pprops['facecolor'] = [C_NEU_LT]
#        sprops = dict(lw=0, s=2., marker='o', alpha=1)
#        if len(s_muts)>0:
#            mp.scatter(ax=ax_vars, x=[s_muts], y=[[-2*i for j in range(len(s_muts))]], plotprops=sprops, **pprops)
        
        ns_muts = [mut_idxs[i][j] for j in range(len(mut_idxs[i])) if mut_ns[i][j]==1]
        ns_labels = [mut_labels[i][j] for j in range(len(mut_idxs[i])) if mut_ns[i][j]==1]
        
        pprops['facecolor'] = [var_colors[i]]
        sprops = dict(lw=0, s=2., marker='o', alpha=1)
        if i==len(mut_idxs)-1:
            mp.plot(type='scatter', ax=ax_vars, x=[ns_muts], y=[[-2*i for j in range(len(ns_muts))]], plotprops=sprops, **pprops)
        else:
            mp.scatter(ax=ax_vars, x=[ns_muts], y=[[-2*i for j in range(len(ns_muts))]], plotprops=sprops, **pprops)
        
#        # plot data points
#
#        y_vals = np.array(y_vals)
#        y_vals[y_vals<0.5] = 0.5
#
#        pprops['facecolor'] = ['None' for _c1 in range(len(x_ben[k]))]
#        pprops['edgecolor'] = eclist
#        sprops = dict(lw=AXWIDTH, s=2., marker='o', alpha=1.0)
#        temp_x = [[x_vals[_c1] + np.random.normal(0, 0.08) for _c2 in range(len(y_vals[_c1]))] for _c1 in range(len(y_vals))]
#        mp.scatter(ax=ax, x=temp_x, y=y_vals, plotprops=sprops, **pprops)
#
#        pprops['facecolor'] = fclist
#        sprops = dict(lw=0, s=2., marker='o', alpha=1)
#        mp.scatter(ax=ax, x=temp_x, y=y_vals, plotprops=sprops, **pprops)
#
#    dashlineprops = { 'lw' : SIZELINE * 2.0, 'ls' : ':', 'alpha' : 0.5 }
#    sprops = dict(lw=0, s=9., marker='o')
#
#    pprops = { 'yticks': [],
#               'xticks': [],
#               'hide'  : ['top', 'bottom', 'left', 'right'],
#               'theme' : 'open' }
#
#    for i in range(n_exs):
#        pprops['xlim'] = [-0.04, 0.04]
#        pprops['ylim'] = [  0.5,  1.5]
#        ydat           = [1]
#        xdat           = [inferred[i]]
#        xerr           = error[i]
#        if (i==n_exs-1):
#            pprops['xticks']      = [-0.04,   -0.02,      0,   0.02,   0.04]
#            pprops['xticklabels'] = [  ' ', r'$-2$', r'$0$', r'$2$', r'$4$']
#            pprops['xlabel']      = 'Inferred selection\ncoefficient, ' + r'$\hat{s}$' + ' (%)'
#            pprops['hide']        = ['top', 'left', 'right']
#            pprops['axoffset']    = 0.3
#        mp.plot(type='error', ax=ax[i][1], x=[xdat], y=[ydat], xerr=[xerr], colors=[colors[i]], **pprops)
#        ax[i][1].axvline(x=actual_unique[(-(i//2) + 2)%3], color=BKCOLOR, **dashlineprops)

    # SAVE FIGURE

    plt.savefig('%s/fig-3%s' % (FIG_DIR, EXT), dpi = 1000, facecolor = fig.get_facecolor(), edgecolor=None, **FIGPROPS)
    plt.close(fig)

