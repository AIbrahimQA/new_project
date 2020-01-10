pipeline{
        agent any
        
        stages{
                stage('--deploy--'){
                        steps{
                                sh '''ssh 35.246.0.219  << BOB
				      source ~/.bashrc		
				      git clone https://github.com/AIbrahimQA/new_project.git
			              cd new_project/
				      git pull
				      docker-compose up -d --build
                                
                                      '''
                        }
                }
        }
}
