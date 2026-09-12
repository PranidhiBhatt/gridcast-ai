from fastapi import FastAPI

app = FastAPI(
    title="GridCast AI",
    description=(
        "An AI-powered hyperlocal weather-to-energy intelligence platform "
        "for renewable grid optimisation. Milestone 0 provides a health endpoint."
    ),
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "GridCast AI"}
