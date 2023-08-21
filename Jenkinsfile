pipeline{
    agent any

    stages{
        stage('Build Image') {
            steps {
                script{
                    dockerapp = docker.build("thiagogonncalves/lavajato-backend", '-f $HOME/Documentos/projetos/lavajato/Dockerfile .')
                }
            }
        }
    }
}