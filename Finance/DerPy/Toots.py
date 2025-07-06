def coupons_between_date(date_start, date_end, coupons_per_year=2):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    # Parse input dates
    start = datetime.strptime(date_start, "%d.%m.%Y")
    end = datetime.strptime(date_end, "%d.%m.%Y")

    # Step in months (e.g., 6 for semiannual)
    months_step = 12 // coupons_per_year

    # Loop backwards and store year fractions
    year_fractions = []
    current_date = end
    while current_date > start:
        delta_days = (current_date - start).days
        year_frac = delta_days / 365  # using actual/365
        year_fractions.append(year_frac)
        current_date -= relativedelta(months=months_step)

    return sorted(year_fractions)

# Example usage
fractions = coupons_between_date("15.05.2001", "15.11.2002")
print(fractions)