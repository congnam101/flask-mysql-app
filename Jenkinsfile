pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask_mysql_app_web'
    }

    stages {
        stage('Checkout Source') {
            steps {
                git 'https://github.com/congnam101/flask-mysql-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🔧 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop Existing Containers') {
            steps {
                echo '🛑 Stopping old containers...'
                sh 'docker compose down || true'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo '🚀 Deploying with Docker Compose...'
                sh 'docker compose up -d'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo '🔍 Verifying app is running...'
                sh 'curl -f http://localhost:5000 || echo "⚠️ App may not be ready yet."'
            }
        }
    }

    post {
        success {
            echo "✅ Deployment succeeded!"
        }
        failure {
            echo "❌ Deployment failed. Check logs above."
        }
    }
}
