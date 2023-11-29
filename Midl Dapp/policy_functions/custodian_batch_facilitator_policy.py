def custodian_reward_policy(state, system_parameters):
    
    # Calculate custodian rewards from ramp fee
    custodian_rewards = state['custodian_balance'] * system_parameters['ramp_fee_percentage']
    
    # Calculate batch facilitation rewards for each custodian
    for custodian in state['custodians']:
        batch_rewards = custodian['batch_facilitated'] * system_parameters['batch_fee']
        custodian_rewards += batch_rewards
        
        # Categorize custodian based on transaction volume
        cumulative_volume = custodian['cumulative_volume']
        total_volume = state['total_cumulative_volume']
        custodian['category'] = ''
        activity_meter = cumulative_volume / total_volume
        
        if activity_meter > 0.10:
            custodian['category'] = 'Platinum'
        elif 0.075 <= activity_meter <= 0.10:
            custodian['category'] = 'Gold'
        elif 0.05 <= activity_meter < 0.075:
            custodian['category'] = 'Silver'
        elif 0.025 <= activity_meter < 0.05:
            custodian['category'] = 'Bronze'
        
        # Calculate activity based rewards for each custodian
        category_rewards = system_parameters[custodian['category'] + '_reward_pool'] * (batch_rewards / state['total_batch_fee'])
        custodian['category_rewards'] += category_rewards
        state['custodian_balance'] -= category_rewards
    
    # Update system parameters with custodian rewards
    system_parameters['custodian_rewards'] = custodian_rewards
    
    return state, system_parameters
