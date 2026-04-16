pipeline {
    agent any
    stages {
        stage('Cloning from Github repository ... ') {
            steps {
                script{
                    echo "Cloning from Github"
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/mohamed-elaouan/Hotel_Reservation_MLOps-Project.git']])                } 
            }
        }
    }
}
