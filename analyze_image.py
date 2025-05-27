import random

from utils import (
    calculate_num_panels,
    calculate_kw_installed,
    calculate_annual_output,
    calculate_cost,
    calculate_savings,
    calculate_roi_years
)

def analyze_image(image):
    """a
    Simulates analysis of rooftop area from an image and returns solar system metrics.
    """
    # Simulate usable rooftop area between 20 and 80 m²
    usable_area_m2 = round(random.uniform(20, 80), 2)

    # Calculate all metrics
    num_panels = calculate_num_panels(usable_area_m2)
    kw_installed = round(calculate_kw_installed(num_panels), 2)
    annual_output_kwh = round(calculate_annual_output(kw_installed), 2)
    estimated_cost = round(calculate_cost(kw_installed), 2)
    savings_per_year = round(calculate_savings(annual_output_kwh), 2)
    roi_years = round(calculate_roi_years(estimated_cost, savings_per_year), 2)

    # Return results in expected format
    return {
        "usable_area_m2": usable_area_m2,
        "num_panels": num_panels,
        "kw_installed": kw_installed,
        "annual_output_kwh": annual_output_kwh,
        "estimated_cost_usd": estimated_cost,
        "savings_per_year_usd": savings_per_year,
        "roi_years": roi_years
    }
