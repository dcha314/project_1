def load_portfolio_weight():
    """Ask for the file path to the latest portfolio data and load the CSV file.
    Returns:
        The from the CSV file.
    """

    csvpath = questionary.text("Enter a file path (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)