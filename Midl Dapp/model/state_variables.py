def fee_structure_model(state, step, sL, s, p):
    """
    A dynamic model to calculate the amount accumulated in fees by all the agents in a certain time period.
    """

    # Define the ramp and batch fees
    ramp_fee = 5
    batch_fee = 0.2
    number_of_custodians = 12000
    awake_quotient=0.75
    awake_custodians=number_of_custodians * awake_quotient
    avg_transaction_volume_per_day =100000000
    avg_number_of_transavtions_per_day= 12000
    on_ramp_off_ramp_ratio=0.5
    dispute_prob=0.1
    appeal_prob=0.05

    # Calculate the total ramp fees accumulated
    total_ramp_fees = ramp_fee * s['num_ramp_transactions']

    # Calculate the total withdrawal fees accumulated
    total_withdrawal_fees = (ramp_fee + batch_fee) * s['num_withdrawals']

    # Calculate the total batch fees accumulated
    total_batch_fees = s['total_batch_volume'] * batch_fee
    ala_token_swap_burn_fee = total_batch_fees * 0.3
    batch_owner_fee = total_batch_fees * 0.05
    batch_facilitator_fee = total_batch_fees * 0.09
    founding_team_fee = total_batch_fees * 0.1
    future_dev_team_fee = total_batch_fees * 0.25
    custodian_category_reward_pool_fee = total_batch_fees * 0.21

    # Calculate the total custodian fees accumulated
    total_custodian_fees = ramp_fee * s['num_custodian_transactions']
    custodian_fee = total_custodian_fees * 0.99
    jury_fee = total_custodian_fees * 0.01

    # Update the state variables for fees accumulated
    total_fees = total_ramp_fees + total_withdrawal_fees + total_batch_fees
    s['total_fees'] = total_fees
    s['total_ramp_fees'] = total_ramp_fees
    s['total_withdrawal_fees'] = total_withdrawal_fees
    s['total_batch_fees'] = total_batch_fees
    s['ala_token_swap_burn_fee'] = ala_token_swap_burn_fee
    s['batch_owner_fee'] = batch_owner_fee
    s['batch_facilitator_fee'] = batch_facilitator_fee
    s['founding_team_fee'] = founding_team_fee
    s['future_dev_team_fee'] = future_dev_team_fee
    s['custodian_category_reward_pool_fee'] = custodian_category_reward_pool_fee
    s['total_custodian_fees'] = total_custodian_fees
    s['custodian_fee'] = custodian_fee
    s['jury_fee'] = jury_fee

    return ('state', s)

# System Parameters

ramp_fee = 5    # fixed ramp fee
batch_fee = 0.2    # batch fee
jury_reward_percentage = 0.01    # 1% of ramp fee for jury rewards
dispute_appeal_fee = 10    # appeal fee for disputes

# Batch Fee Distribution

ala_token_swap_burn_percentage = 0.3
batch_owner_percentage = 0.05
batch_facilitator_percentage = 0.09
founding_team_percentage = 0.1
future_dev_team_percentage = 0.25
custodian_reward_pool_percentage = 0.21

# Jury Categorization

platinum_threshold = 0.1    # 10% disputes resolved for platinum category
gold_threshold = 0.075    # 7.5% disputes resolved for gold category
silver_threshold = 0.05    # 5% disputes resolved for silver category

platinum_stake_percentage = 0.05    # 5% stake required for platinum category
gold_stake_percentage = 0.1    # 10% stake required for gold category
silver_stake_percentage = 0.2    # 20% stake required for silver category
regular_member_stake_percentage = 0.25    # 25% stake required for regular members

# Jury Rewards

dispute_reward_percentage = 0.75    # 75% of dispute fee for right wing jury members
appeal_reward_percentage = 0.75    # 75% of dispute fee for left wing jury members

# Custodian Categorization

platinum_volume_percentage = 0.1    # 10% transaction volume for platinum category
gold_volume_percentage = 0.075    # 7.5% transaction volume for gold category
silver_volume_percentage = 0.05    # 5% transaction volume for silver category

# Custodian Slashing

custodian_slashing_amount = 5    # 5 USD ramp fee slashing for custodian
jury_slashing_amount = 5    # 5 USD slashing for jury members
jury_appeal_slashing_amount = 10    # 10 USD slashing for false appeal

# User Slashing

user_slashing_amount = 5    # 5 USD ramp fee slashing for users


# State Variables

system_reward_pool = 0    # total reward pool of the system
jury_reward_pool = 0    # reward pool for jury members
custodian_reward_pool = 0    # reward pool for custodians
user_reward_pool = 0    # reward pool for users

jury_members = []    # list of all jury members
custodians = []    # list of all custodians
users = []    # list of all users

platinum_custodians = []    # list of platinum custodians
gold_custodians = []    # list of gold custodians
silver_custodians = []    # list of silver custodians

platinum_jury_members = []    # list of platinum jury members
gold_jury_members = []    # list of gold jury members
silver_jury_members = []    # list of silver jury members
regular_jury_members = []    # list of regular jury members

disputes = []    # list of all disputes
appeals = []    # list of all appeals


