pipeline {
    agent any

    options {
        skipDefaultCheckout(true) // Không tự động checkout từ SCM
        cleanWs()                 // Dọn workspace đầu mỗi lần build
    }

    environment {
        DOCKER_BUILDKIT = 1       // Bật buildkit nếu cần
    }

    stages {
        stage('Clone Git Repo') {
            steps {
                echo '📥 Cloning repository...'
                sh '''
                    echo 🔍 Trước khi xóa:
                    ls -al || true
                    rm -rf app
                    echo 🧹 Sau khi xóa:
                    ls -al || true
                    git clone https://github.com/congnam101/flask-mysql-app.git app
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('app') {
                    echo '🔧 Building Docker image...'
                    sh 'docker build -t flask_mysql_app_web .'
                }
            }
        }

        stage('Stop Existing Containers') {
            steps {
                dir('app') {
                    echo '🛑 Stopping containers (if any)...'
                    sh 'docker-compose down || true'
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                dir('app') {
                    echo '🚀 Starting containers...'
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                echo '🔍 Verifying deployment...'
                sh 'curl -f http://localhost:5000 || echo "⚠️ App may not be ready yet."'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed. Check logs above.'
        }
    }
}
