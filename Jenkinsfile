pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask_app"
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {
        stage('Checkout Source') {
            steps {
                git branch: 'main', url: 'https://github.com/congnam101/flask-mysql-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ."
                }
            }
        }

        stage('Stop Existing Containers') {
            steps {
                script {
                    sh "docker-compose down || true"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    sh "docker-compose up -d --build"
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                sh "docker ps"
            }
        }
    }

    post {
        success {
            echo '✅ Deployment completed successfully!'
        }
        failure {
            echo '❌ Deployment failed. Check logs above.'
        }
    }
}
