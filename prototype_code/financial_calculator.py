import math

# ===================================
# USER INPUT
# ===================================

margin_capital = float(input("Enter Available Margin Capital (₹): "))

# ===================================
# PROJECT COST & LOAN CALCULATION
# ===================================

project_cost = margin_capital / 0.10
loan_amount = project_cost * 0.90

# ===================================
# SCHEME ROUTING
# ===================================

if project_cost <= 140000:

    scheme = "Micro Finance Scheme"
    interest_rate = 6.5
    tenure_years = 3
    moratorium_months = 3
    eligibility = "ELIGIBLE"

elif project_cost <= 5000000:

    scheme = "Term Loan Scheme"
    interest_rate = 8.0
    tenure_years = 7
    moratorium_months = 6
    eligibility = "ELIGIBLE"

else:

    scheme = "No Scheme Available"
    interest_rate = 0
    tenure_years = 0
    moratorium_months = 0
    eligibility = "NOT ELIGIBLE"

# ===================================
# EMI CALCULATION
# ===================================

if eligibility == "ELIGIBLE":

    monthly_rate = interest_rate / (12 * 100)

    total_months = tenure_years * 12

    emi = (
        loan_amount
        * monthly_rate
        * ((1 + monthly_rate) ** total_months)
        / (((1 + monthly_rate) ** total_months) - 1)
    )

    quarterly_emi = emi * 3

    total_payment = emi * total_months

    total_interest = total_payment - loan_amount

# ===================================
# REPORT
# ===================================

print("\n" + "=" * 60)
print("SMART FINANCIAL STRUCTURING REPORT")
print("=" * 60)

print(f"\nAvailable Margin Capital : ₹{margin_capital:,.2f}")

print(f"Total Project Cost       : ₹{project_cost:,.2f}")

print(f"Maximum Loan Amount      : ₹{loan_amount:,.2f}")

print(f"\nEligibility Status       : {eligibility}")

if eligibility == "ELIGIBLE":

    print(f"\nSelected Scheme          : {scheme}")

    print(f"Interest Rate            : {interest_rate}%")

    print(f"Loan Tenure              : {tenure_years} Years")

    print(f"Moratorium Period        : {moratorium_months} Months")

    print(f"First EMI Starts After   : {moratorium_months} Months")

    print("\nRepayment Details")
    print("-" * 35)

    print(f"Monthly EMI              : ₹{emi:,.2f}")

    print(f"Quarterly EMI            : ₹{quarterly_emi:,.2f}")

    print(f"Total Interest Payable   : ₹{total_interest:,.2f}")

    print(f"Total Repayment Amount   : ₹{total_payment:,.2f}")

else:

    print("\nProject Cost exceeds ₹50,00,000")
    print("No scheme available under current rules.")

print("\n" + "=" * 60)
