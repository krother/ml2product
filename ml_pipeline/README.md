
# Data Pipeline Sample Solution

## Usage

### 1. Install packages

Do

    pip install -r requirements.txt

### 2. Start the Data API

Go to the `data_source/` folder (1 level above) and type

    uvicorn rest_api:app --reload

### 3. Test downloading the data

Run

    python get_data.py

You should see the shape of train/test data frames.

### 4. Train the model

Run 

    python model.py

You should see the file `model.pkl` afterwards.

### 5. Start the prediction server

Type
 
    uvicorn prediction_server:app --reload --port 8001

Now go to the browser at [http://localhost:8001/docs](http://localhost:8001/docs) and try it.

## Authors

Lennart Böckenförde, Marie Mink and Kristian Rother

## License

2022 MIT License
