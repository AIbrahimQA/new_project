pipeline{
        agent any
        
        stages{
                stage('--deploy--'){
                        steps{
                                sh '''ssh 34.89.80.253 << EOF
                                      cd passwordgen/
                                      git pull
                                      docker-compose up -d --build
                                      '''
                        }
                }
        }
}
