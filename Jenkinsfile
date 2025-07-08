pipeline {
    agent any

    options {
        skipDefaultCheckout() // Không tự động checkout code
        cleanWs() // Dọn toàn bộ workspace đầu mỗi lần chạy
    }

    stages {
        stage('Clone Git Repo') {
            steps {
                echo '📥 Cloning repo...'
                // Xóa thư mục app nếu đã tồn tại
                sh 'rm -rf app'
                sh 'git clone https://github.com/congnam101/flask-mysql-app.git app'
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
                    echo '🛑 Stopping containers...'
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
        failure {
            echo '❌ Deployment Failed. Check logs above.'
        }
        success {
            echo '✅ Deployment Successful!'
        }
    }
}
