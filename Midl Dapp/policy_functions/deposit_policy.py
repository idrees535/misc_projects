def deposit_policy_function(state, parameters, substep, history):
    # Get the current deposit amount from the user
    user_deposit = state['user_deposit']
    
    # Get the current collateral amount deposited by the custodian
    collateral = state['collateral']
    
    # Get the current wrapped fiat balance
    wrapped_fiat_balance = state['wrapped_fiat_balance']
    
    # Get the current fiat balance in the custodian's bank account
    fiat_balance = state['fiat_balance']
    
    # Calculate the maximum deposit amount that can be facilitated by the custodian
    max_deposit = collateral * parameters['max_deposit_ratio']
    
    # Determine the deposit amount that can be processed
    deposit_amount = min(user_deposit, max_deposit)
    
    # Calculate the amount of wrapped fiat to be minted
    wrapped_fiat_to_mint = deposit_amount * parameters['wrapped_fiat_ratio']
    
    # Update the state with the new wrapped fiat balance and fiat balance in the custodian's bank account
    new_wrapped_fiat_balance = wrapped_fiat_balance + wrapped_fiat_to_mint
    new_fiat_balance = fiat_balance + deposit_amount
    
    # Return the updated state
    return ({'wrapped_fiat_balance': new_wrapped_fiat_balance, 
             'fiat_balance': new_fiat_balance},)
