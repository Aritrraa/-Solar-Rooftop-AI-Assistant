import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

def generate_report(data: dict):
    prompt = (
        f"Generate a simple, friendly solar installation report for the following data:\n\n"
        f"Usable Rooftop Area: {data['usable_area_m2']} m²\n"
        f"Number of Panels: {data['num_panels']}\n"
        f"Installed Capacity: {data['kw_installed']} kW\n"
        f"Annual Energy Output: {data['annual_output_kwh']} kWh\n"
        f"Estimated Installation Cost: ${data['estimated_cost_usd']}\n"
        f"Estimated Annual Savings: ${data['savings_per_year_usd']}\n"
        f"Expected ROI: {data['roi_years']} years\n"
    )

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENROUTER_API_KEY environment variable is not set.")

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    response_json = response.json()
    if "choices" not in response_json:
        raise ValueError("Invalid API response: 'choices' key not found.")

    return response_json["choices"][0]["message"]["content"]
