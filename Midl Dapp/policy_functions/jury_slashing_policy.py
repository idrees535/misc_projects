# User slashing policy function
def user_slashing(dispute_type):
    if dispute_type == 'jury':
        # Slash 5USD from user's accrued reward pool
        slashed_amount = 5
        # Distribute slashed amount among custodians and jury team members
        custodian_reward = 0.25 * slashed_amount
        jury_reward = 0.75 * slashed_amount / 11 # Equally among 11 jury members
        # Return rewards to be distributed
        return {'custodian_reward': custodian_reward, 'jury_reward': jury_reward}
    elif dispute_type == 'appeal':
        # Confiscate 10USD refundable fee from user's appeal
        confiscated_fee = 10
        # Return confiscated fee to be awarded to appeal board
        return {'confiscated_fee': confiscated_fee}
    else:
        # Invalid dispute type
        return None

#Custodian Slashing policy Function
def custodian_slashing(custodian_accrued_rewards, jury_members, affected_user):
    """
    Function to slash a custodian's accrued rewards if found guilty of fraudulent activity

    Parameters:
    custodian_accrued_rewards (float): the current amount of accrued rewards for the custodian
    jury_members (list): a list of the jury members who voted against the custodian
    affected_user (str): the address of the user who was affected by the fraudulent activity

    Returns:
    tuple: a tuple containing the updated amount of accrued rewards for the custodian and the amount slashed
    """

    # Set the amount to be slashed
    slashing_amount = 5.0

    # Calculate the amount to be distributed to the jury members
    jury_reward = (slashing_amount * 0.75) / len(jury_members)

    # Calculate the amount to be awarded to the affected user
    user_reward = slashing_amount * 0.25

    # Distribute the rewards to the jury members
    for jury_member in jury_members:
        jury_member.accrued_rewards += jury_reward

    # Award the reward to the affected user
    affected_user.accrued_rewards += user_reward

    # Apply the slashing to the custodian's accrued rewards
    custodian_accrued_rewards -= slashing_amount

    # Return the updated amount of accrued rewards for the custodian and the amount slashed
    return custodian_accrued_rewards, slashing_amount


#Jury slashing policy function

def jury_slashing(jury_members, affected_jury_members):
    """
    Applies slashing to jury members who voted against the affected party and their decision was overturned by the protocol appeal board

    Parameters:
    jury_members (list): List of all jury members
    affected_jury_members (list): List of jury members who voted against the affected party and their decision was overturned

    Returns:
    None
    """
    slashing_amount = 10
    for jury_member in jury_members:
        if jury_member in affected_jury_members:
            jury_member.accrued_reward_pool -= slashing_amount / len(jury_members)
