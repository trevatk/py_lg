"""HTTP server for the application"""
import os

import uvicorn

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

# create fastapi application
app = FastAPI()


@app.get("/health")
def health():
    """Health check endpoint"""
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "OK"})


def serve():
    """Start the HTTP server"""
    # read port from environment variable
    http_port: str = os.getenv("SERVER_HTTP_PORT", "8080")
    # run uvicorn server
    uvicorn.run(app=app, host="0.0.0.0", port=int(http_port, base=0))
