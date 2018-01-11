pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm

            }
        }
        stage('Deploy') {
            steps {
                sh 'scp *.py appuser@172.31.20.73:/opt/appuser'
            }
        }
        stage('Start Application') {
            steps {
                sh 'ssh appuser@172.31.20.73 python /opt/appuser/fantasyranks.py'
            }
        }
    }
}