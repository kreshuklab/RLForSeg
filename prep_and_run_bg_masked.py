import matplotlib
matplotlib.use('Agg')
import torch.multiprocessing as mp
from run import main
from utils.yaml_conv_parser import YamlConf
import os
import wandb

if __name__ == '__main__':
    # os.nice(15)
    # project name: "RL for Segmentation"
    wandb.init(dir="/g/kreshuk/hilt/projects/RLForSeg/results/wandb", project="leptin_bg_m_objlvl_newfe", entity="rl_segmentation", config="conf/leptin_bg_masked_configs.yaml")
    main(wandb.config)
