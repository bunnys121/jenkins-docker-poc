pipeline {
    agent any

    environment {
        IMAGE_NAME = "poc7-python-app"
        IMAGE_TAG = "latest"
        IMAGE_TAR = "/tmp/poc7-python-app.tar"
        ANSIBLE_HOST_KEY_CHECKING = "False"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'ansible',
                    url: 'https://github.com/bunnys121/jenkins-docker-poc.git'
            }
        }

        stage('Verify Tools') {
            steps {
                sh '''
                    echo "Checking required tools..."
                    java -version || true
                    docker --version
                    ansible --version
                    python3 --version || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker image..."
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Save Docker Image') {
            steps {
                sh '''
                    echo "Saving Docker image as tar file..."
                    docker save -o ${IMAGE_TAR} ${IMAGE_NAME}:${IMAGE_TAG}
                    ls -lh ${IMAGE_TAR}
                '''
            }
        }

        stage('Deploy Using Ansible') {
            steps {
                sh '''
                    echo "Deploying Docker container using Ansible..."
                    ansible-playbook -i ansible/inventory ansible/deploy.yml
                '''
            }
        }
    }

    post {
        success {
            echo "POC-7 deployment completed successfully."
        }

        failure {
            echo "POC-7 deployment failed. Please check Jenkins console logs."
        }
    }
}
