pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImageTag = "lavajato-backend:latest"

                    // Execute o comando Docker para construir a imagem
                    sh "docker build -t ${dockerImageTag} /home/gthiago/Documentos/projetos/lavajato"

                    // Verifique se a construção foi bem-sucedida
                    sh "docker image ls ${dockerImageTag}"
                }
            }
        }

        // Outros estágios do pipeline podem ser adicionados aqui
    }
}
