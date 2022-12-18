# FoNCM_SORN_project

For the Foundations of Neural and Cognitive Modelling 2022 course at UvA, we experiment with different types of plasticity mechanisms implemented for the SORN network (from [Lazar et al. 2009](http://journal.frontiersin.org/article/10.3389/neuro.10.023.2009/full)). We use the Counting Task from the original paper, making more experiments by turning on and off different plasticity mechanisms.

We relay on a [previous implementation](https://github.com/delpapa/SORN_V2) of the SORN network by Del Papa.

We added a switch for the synaptic plasticity in the `sorn` module and we included `project_params` folder inside the `CountingTask` folder to store files that specify which plasticities are on and off during the experiment.


We also modified the plotting function and added a small shell script to programmatically run experiments with SORN, while selecting different parameters files and changing some lines of those.

### How to run?

Just copy the Jupyter notebook `Final_Project.ipynb` and the `SORN_V2` folder in your drive and run all the uncommented cells; data from the runned experiment and the report is included in the folder `experiment` and must be firstly unzipped, then moved to `SORN_V2/backup`. 

To run different experiments, change the name of the experiment in the shell script from `exp3` to the desired one. Change the iterations value to change the parameter file selected, the number of excitatory neurons and the number of iterations to be performed for each configuration of SORN.

If different numbers of excitatory neurons are introduced, include them in `<N_VALUES>` list of the `<plotty3>` function as otherwise they will not appear in your graph.

The results of the experiments displayed in `plot1`, `plot2` and `plot3` are zipped at `experiments/CountingTask_exp3_<PARAMETER>`, while the ones for `counterInt` are called `experiments/CountingTask_exp4_<PARAMETER>`.

## Disclaimer!

The code is not beautiful, but it works!
  
We might add some changes and improve its efficiency; specifically there are some hard-coded parts and the way in which experiments are saved generate a complex structure of nested folders.
  
Any suggestion or contribution is welcomed!

## To DO:
* (DONE) import CoLab
* (DONE) import compressed data
* (DONE) import anomaly experiment  
