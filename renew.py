name: E5 Dev Renewal

on:
  schedule:
    # run once per day (adjust as needed)
    - cron: '0 4 * * *'
  workflow_dispatch:

jobs:
  renew:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run renewal script
        env:
          AZ_TENANT_ID: ${{ secrets.AZ_TENANT_ID }}
          AZ_CLIENT_ID: ${{ secrets.AZ_CLIENT_ID }}
          AZ_CLIENT_SECRET: ${{ secrets.AZ_CLIENT_SECRET }}
          M365_EMAIL: ${{ secrets.M365_EMAIL }}
          M365_PASSWORD: ${{ secrets.M365_PASSWORD }}
        run: |
          python renew.py
