import random

def calculate_num_panels(usable_area_m2, panel_area_m2=1.6):
    """
    Calculate the number of panels that fit in the usable rooftop area.
    Default panel size is 1.6 m².
    """
    return int(usable_area_m2 / panel_area_m2)

def calculate_kw_installed(num_panels, watts_per_panel=300):
    """
    Calculate total installed capacity in kilowatts.
    Default panel wattage is 300W.
    """
    return round((num_panels * watts_per_panel) / 1000, 2)

def calculate_annual_output(kw_installed, sunlight_hours_per_day=None):
    """
    Estimate annual energy output in kWh.
    Sunlight hours are randomized if not provided (range: 4.5 to 6.5).
    """
    if sunlight_hours_per_day is None:
        sunlight_hours_per_day = random.uniform(4.5, 6.5)
    return round(kw_installed * sunlight_hours_per_day * 365, 2)

def calculate_cost(kw_installed, cost_per_watt=None):
    """
    Estimate installation cost in USD.
    Cost per watt is randomized between $0.45 and $0.65 if not provided.
    """
    if cost_per_watt is None:
        cost_per_watt = random.uniform(0.45, 0.65)
    return round(kw_installed * 1000 * cost_per_watt, 2)

def calculate_savings(annual_output_kwh, electricity_rate=None):
    """
    Estimate annual savings in USD based on energy output.
    Electricity rate is randomized between $0.10 and $0.15 if not provided.
    """
    if electricity_rate is None:
        electricity_rate = random.uniform(0.10, 0.15)
    return round(annual_output_kwh * electricity_rate, 2)

def calculate_roi_years(cost, annual_savings):
    """
    Estimate return on investment (ROI) in years.
    Returns infinity if savings is zero.
    """
    return round(cost / annual_savings, 2) if annual_savings > 0 else float('inf')
