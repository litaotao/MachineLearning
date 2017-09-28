
# -*- coding: utf-8 -*-

try:
    print '-' * 80

    ### built-in
    import os
    import sys

    import copy
    import json
    import time
    import requests
    import collections
    import datetime as dt

    import warnings
    warnings.filterwarnings('ignore')

    ### 3-party
    import matplotlib
    matplotlib.rc('font', **{'size': 10})
    matplotlib.rc('lines', linewidth=1)

    import seaborn as sns 
    sns.set_style('whitegrid')
    import numpy as np
    import scipy as sp
    import pandas as pd
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 200
    pd.options.display.notebook_repr_html = True
    
    import pprint
    printf = pprint.pprint

    from playsound import playsound
    from IPython.core.debugger import Tracer

    print 'Config All Set Done ...'
except:
    import traceback
    traceback.print_exc()

### 占位
# __builtin__.__dict__['profile'] = ''