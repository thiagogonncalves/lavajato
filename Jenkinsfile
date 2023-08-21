pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                script {
                    def dockerapp = docker.build("thiagogonncalves/lavajato-backend", "-f ./Dockerfile .")
                }
            }
        }
    }
}
