pipeline{
        agent any
        
        stages{
                stage('--deploy--'){
                        steps{
                                sh '''ssh 35.246.0.219  << BOB
				      git clone https://github.com/AIbrahimQA/new_project.git
			              source ~/.bashrc
                                      cd new_project/
				      docker-compose up -d
				      docker-compose down --volumes
			              docker-compose push
                                      docker stack deploy --compose-file docker-compose.yaml stackdeploy
                                      '''
                        }
                }
        }
}
