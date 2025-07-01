pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = 1
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                echo '🔄 Checking out source code...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🚀 Building Docker image...'
                sh 'docker build -t flask_app:latest .'
            }
        }

        stage('Stop Existing Containers') {
            steps {
                echo '🛑 Stopping existing containers...'
                sh '''
                    echo "📦 Dừng và xóa container cũ (nếu có)..."
                    docker-compose down --remove-orphans || echo "Không có container cũ để dừng."
                '''
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo '🚢 Deploying application...'
                sh 'docker-compose up -d'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo '✅ Checking running containers...'
                sh 'docker ps'
            }
        }
    }

    post {
        failure {
            echo '❌ Deployment failed. Check logs above.'
        }
        success {
            echo '🎉 Deployment successful!'
        }
    }
}
