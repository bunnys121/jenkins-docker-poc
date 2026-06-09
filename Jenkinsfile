pipeline {
    agent any

    environment {
        IMAGE_NAME = "poc2-python-app"
        CONTAINER_NAME = "poc2-container"
        APP_PORT = "5000"
    }

    stages {

        stage('1. Checkout Code') {
            steps {
                echo 'Cloning source code from Git...'
                checkout scm
            }
        }

        stage('2. Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    python3 --version
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('3. Build and Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    pytest -v
                '''
            }
        }

        stage('4. Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('5. Deploy Docker Container') {
            steps {
                echo 'Deploying application container...'
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true

                    docker run -d \
                      --name $CONTAINER_NAME \
                      -p $APP_PORT:5000 \
                      $IMAGE_NAME:latest

                    docker ps
                '''
            }
        }
    }

    post {
        success {
            echo 'POC-2 completed successfully: Application deployed using Docker.'
        }

        failure {
            echo 'POC-2 failed. Please check Jenkins console logs.'
        }
    }
}
