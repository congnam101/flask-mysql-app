pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/YOUR-USERNAME/flask-mysql-app.git'
            }
        }
        stage('Backup Source') {
            steps {
                sh './backup.sh'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("flask-mysql-app:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Run with Docker Compose') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }
}
