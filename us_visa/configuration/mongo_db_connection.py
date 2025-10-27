# us_visa/configuration/mongo_db_connection.py

import sys
import os
import pymongo

try:
    from dotenv import load_dotenv
except ImportError:
    # Fallback so the package remains optional at runtime.
    load_dotenv = lambda *args, **kwargs: None  # noqa: E731

from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY

load_dotenv(override=True)  # load values from .env if present, overriding stale env vars

class MongoDBClient:
    """
    Creates and holds a MongoDB client and database handle.
    """
    client = None

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if not mongo_db_url:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                if "<db_password>" in mongo_db_url:
                    raise Exception(
                        f"Environment key: {MONGODB_URL_KEY} still contains the '<db_password>' placeholder. "
                        "Update your .env with the actual password (URL-encoded if needed)."
                    )

                MongoDBClient.client = pymongo.MongoClient(mongo_db_url)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys)
