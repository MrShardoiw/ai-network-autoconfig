# AI Network Auto-Config (Simulation Mode)

This is a dummy project that simulates an AI-based network configuration agent.

## How it works:
1. It uses a **Dummy AI** script to "generate" configs (No OpenAI account needed).
2. It uses a **Simulation Runner** to "push" configs (No real router needed).
3. It runs automatically via GitHub Actions.

## To run locally:
```bash
python agent/ai_agent.py
### 📄 5. The GitHub Workflow (`.github/workflows/deploy.yml`)
This is the file that makes the code run automatically on GitHub. Because this is a **Dummy** version, we don't need to worry about "Secrets" yet—it will run just to show you it works!

**File:** `.github/workflows/deploy.yml`
```yaml
name: Simulation Deployment

on: [push] # Runs every time you push code to GitHub

jobs:
  run-simulation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: pip install pyyaml  # Only pyyaml is needed for the dummy version

      - name: Run Dummy Agent
        run: python agent/ai_agent.py