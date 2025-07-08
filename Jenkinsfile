pipeline {
    agent any

    stages {
        stage('Clone Source') {
            steps {
                git 'https://github.com/congnam101/flask-mysql-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask_mysql_app_web .'
            }
        }

        stage('Stop Existing Containers') {
            steps {
                sh 'docker compose down || true'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'curl -f http://localhost:5000 || echo "App may not be ready yet."'
            }
        }
    }

    post {
        failure {
            echo "❌ Deployment failed. Check logs above."
        }
    }
}
