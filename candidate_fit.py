def calculate_candidate_score(total_requirements: int, satisfied_requirements: int, is_referral: bool) -> float:
    """
    Calculate a candidate score based on requirement satisfaction and referral status.
    
    Args:
        total_requirements: Total number of requirements in job description (X)
        satisfied_requirements: Number of requirements candidate satisfies (Y)
        is_referral: Whether candidate is a referral (True/False or 1/0)
    
    Returns:
        Score as a float, rounded to 1 decimal place, max 100
    """
    # Calculate base percentage score
    base_score = (satisfied_requirements / total_requirements) * 100
    
    # Add referral bonus if applicable
    if is_referral:
        base_score += 10
    
    # Cap at 100 and round to 1 decimal
    final_score = min(round(base_score, 1), 100.0)
    
    return final_score


# Example usage
# if __name__ == "__main__":
#     # Test cases
#     print(calculate_candidate_score(10, 8, False))  # 80.0
#     print(calculate_candidate_score(10, 8, True))   # 90.0
#     print(calculate_candidate_score(10, 10, True))  # 100.0 (capped)
#     print(calculate_candidate_score(15, 12, False)) # 80.0