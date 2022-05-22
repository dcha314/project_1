def get_portfolio_info():
    """Prompt dialog to get the applicant's financial information.
    Returns:
        Returns the applicant's financial information.
    """

    commodities = questionary.text("What percentage of your portfolio is in commodities?").ask()
    gold = questionary.text("What percentage of your portfolio is in gold?").ask()
    real_estate = questionary.text("What percentage of your portfolio lies in real estate?").ask()
    equities = questionary.text("What's percentage of your portfolio is in equities?").ask()
    fixed_income = questionary.text("What's your monthly income?").ask()

    commodities = float(commodities)
    gold = float(gold)
    real_estate = float(real_estate)
    equities = float(equities)
    fixed_income = float(fixed_income)

    return commodities, gold, real_estate, equities, fixed_income