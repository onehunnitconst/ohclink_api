import uvicorn


def main() -> None:
    """Run the app exposed by the package as `ohclink_api.app:app` using uvicorn.

    Uses the default host `127.0.0.1` and port `8000`. `reload=True` is enabled
    for development convenience.
    """
    uvicorn.run("ohclink_api.app:app", host="127.0.0.1", port=8000, reload=True)

