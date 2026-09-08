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

        stage('Trivy FS Scan') {
            steps {
                sh '''
                    trivy fs . \
                        --format json \
                        --output trivy-fs-report.json
                '''
            }
        }

        stage('Unit Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/pytest
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

        stage('Trivy Image Scan') {
            steps {
                sh '''
                    trivy image \
                        --format json \
                        --output trivy-image-report.json \
                        ${IMAGE_NAME}:latest
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

    post {
        always {
            archiveArtifacts artifacts: 'trivy-*-report.json',
                             allowEmptyArchive: true
        }
    }
}
