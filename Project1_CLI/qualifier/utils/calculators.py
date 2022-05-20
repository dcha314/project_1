# -*- coding: utf-8 -*-
"""A Collection of Financial Calculators.

This script contains a variety of financial calculator functions needed to
determine loan qualifications.

"""


def Portfolio_return(Equities, Real_Estate,Fixed_income,Precious_metals,Commodities):
    """Calculates users monthly debt to income ratio.

    Args:
        monthly_debt_payment (int): The total monthly debt.
        monthly_income (int): The total monthly income.

    Returns:
        The monthly debt ratio
    """
    Portfolio_return= (Equities * -.05) + (Real_Estate*.10) + (Fixed_income* .04) + (Precious_metals*.05) + (Commodities*-.02)
    return Portfolio_return

def calculate_loan_to_value_ratio(loan_amount, home_value):
    """Calculates users loan to value ratio based on inputs.

    Args:
        loan_amount (int): The requested loan amount.
        home_value (int): The home value.

    Returns:
        The loan-to-value ratio.
    """
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio
