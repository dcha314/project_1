import sys
import fire
from numpy import save
import questionary
import matplotlib.pyplot as plt

from DataFrame_Analysis import optimal_risky_port_2001
from DataFrame_Analysis import optimal_risky_port_2003
from DataFrame_Analysis import optimal_risky_port_2008
from DataFrame_Analysis import optimal_risky_port_2020
from DataFrame_Analysis import optimal_risky_port_2022

from DataFrame_Analysis import cumulative_returns_event_2001
from DataFrame_Analysis import cumulative_returns_event_2003
from DataFrame_Analysis import cumulative_returns_event_2008
from DataFrame_Analysis import cumulative_returns_event_2020
from DataFrame_Analysis import cumulative_returns_event_2022


def get_applicant_info():
    user_Commodity_weight = questionary.text("Enter your Commodity weight of portfolio  as %:").ask()
    user_GOLD_weight = questionary.text("Enter your Gold weight of portfolio as %:").ask()
    user_RE_weight = questionary.text("Enter your Real Estate weight of portfolio as %:").ask()
    user_Equity_weight = questionary.text("Enter your Equity weight of portfolio as %:").ask()
    user_Fixedincome_weight = questionary.text("Enter your Fixed Income weight of portfolio as %:").ask()

    user_Commodity_weight = float(user_Commodity_weight)/100
    user_GOLD_weight = float(user_GOLD_weight)/100
    user_RE_weight = float(user_RE_weight)/100
    user_Equity_weight = float(user_Fixedincome_weight)/100
    user_Fixedincome_weight = float(user_Fixedincome_weight)/100
    return [user_Commodity_weight,user_GOLD_weight,user_RE_weight,user_Equity_weight,user_Fixedincome_weight]

def user_wt_returns(applicant_info):
    user_returns_2001 = cumulative_returns_event_2001.mul(applicant_info).sum(axis=1)
    print(f"your return during 911 is {user_returns_2001[-1]:.2%}")
    user_returns_2003 = cumulative_returns_event_2003.mul(applicant_info).sum(axis=1)
    print(f"your return during War is {user_returns_2003[-1]:.2%}")
    user_returns_2008 = cumulative_returns_event_2008.mul(applicant_info).sum(axis=1)
    print(f"your return during housing bubble is {user_returns_2008[-1]:.2%}")
    user_returns_2020 = cumulative_returns_event_2020.mul(applicant_info).sum(axis=1)
    print(f"your return during Covid is {user_returns_2020[-1]:.2%}")
    user_returns_2022 = cumulative_returns_event_2022.mul(applicant_info).sum(axis=1)
    print(f"your return during Invasion is {user_returns_2022[-1]:.2%}")

    return user_returns_2001,user_returns_2003,user_returns_2008,user_returns_2020,user_returns_2022



def run():
    """The main function for running the script."""
    applicant_info = get_applicant_info()
    # Get the applicant's information

    user_wt_returns(applicant_info)

    print(f"your optiam allocation during 911 is,\n{optimal_risky_port_2001}")
    print(f"your optiam allocation during War in Iraq is,")
    print(optimal_risky_port_2003)
    print(f"your optiam allocation during housing bubble is,")
    print(optimal_risky_port_2008)
    print(f"your optiam allocation during Pandemic is,")
    print(optimal_risky_port_2020)
    print(f"your optiam allocation during Russian invasion is,")
    print(optimal_risky_port_2022)

if __name__ == "__main__":
    fire.Fire(run)