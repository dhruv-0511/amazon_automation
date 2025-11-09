from fastapi import FastAPI
from api.api import api_router
import uvicorn

app = FastAPI(title='Order Automation', openapi_url="/api/api/openapi.json")

app.include_router(api_router)

# Only start the server when this file is executed as a script.
# This prevents uvicorn from being started when the module is imported
# (for example, by `uvicorn` itself or by tests), which can cause
# "asyncio.run() cannot be called from a running event loop" errors.
if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)