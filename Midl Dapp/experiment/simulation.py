# Import the setup module:
# * sets up the Python path
# * runs shared notebook-configuration methods, such as loading IPython modules
import setup

# External dependencies
import copy
import logging
import numpy as np
import pandas as pd
import plotly.express as px
from pprint import pprint

# Project dependencies
from midl_model.model import MidlModel
import midl_model.constants as constants
import midl_model.environment as environment
import experiments.notebooks.visualizations as visualizations
from experiments.run import run
from experiments.utils import display_code

# Import the default experiment and experiment templates
import experiments.default_experiment as default_experiment
import experiments.templates.time_domain_analysis as time_domain_analysis
import experiments.templates.eth_price_eth_staked_grid_analysis as eth_price_eth_staked_grid_analysis

# Create a copy of the MidlModel
model = MidlModel()

# Create a copy of the default simulation
simulation = copy.deepcopy(default_experiment.experiment.simulations[0])

# Customize the simulation's initial state and system parameters
simulation.model.initial_state.update({
    "total_staked": 1000000,
    "eth_price": 2000,
    "market_cap": 2000000000,
    "daily_active_users": 1000,
    "total_rewards_paid": 1000000,
    "total_supply": 100000000,
    "user_rewards": {
        "0x1234": 10000,
        "0x5678": 20000
    }
})

simulation.model.params.update({
    "eth_price_process": ["geometric_brownian_motion", {"mu": 0.0001, "sigma": 0.01}],
    "market_cap_process": ["geometric_brownian_motion", {"mu": 0.0001, "sigma": 0.01}],
    "daily_active_users_process": ["geometric_brownian_motion", {"mu": 0.0001, "sigma": 0.01}],
    "total_rewards_paid_process": ["geometric_brownian_motion", {"mu": 0.0001, "sigma": 0.01}],
    "total_supply_process": ["geometric_brownian_motion", {"mu": 0.0001, "sigma": 0.01}],
    "user_rewards_process": ["geometric_brownian_motion", {"mu": 0.0001, "sigma": 0.01}],
    "reward_rate": [1],
    "reward_period": [7],
    "alpha": [0.1],
    "beta": [0.9],
    "gamma": [0.1],
    "min_commitment_days": [90],
    "max_commitment_days": [365],
    "max_user_committment_percentage": [0.1],
    "min_mining_frequency_days": [7],
    "max_mining_frequency_days": [30],
    "staking_token": ["MIDLT"]
})

# Create a copy of the eth_price_eth_staked_grid_analysis simulation
simulation_analysis_3 = copy.deepcopy(eth_price_eth_staked_grid_analysis.experiment.simulations[0])

# Customize the simulation's initial state and system parameters
simulation_analysis_3.model.initial_state.update({
    "total_staked": 1000000,
    "market_cap": 2000000000,
    "daily_active_users": 1000,
    "total_rewards_paid": 1000000,
    "total_supply": 100000000,
    "user_rewards": {
        "0x1234": 10000,
        "0x
