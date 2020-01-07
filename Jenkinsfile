pipeline{
        agent any
        
        stages{
                stage('--deploy--'){
                        steps{
                                sh '''ssh -T 35.242.182.148 << BOB
				      git clone https://github.com/AIbrahimQA/new_project.git
                                      cd new_project/
                                      docker-compose up -d --build
                                      '''
                        }
                }
        }
}
