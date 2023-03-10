"""This script runs a single sorn simulation for the experiment given as an
argument with the specified parameters and experiment instructions"""

import sys; sys.path.append('.')
from importlib import import_module

from common.sorn import Sorn
from common.stats import Stats
from utils import backup_pickle

################################################################################
#                              SORN simulation                                 #
################################################################################

# 1. load param file
try:
    exp_dir = import_module(sys.argv[1])
except:
    raise ValueError('Please specify a valid experiment name as first argument.')

try:
    tag = sys.argv[2]
except:
    raise ValueError('Please specify a valid experiment tag.')

# 2. add experiment specific parameters
try:
    if sys.argv[3]=="param":
        params = exp_dir.param
        print("Running with param")
    elif sys.argv[3]=="NO_stdp":
        params = exp_dir.param_NO_stdp
        print("Running with NO stdp")
    elif sys.argv[3]=="NO_ip":
        params = exp_dir.param_NO_ip
        print("Running with NO ip")
    elif sys.argv[3]=="NO_sn":
        params = exp_dir.param_NO_sn
        print("Running with NO sn")
    elif sys.argv[3]=="JUST_stdp":
        params = exp_dir.param_JUST_stdp
        print("Running with JUST stdp")
    elif sys.argv[3]=="JUST_ip":
        params = exp_dir.param_JUST_ip
        print("Running with JUST ip")
    elif sys.argv[3]=="JUST_sn":
        params = exp_dir.param_JUST_sn
        print("Running with JUST sn")
    else:
        raise ValueError('Specified parameters module not found.')
except:
    raise ValueError('Please specify a valid parameters module.')
    
params.get_par()
params.get_aux()
params.aux.display = True
params.aux.experiment_tag = '_{}'.format(tag)

# 3. initialize experiment, sorn, and stats objects
#    the experiment class keeps a copy of the initial sorn main parameters
experiment = exp_dir.experiment.Experiment(params)
experiment.files_tosave = ['params', 'stats', 'scripts']
sorn = Sorn(params, experiment.inputsource)
stats = Stats(experiment.stats_cache, params)

# 4. run one experiment once
experiment.run(sorn, stats)

# 5. save initial sorn parameters and stats objects
backup_pickle(experiment, stats)
