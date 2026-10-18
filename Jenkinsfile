
pipeline {
    agent any

    stages {
        stage('Environment Check') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                      -e PYTHONDONTWRITEBYTECODE=1 \
                      -v "$WORKSPACE:/app" \
                      -w /app \
                      python:3.11-slim \
                      sh -c "pip install --no-cache-dir -r requirements.txt && python test_system.py"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t careerwise-ai:${BUILD_NUMBER} .'
            }
        }
    }
}


