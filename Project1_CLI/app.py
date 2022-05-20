# from pathlib import Path
import fire
import questionary



# from qualifier.utils.calculators import (Portfolio_return)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information."""


    Equities = questionary.text("what percentage of your portfolio is invested in Equities?").ask()
    Real_Estate = questionary.text("what percentage of your portfolio is invested in Real Estate?").ask()
    Fixed_income = questionary.text("what percentage of your portfolio is invested in Fixed Income?").ask()
    Precious_metals = questionary.text("what percentage of your portfolio is invested in Precious Metals?").ask()
    Commodities = questionary.text("what percentage of your portfolio is invested in Commodities?").ask()

    Equities = float(Equities)
    Real_Estate = float(Real_Estate)
    Fixed_income = float(Fixed_income)
    Precious_metals = float(Precious_metals)
    Commodities = float(Commodities)

    return (Equities, Real_Estate, Fixed_income, Precious_metals, Commodities)

# Portfolio = Portfolio_return (Equities, Real_Estate, Fixed_income, Precious_metals, Commodities)
#     print(f"Your Portfolio return is {Portfolio:.02f}")
    
def Portfolio_return(Equities, Real_Estate,Fixed_income,Precious_metals,Commodities):
    Portfolio_return= (Equities * -.05) + (Real_Estate*.10) + (Fixed_income* .04) + (Precious_metals*.05) + (Commodities*-.02)
    # return Portfolio_return    
    print(f"Your Portfolio return is {Portfolio_return:.02f}")
    

def run():
    """The main function for running the script."""
    Equities, Real_Estate, Fixed_income, Precious_metals, Commodities = get_applicant_info()

    Portfolio_return = Portfolio_return(Equities, Real_Estate,Fixed_income,Precious_metals,Commodities)
    

if __name__ == "__main__":
    fire.Fire(run)
