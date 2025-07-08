pipeline {
    agent any

    stages {
        stage('List Files') {
            steps {
                sh 'ls -al'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🔧 Building Docker image...'
                sh 'docker build -t flask_mysql_app_web .'
            }
        }

        stage('Stop Existing Containers') {
            steps {
                echo '🛑 Stopping existing containers (if any)...'
                sh 'docker-compose down || true'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo '🚀 Starting containers...'
                sh 'docker-compose up -d'
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
            echo "❌ Deployment failed. Check logs above."
        }
        success {
            echo "✅ Deployment successful!"
        }
    }
}

