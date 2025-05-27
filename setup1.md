# Local Setup Instructions

## 1. Prerequisites

- Python 3.13 installed (or your project's required Python version)
- Git (optional, if cloning from a repo)
- An API key for OpenRouter AI (`OPENROUTER_API_KEY`)

---

## 2. Clone the Repository (Optional)

```bash
git clone https://github.com/Aritrraa/-Solar-Rooftop-AI-Assistant.git
cd -Solar-Rooftop-AI-Assistant
```

---

## 3. Create and Activate a Virtual Environment

On Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

On macOS/Linux (bash):

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Set Environment Variables

Create a `.env` file in the project root with the following content:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenRouter API key.

---

## 6. Run the Application

```bash
python app.py
```

Or if you use Streamlit or another framework, adjust accordingly.

---

## 7. Notes

- Make sure your internet connection is active to access the API.
- If you encounter encoding errors while running tools like `pipreqs`, try running them with `--encoding=utf-8`.
- Check logs for detailed error messages.
