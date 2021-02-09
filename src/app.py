# %%

# data
import pandas as pd
import pm4py
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.util import dataframe_utils

# process mining 
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery

# viz
from pm4py.visualization.petrinet import visualizer as pn_visualizer
from pm4py.visualization.process_tree import visualizer as pt_visualizer
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.dfg import visualizer as dfg_visualization
from pm4py.visualization.bpmn import visualizer as bpmn_visualization

# misc
from pm4py.objects.conversion.process_tree import converter as pt_converter


## small process model
#log
# log = xes_importer.apply('./../ressource/running-example.xes')
log_csv_small = pd.read_csv('./../ressource/running-example.csv')
log_csv_small = dataframe_utils.convert_timestamp_columns_in_df(log_csv_small)
print(log_csv_small.head())

# create xes log from data frame
log = log_converter.apply(log_csv_small)

# inductive miner
# create the process tree
tree = inductive_miner.apply_tree(log)

# viz tree
gviz = pt_visualizer.apply(tree)
pt_visualizer.view(gviz)

# bpmn & viz bpmn
bpmn_model = pm4py.convert_to_bpmn(tree)
gviz = bpmn_visualization.apply(bpmn_model)
bpmn_visualization.view(gviz)

# creatig the graph from log
dfg = dfg_discovery.apply(log)

# viz
gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.FREQUENCY)
dfg_visualization.view(gviz)



## bigger process model
log_csv_big = pd.read_csv('./../ressource/process.csv')
# log_csv_process = dataframe_utils.convert_timestamp_columns_in_df(log_csv)
print(log_csv_big.head())

log_csv_big.rename(columns={'TIMESTAMP': 'time:timestamp', 'CASE_ID': 'case:concept:name', 'ACTIVITY': 'concept:name', 'SERVICEPOINT': 'org:resource'}, inplace=True)
log_csv_big = dataframe_utils.convert_timestamp_columns_in_df(log_csv_big)

print(log_csv_big.head())

# create xes log from data frame
log = log_converter.apply(log_csv_big)

# inductive miner
# create the process tree
tree = inductive_miner.apply_tree(log)

# viz tree
gviz = pt_visualizer.apply(tree)
pt_visualizer.view(gviz)

# bpmn & viz bpmn
bpmn_model = pm4py.convert_to_bpmn(tree)
gviz = bpmn_visualization.apply(bpmn_model)
bpmn_visualization.view(gviz)

# creatig the graph from log
dfg = dfg_discovery.apply(log)

# viz
gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.FREQUENCY)
dfg_visualization.view(gviz)
# %%
