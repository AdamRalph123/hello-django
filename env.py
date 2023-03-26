from pathlib import Path
import os
import dj_database_url
import env

os.environ["VARIABLE_NAME"] = "variable value"

SECRET_KEY = os.environ.get('SECRET_KEY', '')

os.environ.setdefault("DATABASE_URL", postgres://lxuyofcz:C_sCQ2wyUEoNH_mcbJ1QKqDTH9Y42bJp@mel.db.elephantsql.com/lxuyofcz)
