pipeline{
        agent any
        
        stages{
                stage('--deploy--'){
                        steps{
                                sh '''ssh -T 34.89.80.253 << BOB
                                      cd passwordgen/
                                      git pull
                                      docker-compose up -d --build
                                      '''
                        }
                }
        }
}
