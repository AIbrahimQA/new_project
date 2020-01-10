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
				docker-compose up -d --build
                                
                                '''
                        }
                }
        }
}
