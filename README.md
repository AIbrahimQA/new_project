# Second Project
https://docs.google.com/presentation/d/1F9Cj21d4B0wxGYmhfD27b4M9m87nle87fw-SpfpZsS0/edit#slide=id.g6c29b958af_0_83

Solo Project 2 : Random password generator

The contents:

Solo Project 2
Requirements
Application Use
Planning
Configuration
CI Pipeline
Summary
Requirements:

Trello Board
Functional Python application with testing
Front-end website using Flask
Configuration Management: Ansible
Integration with Version Control System
Containerisation: Docker
Deployed by CI Server
Documentation

CI Pipeline -Jenkins – Rolling Update

Github commit
1.	Webhook triggered
2.	Jenkins starts pipeline
3.	Build and push on Jenkins machine
4.	SSH to swarm machine
5.	Cd to project location
6.	Git pull
7.	Docker Service update image


Technologies Used:

Trello
Google Console Platform
Python
Flask
Version Control – Git
CI Server – Jenkins
Ansible
Docker
Docker Swarm
Docker Stack



 
Risk Assessment

Poor Planning:
With poor planning there may be a low likelihood of it occurring but if it happened then the impact would be very high the project. Having poor planning would be a major danger to the project. So to combat this I used trello to make sure all requirements are down and all major goals are planned out.

IP Address:
If a static ip address is not used then there is the risk of the CI pipeline not working. If this was to occur then the impact of this would be huge as the app would not be able to work correctly. So to combat this assigning static ip address to the virtual machines would eliminate the risk of ip address changing.

Ansible Playbook:
There is a risk that the inventory files are outdated so the impact can be massive resulting in the playbooks not connecting to the desired machine. So having the name of the machine could be a better option as the name will resolve to the ip address when needed.

GCP issues:

Having a problem with the GCP instances would have a major impact on my project however it has a low likelihood of happening. To make sure the likelihood is low i will keep the number of instances down so there is no conflict or confusion between any virtual machine


Presentation:
With the presentation there is a low likelihood as well as a medium impact on the project. If the presentation was to have problems this shouldnt impact the project greatly if there is sufficient documentation to support the web application.


Automates Test:

As having automated tests is an important feature of the project. It would have an impact on the project if there was no automated test. However if there is a problem with the automation there is always the manual unit testing to fall back on which does the same job just not automated.


Version Control:

Having a version control system in place is essential to having a successful project. Working on different features and pushing the complete code up using git gives the project a high chance of succeeding. It's better than uploading all work at the last minute which could have massive bugs.


Documentation:

Documentation is very important so not having sufficient documentation would have a high impact on the project. If there is no evidence of the work you did then the credibility of the work is not great.



Summary

Positives

CI Pipeline
Ansible Playbook
Docker Stack Deploy
Rolling Update

Improvements

Add more tests
Add testing to CI Pipeline
Update all images for rolling update.


