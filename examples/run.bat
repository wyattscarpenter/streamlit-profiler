uv --version || pip install --disable-pip-version-check --break-system-packages uv
uv venv && uv pip install -r requirements.txt
uv run streamlit run basic.py
uv run python -c "input('Press enter to exit...')"
