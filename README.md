# RLForSeg

Reinforcement learning for Instance Segmentation implementing the concepts discussed [here](...)

## Installation via conda:
```
conda env create -f environment.yml
```
## Initiating the training:
```
python run.py -d </path/to/log/dir> -p <wandb_project_name> -e <wandb_user> -c <conf/file.yaml>
```
## Input data
Train- as well as validation-data is expected to be in separate directories, 
each containing a set of h5 files.
Each file needs the following entries:
    
    - input data (N, H, W) for the feature extractor. 
      Typically the raw image + additional channles 
    - A superpixel segmentation, where the n superpixel labels have to be 
      consecutive integers, starting at 0.
    - a set of edges (2, E) defining the superpixel graph where 
      each entry corresponds to a superpixel label
    optional:
    - a ground truth segmentation
    - a set of ground truth edge weights (E)
    - a set of edge features (E, f) as additional input to the GNN
    - a set of node features (n, f) as additional input to the GNN

## Custom reward function:
A custom reward function can be implemented in `/rewards`. It has to be subclassed from 
`RewardFunctionAbc` in `/rewards/reward_abc.py` and implement its two functions. 
An example for the circles dataset can be found in `/rewards/circles_reward.py`.
The reward class needs to be imported in `/rewards/__init__.py`.
The class name can the be referenced in the confg file. A config file example can be found in `/conf/example.yaml`.
