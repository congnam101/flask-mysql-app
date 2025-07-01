pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask_app"
    }

    stages {
        stage('Clone Source') {
            steps {
                 git branch: 'main', url: 'https://github.com/congnam101/flask-mysql-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d --build'
            }
        }
    }
}

