pipeline {
    agent any
    environment {
        VIRTUAL_ENV = 'venv'
    }
    stages {
        // get the repository from github
        stage('Cloning from Github repository ... ') {
            steps {
                script{
                    echo "Cloning from Github"
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/mohamed-elaouan/Hotel_Reservation_MLOps-Project.git']])                } 
            }
        }
        // environment 
        stage('Making virtual environment ....') {
            steps {
                script{
                    echo "virtual environment "
                    sh '''
                    python -m venv ${VIRTUAL_ENV}
                    source ${VIRTUAL_ENV}/bin/activate
                    pip install -e .
                    pip install dvc 
                    '''
                }
            }
        }
        //  Dvc Pull => obtaint the data 
        stage('Dvc pull data from GCP bucket storage data source/ data entry.') {
            steps {
                WithCredentials([file(credentialsId: 'Anime-Recommendation-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script{
                            echo "Dvc pull data from GCP"
                            sh '''
                                source ${VIRTUAL_ENV}/bin/activate
                                dvc pull
                                '''
                    }
                }
                
            }

    }
}
