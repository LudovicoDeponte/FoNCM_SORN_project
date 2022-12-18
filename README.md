# FoNCM_SORN_project

For the Foundations of Neural and Cognitive Modelling 2022 course at UvA, we experiment with different types of plasticity mechanism implemented for the SORN network (from [Lazar et al. 2009](http://journal.frontiersin.org/article/10.3389/neuro.10.023.2009/full)).

We relay on a [previous implementation](https://github.com/delpapa/SORN_V2) of the SORN network by Del Papa.

We add new parameters file and a switch for the synaptic plasticity.

We also modify the plotting function and add a small shell script to programmatically run experiments with SORN, while changing some lines of the parameters files and selecting one of them.

### How to run?

Just mount the drive and pull the original directory, then run all the cells!

If different numbers of excitatory neurons are introduced, include them in <N_VALUES> list of the <plotty3> function as otherwise they will not appear in your graph.

## Disclaimer!

The code is not beautiful, but it works!
  
We might add some changes and improve its efficiency; specifically there are some hard-coded parts and the way in which experiments are saved generate a complex structure of nested folders.
  
Any suggestion or contribution is welcomed!
