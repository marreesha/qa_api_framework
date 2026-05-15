pipeline {
    agent any

    environment {
        API_KEY = credentials('api-key')
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t qa-api-tests .'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                docker run --rm \
                  --env-file .env \
                  -v $(pwd)/allure-results:/app/allure-results \
                  qa-api-tests pytest --alluredir=allure-results
                '''
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}