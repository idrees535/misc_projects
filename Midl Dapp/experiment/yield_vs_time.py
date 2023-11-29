import matplotlib.pyplot as plt
import numpy as np

# Define initial state variables and system parameters
state = {
    'custodians': [
        {'id': 1, 'category': 'Bronze', 'volume': 100},
        {'id': 2, 'category': 'Bronze', 'volume': 200},
        {'id': 3, 'category': 'Silver', 'volume': 300},
        {'id': 4, 'category': 'Gold', 'volume': 400},
        {'id': 5, 'category': 'Platinum', 'volume': 500},
    ],
    'jury_members': [
        {'id': 1, 'category': 'Regular', 'stake': 10},
        {'id': 2, 'category': 'Regular', 'stake': 20},
        {'id': 3, 'category': 'Silver', 'stake': 50},
        {'id': 4, 'category': 'Gold', 'stake': 100},
        {'id': 5, 'category': 'Platinum', 'stake': 200},
    ],
    'user_accrued_rewards': {'1': 100, '2': 50, '3': 200},
    'custodian_accrued_rewards': {'1': 20, '2': 30, '3': 50, '4': 100, '5': 200},
    'jury_accrued_rewards': {'1': 10, '2': 15, '3': 30, '4': 50, '5': 100},
}

params = {
    'batch_owner_rewards': 0.05,
    'jury_rewards': 0.01,
    'jury_stake_min': {
        'Regular': 25,
        'Silver': 20,
        'Gold': 10,
        'Platinum': 5,
    },
    'jury_stake_max': {
        'Regular': 100,
        'Silver': 50,
        'Gold': 25,
        'Platinum': 10,
    },
    'custodian_reward_rate_ramp': 5,
    'custodian_reward_rate_batch': 0.2,
    'category_reward_pool_size': {
        'Platinum': 10000,
        'Gold': 5000,
        'Silver': 2500,
    },
    'batch_fee_distribution': {
        'Ala_token_swap_burn': 0.3,
        'Batch_Owner': 0.05,
        'Batch_Facilitator': 0.09,
        'Founding_Team': 0.1,
        'Future_Development_Team': 0.25,
        'Custodian_Category_Reward_Pool': 0.21,
    },
    'jury_slashing_amount': 10,
    'custodian_slashing_amount': 5,
    'user_slashing_amount': 5,
}

# Define simulation time period
start_time = 0
end_time = 5  # years
time_step = 0.1  # years

# Define function to calculate custodian rewards and slashing at a given time
def calculate_custodian_rewards_slashing(time):
    rewards = []
    slashing = []
    for custodian in state['custodians']:
        reward = get_custodian_reward(state, params, custodian['id'])
        rewards.append(reward)
        if is_custodian
