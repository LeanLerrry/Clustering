from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from analyzer.text_analyzer import TextAnalyzer
import pandas as pd

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return jsonify({
        'status': 'API is running',
        'endpoints': {
            'health': '/health',
            'cluster': '/cluster'
        }
    })

class HealthCheck(Resource):
    def get(self):
        return {'status': 'healthy'}, 200

class TopicCluster(Resource):
    def post(self):
        if 'file' not in request.files:
            return {'error': 'No file provided'}, 400
        
        file = request.files['file']
        text_column = request.form.get('text_column', 'text')
        threshold = float(request.form.get('threshold', 0.5))
        batch_size = int(request.form.get('batch_size', 500))
        
        try:
            df = pd.read_excel(file)
            if text_column not in df.columns:
                return {'error': f'Column {text_column} not found in file'}, 400
            
            analyzer = TextAnalyzer()
            results = analyzer.analyze_texts(
                texts=df[text_column].tolist(), 
                threshold=threshold,
                batch_size=batch_size
            )
            
            # Create topic number mapping
            topic_mapping = {}
            for cluster in results:
                topic_num = cluster['topic_number']
                for idx in cluster['indices']:
                    topic_mapping[idx] = topic_num
            
            # Format response
            response = {
                'total_topics': len(results),
                'clusters': results,
                'topic_mapping': topic_mapping
            }
            
            return jsonify(response)
            
        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(HealthCheck, '/health')
api.add_resource(TopicCluster, '/cluster')

if __name__ == '__main__':   
    app.run(debug=False, host='0.0.0.0', port=5000)
