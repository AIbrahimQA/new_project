pipeline{
        agent any
        
        stages{
                stage('--deploy--'){
                        steps{
                                sh '''ssh 35.246.107.87 << BOB
				      git clone https://github.com/AIbrahimQA/new_project.git
                                      cd new_project/
				      docker stop $(docker ps -qa)
                                      docker rm $(docker ps -qa)
                                      docker rmi -f $(docker images -a -q)
				      docker-compose up -d
				      docker-compose down --volumes
			              docker-compose push
                                      docker stack deploy --compose-file docker-compose.yaml stackdeploy
                                      '''
                        }
                }
        }
}
