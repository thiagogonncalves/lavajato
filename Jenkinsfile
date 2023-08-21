pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerapp = docker.build("thiagogonncalves/lavajato-backend:latest")
                }
            }
        }
    }
}
