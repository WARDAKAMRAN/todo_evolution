"""Phase 2: Agentic Web API - Entry Point"""

from fastapi import FastAPI

app = FastAPI(title="Todo Evolution - Phase 2 API", version="1.0.0")


@app.get("/")
async def root():
    """Root endpoint for the API"""
    return {"message": "Welcome to Phase 2: Agentic Web API", "status": "operational"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "phase": "2", "component": "web-api"}

# Additional API routes will be implemented following the specification
# See specs/2-phase-2-spec.md for detailed requirements

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
