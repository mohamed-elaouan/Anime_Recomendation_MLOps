pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {

        // Clone the repository from GitHub
        stage('Clone from GitHub repository') {
            steps {
                script {
                    echo "Cloning from GitHub..."
                    checkout scmGit(
                        branches: [[name: '*/master']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/mohamed-elaouan/Hotel_Reservation_MLOps-Project.git'
                        ]]
                    )
                }
            }
        }

        // Create virtual environment and install dependencies
        stage('Setup virtual environment') {
            steps {
                script {
                    echo "Setting up virtual environment..."
                    sh '''
                        python3 -m venv ${VIRTUAL_ENV}
                        . ${VIRTUAL_ENV}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                        pip install dvc
                    '''
                }
            }
        }

        // Pull data using DVC from GCP bucket
        stage('DVC pull data from GCP bucket') {
            steps {
                withCredentials([file(credentialsId: 'Anime-Recommendation-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo "Pulling data using DVC..."
                        sh '''
                            . ${VIRTUAL_ENV}/bin/activate
                            dvc pull
                        '''
                    }
                }
            }
        }
    }
}