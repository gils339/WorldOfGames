pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    def dockerImage = docker.build("my-flask-app:${BUILD_NUMBER}")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    def dockerContainer = dockerImage.run("-p 8777:80 -v ${pwd()}/dummy_Scores.txt:/Scores.txt")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh("python e2e.py")
                    } finally {
                        def exitCode = dockerContainer.stop()
                        dockerContainer.remove(force: true)
                        if (exitCode != 0) {
                            error("Tests failed.")
                        }
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub-credentials', url: '') {
                        dockerImage.push("${BUILD_NUMBER}")
                    }
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}

