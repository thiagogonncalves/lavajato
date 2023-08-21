pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerapp = docker.build("thiagogoncalves/lavajato-backend")
                }
            }
        }
    }
}
