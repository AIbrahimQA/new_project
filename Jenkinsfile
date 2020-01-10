pipeline{
        agent any
        
        stages{


                stage('--initialise--'){
                        steps{
                                sh '''ssh 35.246.0.219  << BOB
				source ~/.bashrc
				cd new_project/
				docker-compose build
                                docker-compose push
				
				'''

                        }
                }


                            
                stage('--deploy--'){
                        steps{
                                sh '''ssh 35.246.0.219  << BOB      		
				git clone https://github.com/AIbrahimQA/new_project.git
			        cd new_project/
				git pull
				docker stack deploy --compose-file docker-compose.yaml passgen
                                
                                '''
                        }
                }
        }
}
