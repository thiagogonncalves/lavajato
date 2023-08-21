pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                dir('/home/gthiago/Documentos/projetos/lavajato') {
                    // Defina as etapas necessárias para construir a imagem Docker aqui
                    script {
                        def dockerImageTag = "lavajato-backend:latest"

                        // Execute o comando Docker para construir a imagem
                        sh "docker build -t ${dockerImageTag} ."

                    }
                }
            }
        }
}
