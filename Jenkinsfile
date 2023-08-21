pipeline{
    agent any

    stages{
        stage('Build Image') {
            steps {
                sript{
                    dockerapp = docker.build("thiagogonncalves/lavajato-backend:latest" , '-f ./Dockerfile .')
                }
            }
        }
    }
}