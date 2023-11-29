def get_user_rewards(batch_owner_funds_used, total_transfer_size):
    batch_fee = 0.2 # USD
    reward_percentage = 0.05
    reward_amount = batch_owner_funds_used / total_transfer_size * batch_fee * reward_percentage
    return reward_amount
