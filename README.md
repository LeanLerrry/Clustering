# topic-clustering/README.md

# Topic Clustering

A Python tool for clustering similar topics using sentence transformers and cosine similarity.

## Project Structure

```
topic-clustering
├── src
│   ├── __init__.py
│   ├── analyzer
│   │   ├── __init__.py
│   │   └── text_analyzer.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── embeddings.py
│   └── main.py
├── requirements.txt
├── run_api.py
└── README.md
```

## Installation

1. Clone this repository
2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```
3. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

### As a CLI Tool
Run the main script:
```bash
python src/main.py
```

### As an API
Run the API server:
```bash
python run_api.py
```

The API will be available at `http://localhost:5000` with the following endpoints:

#### Health Check
```bash
GET /health
```

#### Topic Clustering
```bash
POST /cluster
```

Parameters (multipart/form-data):
- `file`: Excel file to process
- `text_column`: Name of the column containing text to cluster
- `threshold`: Similarity threshold (0.0-1.0, default: 0.5)
- `batch_size`: Processing batch size (default: 500)

Example using curl:
```bash
curl -X POST -F "file=@input.xlsx" -F "text_column=text" -F "threshold=0.7" http://localhost:5000/cluster
```

## Dependencies

The project requires the following Python packages:

- pandas
- numpy
- sentence-transformers
- scikit-learn
- torch
- openpyxl
- flask
- flask-restful

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Environment: Docker
   - Region: Choose nearest to your users
   - Branch: main
   - Root Directory: ./
   - Docker Command: Leave empty (will use Dockerfile)
   - Instance Type: Starter or higher depending on needs

The service will automatically build and deploy your application. The API will be available at your Render service URL.

Environment Variables (if needed):
- `FLASK_ENV`: production
- `FLASK_APP`: src.api:app

Note: The free tier has some limitations. For production use, consider using a paid instance type.

## License

This project is licensed under the MIT License.