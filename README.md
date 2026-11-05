# SQL Academy Version 2
Dark 3D + neon green Flask/SQLite learning platform. Lessons use Roman Urdu + English, topic levels, progress tracking, practice playground, sample data and quiz section.

## Run in VS Code
1. Install Python 3.10+ and open this folder in VS Code.
2. Create environment: `python -m venv .venv`
3. Activate: Windows ` .venv\\Scripts\\activate` | macOS/Linux `source .venv/bin/activate`
4. Install: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Open http://127.0.0.1:5000

The SQLite database initializes automatically. Playground accepts read-only SELECT/WITH statements only. Mutating SQL is shown as educational examples and cannot be executed there.

## GitHub
Create a repository, then run `git init`, `git add .`, `git commit -m "SQL ACADEMY V3"`, `git branch -M main`, `git remote add origin YOUR_REPOSITORY_URL`, `git push -u origin main`. Do not commit secrets or `.venv`.

## Render deployment
Create a Render Web Service from your GitHub repository, choose Python, build command `pip install -r requirements.txt`, start command `gunicorn app:app` (add `gunicorn` to requirements). Free instance availability and persistent disk policies can change; SQLite on ephemeral disks may reset on redeploy. For durable public hosting, use a managed persistent disk or PostgreSQL.
