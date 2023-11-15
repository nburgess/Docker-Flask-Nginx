from flask import Flask, jsonify, request
import psutil
import docker
import os

app = Flask(__name__)

verification_key = os.getenv("API_VERIFICATION_KEY", "default_key")

@app.route('/data/containers/stats')
def get_container_stats():
    docker_client = docker.from_env()
    containers = docker_client.containers.list()
    container_stats = []
    for container in containers:
        container_stats.append({
            'name': container.name,
            'stats': container.stats(stream=False)
        })
    return jsonify({'container_stats': container_stats})

@app.route('/data/memory')
def get_memory_usage():
    return jsonify({'current_memory_usage': psutil.virtual_memory()._asdict()})

@app.route('/data/cpu')
def get_cpu_usage():
    return jsonify({'current_cpu_usage': psutil.cpu_percent()})

@app.before_request
def verify_api_key():
    if request.headers.get('API-KEY') != verification_key:
        return jsonify({'error': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)