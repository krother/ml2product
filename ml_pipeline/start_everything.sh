
cd data_source
uvicorn rest_api:app --reload --port 8000

cd ../model_training
uvicorn predict_api:app --reload --port 8001

