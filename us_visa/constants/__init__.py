# us_visa/constants.py

# === Mongo basics ===
DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "MONGODB_URL"  # name of the ENV var that holds your MongoDB URI

# === Pipeline / paths ===
PIPELINE_NAME = "us_visa"
ARTIFACT_DIR = "artifact"

# Data Ingestion
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"

# File names
FILE_NAME = "us_visa.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

# Split ratio
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

# Collection used by data ingestion
DATA_INGESTION_COLLECTION_NAME = COLLECTION_NAME
