pipeline{
        agent any
        
        stages{


                stage('--initialise--'){
                        steps{
                                sh '''ssh 35.246.0.219  << BOB
                                docker stop $(docker ps -qa)
                                docker rm $(docker ps -qa)
                                docker rmi -f $(docker images -a -q)
                                rm -rf new_project/
				'''

                        }
                }


                            
                stage('--deploy--'){
                        steps{
                                sh '''ssh 35.246.0.219  << BOB      
				source ~/.bashrc		
				git clone https://github.com/AIbrahimQA/new_project.git
			        cd new_project/
				git pull
				docker stack rm passgen
				docker-compose up -d --build
				docker-compose down --volumes
				docker-compose push
				docker stack deploy --compose-file docker-compose.yaml passgen
				docker service update --replicas 5 passgen_service3
				docker service update --force passgen_service3
                                
                                '''
                        }
                }
        }
}
