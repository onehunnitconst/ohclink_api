def get_database_url(
    user: str,
    password: str,
    host: str,
    port: str,
    db_name: str,
) -> str:
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"