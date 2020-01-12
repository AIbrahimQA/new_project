pipeline{
        agent any
        
        stages{


                stage('--initialise--'){
                        steps{
                                sh ''' 
				. ~/.bashrc
		
				docker-compose build
                                docker-compose push
				
				'''

                        }
                }


                            
                stage('--deploy--'){
                        steps{
                                sh ''' ssh 35.246.107.87  << BOB      		
				export BUILD_NUMBER='${BUILD_NUMBER}'
                                git clone https://github.com/AIbrahimQA/new_project.git
			        cd new_project/
				git pull
				docker service update --replicas 4 passgen_service3
				docker service update --image project2-jenkins:5000/service3
:build-${BUILD_NUMBER} passgen_service3 
                                '''
                        }
                }
        }
}
