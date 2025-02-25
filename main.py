def check_loan_eligibility(revenue, business_age, credit_score, debt_ratio, collateral):
    """Check if a business is eligible for a loan based on given criteria."""
    if revenue >= 500000:
        if business_age >= 2:
            if credit_score >= 70:
                if debt_ratio <= 0.40:
                    if collateral:
                        return "Loan Approved: Eligible for higher loan limit."
                    else:
                        return "Loan Approved: Limited to 3M RWF."
                else:
                    return "Loan Denied: High debt-to-income ratio."
            else:
                return "Loan Denied: Low credit score."
        else:
            return "Loan Denied: Business age is less than 2 years."
    else:
        return "Loan Denied: Revenue is less than 500,000 RWF."

# Example Test Cases
if __name__ == "__main__":
    print(check_loan_eligibility(600000, 3, 80, 0.35, True))   # Approved with higher limit
    print(check_loan_eligibility(600000, 3, 80, 0.35, False))  # Approved with limit
    print(check_loan_eligibility(400000, 3, 80, 0.35, True))   # Denied: Low revenue
    print(check_loan_eligibility(600000, 1, 80, 0.35, True))   # Denied: Short business age
    print(check_loan_eligibility(600000, 3, 60, 0.35, True))   # Denied: Low credit score
