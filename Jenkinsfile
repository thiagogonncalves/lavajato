pipeline{
    agent any

    stages{
        stage('Build Image') {
            steps {
                script{
                    dockerapp = docker.build("thiagogonncalves/lavajato-backend")
                }
            }
        }
    }
}