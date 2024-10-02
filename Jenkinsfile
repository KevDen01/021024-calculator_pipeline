pipeline {
    agent any
    
    stages{
        stage('SCM Checkout') {
            steps {
                echo 'Git clone the repo'
            }
        }

        stage('Install dependencies') {
            steps{
                echo 'Install requirements.txt'
            }
        }

        stage('Check for application functionality'){
            steps{
                echo 'Output from the multiplication function'
                //next line needs sh for bash as jenkins is in a ubuntu container 
                sh 'python3 -c "from calculator import multiply; print(multiply(100,50))"'
            }
        }

        stage('Unit Testing') {
            steps{
                echo 'Unit testing started...'
                //unittest discover will look for files with name test in your pwd
                sh 'python3 -m unittest discover'
            }
        }

        stage('Deploy Phase') {
            steps{
                echo 'Deploying the application on ECR'
            }
        }
    }
}