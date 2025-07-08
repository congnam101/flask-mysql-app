pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = 1
    }

    options {
        // Dọn workspace trước khi build để tránh trùng file/thư mục
        skipDefaultCheckout()
        cleanWs()
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                echo '🔄 Checking out source code...'
                // Clone lại vào workspace sạch
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
                    echo "📦 Dừng container docker-compose (nếu có)..."
                    docker-compose down --remove-orphans || echo "Không có container docker-compose nào."

                    echo "🧹 Xóa container flask_web và flask_db nếu bị kẹt..."
                    docker rm -f flask_web || true
                    docker rm -f flask_db || true
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
                echo '🔍 Trying to connect to http://localhost:5000 ...'
                sh 'curl -f http://localhost:5000 || echo "⚠️ App chưa sẵn sàng hoặc lỗi kết nối."'
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
