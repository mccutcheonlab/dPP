# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:53:38 2018

@author: James Rig
"""

import JM_general_functions as jmf
import JM_custom_figs as jmfig
from dpp_assemble import *
from dpp_sessionfigs import *

import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import scipy.io as sio

## Colour scheme
col={}
col['np_cas'] = 'xkcd:silver'
col['np_malt'] = 'white'
col['lp_cas'] = 'xkcd:kelly green'
col['lp_malt'] = 'xkcd:light green'

# Extracts data from metafiles and sets up ppp_sessions dictionary

picklefolder = 'R:\\DA_and_Reward\\gc214\\dPP_combined\\output\\'

dpp1_sessions = metafile2sessions('R:\\DA_and_Reward\\gc214\dPP1\\dPP1_expdetails.xlsx',
                  'R:\\DA_and_Reward\\gc214\dPP1\\dPP1_metafile',
                  'R:\\DA_and_Reward\\gc214\\dPP1\\matfiles\\',
                  'R:\\DA_and_Reward\\gc214\\dPP1\\output\\',
                  sheetname='metafile')

dpp2_sessions = metafile2sessions('R:\\DA_and_Reward\\gc214\dPP2\\dPP2_expdetails.xlsx',
                  'R:\\DA_and_Reward\\gc214\dPP2\\dPP2_metafile',
                  'R:\\DA_and_Reward\\gc214\\dPP2\\matfiles\\',
                  'R:\\DA_and_Reward\\gc214\\dPP2\\output\\',
                  sheetname='metafile')

dpp_sessions = {**dpp1_sessions, **dpp2_sessions}

# Code to indictae which files to assemble and whether to save and/or make figures
assemble_sacc = False
assemble_cond1 = False
assemble_cond2 = False
assemble_pref = True
assemble_single = False

savefile=True
makefigs=False

if assemble_sacc:
    sessions = assemble_sessions(ppp_sessions,
                  rats_to_include = [],
                  rats_to_exclude = [],
                  sessions_to_include = ['s3', 's4', 's5'],
                  outputfile=picklefolder + 'dpp_sacc.pickle',
                  savefile=savefile,
                  makefigs=makefigs)

if assemble_cond1:
    sessions = assemble_sessions(ppp_sessions,
                  rats_to_include = [],
                  rats_to_exclude = [],
                  sessions_to_include = ['s6', 's7', 's8', 's9'],
                  outputfile=picklefolder + 'dpp_cond1.pickle',
                  savefile=savefile,
                  makefigs=makefigs)

if assemble_cond2:
    assemble_sessions(ppp_sessions,
                  rats_to_include = [],
                  rats_to_exclude = [],
                  sessions_to_include = ['s12', 's13', 's14', 's15'],
                  outputfile=picklefolder + 'dpp_cond2.pickle',
                  savefile=savefile,
                  makefigs=makefigs)

if assemble_pref:
    sessions = assemble_sessions(dpp_sessions,
                  rats_to_include = [],
                  rats_to_exclude = ['dPP1-1', 'dPP1-6', 'dPP1-7', 'dPP1-8',
                                     'dPP2-1', 'dPP2-3', 'dPP2-6', 'dPP2-7', 'dPP2-9', 'dPP2-10'],
                  sessions_to_include = ['s10', 's11', 's16'],
                  outputfile='R:\\DA_and_Reward\\gc214\\dPP_combined\\output\\dpp_pref.pickle',
                  savefile=savefile,
                  makefigs=makefigs)

# Code to run for single rat
if assemble_single:
    sessions_to_add = assemble_sessions(dpp2_sessions,
                  rats_to_include = ['dPP2-4'],
                  rats_to_exclude = [],
                  sessions_to_include = ['s10'],
                  outputfile=picklefolder + 'dpp_test.pickle',
                  savefile=savefile,
                  makefigs=makefigs)

