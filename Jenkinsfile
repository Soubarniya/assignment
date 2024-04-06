pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                
                git branch: 'main', url: 'https://github.com/your/repo.git'
            }
        }
        
        stage('Build') {
            steps {

                script {
                    docker.build('test1')
                }
            }
        }
        
        stage('Test') {
            steps {
                
                sh 'docker run test1 python -m unittest'
            }
        }
        
        stage('Push to ECR') {
            steps {
                // Authenticate Docker to ECR
                script {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-credentials-id', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                        sh 'aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com'
                    }
                }
                
                // Push the Docker image to ECR
                script {
                    docker.withRegistry('<aws_account_id>.dkr.ecr.<region>.amazonaws.com', 'ecr:us-west-2') {
                        docker.image('test1').push('latest')
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the Docker image to ECS or any other deployment target
                // You can use AWS ECS CLI, AWS CDK, or other deployment tools here
                // Example:
                script {
                    sh 'ecs-cli compose --project-name mydatahandler service up'
                }
            }
        }
    }
}
