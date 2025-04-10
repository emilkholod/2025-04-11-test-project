from functools import lru_cache

import pandas as pd
from rich.console import Console

from freelancer_analyzer_app.config import get_settings


@lru_cache(maxsize=1)
def get_df() -> pd.DataFrame:
    settings = get_settings()
    return pd.read_csv(settings.CSV_FILE)


def get_response_console() -> Console:
    return Console()


def get_info_console() -> Console:
    return Console()
