ARG PYTHON_VERSION=3.13.3
FROM python:${PYTHON_VERSION}-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Create a non-privileged user that the app will run under.
RUN useradd --create-home appuser

# Set folder for app to be located in user's home directory.
WORKDIR /home/appuser/trapper-server

# Switch to the non-privileged user to run the application.
USER appuser

# Upgrade pip and install dependencies.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install --user --upgrade pip && \
    python -m pip install --user --no-cache-dir -r requirements.txt

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["python", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]