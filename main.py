def check_loan_eligibility(revenue, business_age, credit_score, debt_ratio, collateral, existing_loans):
    """
    Determines loan eligibility based on key financial and business factors.
    :param revenue: Annual revenue in RWF
    :param business_age: Years in operation
    :param credit_score: Credit rating (0-100)
    :param debt_ratio: Debt-to-income ratio (0-1)
    :param collateral: Boolean (True if collateral is available, False otherwise)
    :param existing_loans: Boolean (True if other loans exist, False otherwise)
    :return: Loan approval decision.
    """

    if revenue < 500000:
        return "Loan Denied: Revenue is less than 500,000 RWF."

    if business_age < 2:
        return "Loan Denied: Business age is less than 2 years."

    if credit_score < 65:
        return "Loan Denied: Low credit score."

    if debt_ratio > 0.40:
        return "Loan Denied: High debt-to-income ratio."

    if existing_loans and debt_ratio > 0.30:
        return "Loan Denied: High debt ratio with existing loans."

    if collateral:
        if credit_score >= 80:
            return "Loan Approved: Eligible for higher loan limit."
        else:
            return "Loan Approved: Limited to 3M RWF."

    return "Loan Denied: No collateral available."


# Example Test Cases
if __name__ == "__main__":
    print(check_loan_eligibility(600000, 3, 80, 0.35, True, False))  # Approved with higher limit
    print(check_loan_eligibility(600000, 3, 75, 0.35, True, False))  # Approved with limit
    print(check_loan_eligibility(400000, 3, 80, 0.35, True, False))  # Denied: Low revenue
    print(check_loan_eligibility(600000, 1, 80, 0.35, True, False))  # Denied: Short business age
    print(check_loan_eligibility(600000, 3, 60, 0.35, True, False))  # Denied: Low credit score
    print(check_loan_eligibility(600000, 3, 80, 0.45, True, False))  # Denied: High debt ratio
    print(check_loan_eligibility(600000, 3, 80, 0.35, False, False))  # Denied: No collateral