def calculate_jury_rewards(num_disputes_resolved, stake_percentage, is_winner):
    """
    Calculates the rewards for a jury member based on the number of disputes resolved, stake percentage,
    and whether the jury member made the correct decision.

    Args:
    - num_disputes_resolved (int): The number of disputes resolved by the jury member in a week.
    - stake_percentage (float): The percentage of stake the jury member holds in the disputed transaction.
    - is_winner (bool): Whether the jury member made the correct decision in resolving a dispute.

    Returns:
    - float: The total rewards earned by the jury member.
    """
    # Calculate the base reward for resolving disputes
    base_reward = 0.75 * slashed_amount  # 75% of slashed amount
    activity_reward = 0
    category_reward = 0
    
    # Calculate activity-based rewards for Platinum, Gold, and Silver categories
    if num_disputes_resolved >= 10:
        if stake_percentage >= 5:
            category_reward = 20 * stake_percentage
            if is_winner:
                activity_reward = 0.01 * ramp_fee  # 1% of ramp fee
        else:
            raise ValueError("Jury member must hold at least 5% stake to be in Platinum category.")
    elif num_disputes_resolved >= 7.5:
        if stake_percentage >= 10:
            category_reward = 10 * stake_percentage
            if is_winner:
                activity_reward = 0.01 * ramp_fee  # 1% of ramp fee
        else:
            raise ValueError("Jury member must hold at least 10% stake to be in Gold category.")
    elif num_disputes_resolved >= 5:
        if stake_percentage >= 20:
            category_reward = 5 * stake_percentage
            if is_winner:
                activity_reward = 0.01 * ramp_fee  # 1% of ramp fee
        else:
            raise ValueError("Jury member must hold at least 20% stake to be in Silver category.")
    else:
        if stake_percentage >= 25:
            category_reward = 4 * stake_percentage
            if is_winner:
                activity_reward = 0.01 * ramp_fee  # 1% of ramp fee
        else:
            raise ValueError("Jury member must hold at least 25% stake to be in Regular category.")
    
    return base_reward + activity_reward + category_reward
