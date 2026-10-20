

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

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        set -eu
                        export DOCKER_CONFIG="$(mktemp -d)"
                        trap 'docker logout >/dev/null 2>&1 || true; rm -rf "$DOCKER_CONFIG"' EXIT

                        printf '%s' "$DOCKERHUB_TOKEN" | docker login \
                          --username "$DOCKERHUB_USERNAME" --password-stdin

                        docker tag "careerwise-ai:${BUILD_NUMBER}" \
                          "$DOCKERHUB_USERNAME/careerwise-ai:${BUILD_NUMBER}"

                        docker push "$DOCKERHUB_USERNAME/careerwise-ai:${BUILD_NUMBER}"

                        docker tag "careerwise-ai:${BUILD_NUMBER}" \
                          "$DOCKERHUB_USERNAME/careerwise-ai:latest"

                        docker push "$DOCKERHUB_USERNAME/careerwise-ai:latest"
                    '''
                }
            }
        }

        stage('Deploy to Minikube') {
            agent {
                label 'windows-minikube'
            }
            steps {
                bat '''
                    kubectl config current-context
                    kubectl set image deployment/careerwise-ai careerwise-ai=avniirai/careerwise-ai:%BUILD_NUMBER%
                    kubectl rollout status deployment/careerwise-ai --timeout=180s
                    kubectl get pods
                    kubectl get services
                '''
            }
        }
    }
}

