from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import sys
from pathlib import Path

project_root=Path(__file__).parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from routers import auth

app=FastAPI()

app.include_router(router=auth.router)