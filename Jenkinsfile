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
                mkdir -p $WORKSPACE/allure-results

                docker run --rm \
                  -e API_KEY=$API_KEY \
                  -v $WORKSPACE/allure-results:/app/allure-results \
                  qa-api-tests pytest --alluredir=allure-results

                ls -la $WORKSPACE/allure-results
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