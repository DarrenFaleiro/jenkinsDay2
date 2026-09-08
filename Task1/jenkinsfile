pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-flask-app"
        CONTAINER_NAME = "my-flask-container"
    }

    stages {

        stage('Clean-up') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p 5500:5500 \
                        ${IMAGE_NAME}:latest
                '''
            }
        }
    }
}
