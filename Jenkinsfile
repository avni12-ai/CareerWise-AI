

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment Check') {
            steps {
                sh 'python3 --version'
                sh 'docker --version'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t careerwise-ai:${BUILD_NUMBER} .'
                sh 'docker images careerwise-ai'
            }
        }
    }
}
