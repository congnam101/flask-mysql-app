pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = 1
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                echo '🔄 Checking out source code...'
                // Bạn có thể chọn 1 trong 2 cách sau:

                // Cách 1: Nếu đã cấu hình `SCM` trong Pipeline Job
                checkout scm

                // Hoặc nếu chạy trực tiếp:
                // git branch: 'main', url: 'https://github.com/congnam101/flask-mysql-app.git'
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
                    if docker compose ps -q | grep -q .; then
                        docker compose down
                    fi
                '''
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo '🚢 Deploying application...'
                sh 'docker compose up -d'
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
