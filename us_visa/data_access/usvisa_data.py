# us_visa/data_access/usvisa_data.py

import os
import sys
from typing import Optional

import numpy as np
import pandas as pd
import pymongo

try:
    from dotenv import load_dotenv
except ImportError:
    # Fallback no-op if python-dotenv is not installed in the runtime env.
    load_dotenv = lambda *args, **kwargs: None  # noqa: E731

from us_visa.exception import USvisaException
from us_visa.constants import DATABASE_NAME, COLLECTION_NAME, MONGODB_URL_KEY

load_dotenv(override=True)  # Populate environment from a local .env if available.

DB_NAME = DATABASE_NAME
DEFAULT_COLLECTION_NAME = COLLECTION_NAME


class USvisaData:
    """
    Export MongoDB collection data as a pandas DataFrame using a simple, modular client.
    """

    def __init__(self) -> None:
        try:
            connection_url = os.getenv(MONGODB_URL_KEY)
            if not connection_url:
                raise Exception(f"Environment key '{MONGODB_URL_KEY}' is not set or empty.")
            if "<db_password>" in connection_url:
                raise Exception(
                    f"Environment key '{MONGODB_URL_KEY}' still contains the '<db_password>' placeholder. "
                    "Update your .env with the actual password (URL-encoded if needed)."
                )

            self.client = pymongo.MongoClient(connection_url)
        except Exception as e:
            raise USvisaException(e, sys)

    def export_collection_as_dataframe(
        self,
        collection_name: Optional[str] = None,
        database_name: Optional[str] = None,
    ) -> pd.DataFrame:
        try:
            db_name = database_name or DB_NAME
            coll_name = collection_name or DEFAULT_COLLECTION_NAME

            data_base = self.client[db_name]
            collection = data_base[coll_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)

            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e, sys)
