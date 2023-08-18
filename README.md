# CD_Assignment
In this Assignment I made a continuous deployment pipeline. I made a simple Flask Application and every time I push an adjustment to github, github actions runs pyetst test to test the text of the flask app. When the tests are succesfull it will login to my VPS on Digital Ocean via shh and update the code there so it is up to date with the repository. 

## Three components from my CD Assignment:
- Digital Ocean: Is a server hosting company that hosts the VPS (Droplet),Virtual Private Sever, where this project runs on.
  
- SSH: Is the method used to log into my VPS for this project. A ssh key is a password and username in one. You get a private ssh key and a public ssh key.
  the public ssh key is located in your authorized keys on your VPS and you need to use the private key to log in. For this project the private key is stored in 
  github secrets
 
- Github Actions: Is a feature of Github that helps to automate tasks, in this case test and deploy. For this you write workflows in yml file. In this case a   main.yml. This workflow makes sure to test the text of my Flask application every time a push adjustment of my code to github. When these tests are succesful it logs into my VPS on Digital Ocean and updates the code there. For this I used appleboy/shh@master, a tool to execute ssh commands remote. It logs into my Vps via the ssh key in github secrets and updates the code by doing a pull request and restart the system, so the adjustments get visible in your browser.  
 
  
## Three problems that I encountered :
 - Error by login ssh key: At first when I ran my workflow I got the error  "ssh: handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain", when it tried to login to the VPS. I did some small adjustments in my yml file. When this did not work, I made a new ssh keypair, with which I was able to login to my VPS via my terminal. Eventually I discovered I used the wrong username (my VPS hostname). After this adjustment my workflow ran succesfull.
 
 - Systemcln restart error: After my workflow ran succefull a couple of times, I suddenly got a error "Job failed because the control process exited with error code." Wanneer ik de command " when it got to the " systemctl restart CD_Assignment " command. When I entered this command manually in my terminal, I got the same error. So I used the command "systemctl stop CD_Assignment" to stop the proces and I ran trough the steps of the exercise Deployment again. But I got the rror again at "systemctl enable --now CD_Assignment ". Eventually I removed the project from the VPS and cloned it again with git clone. After this the workflow workt again. 
    
  - Running .sh file: In the assignment description it was recommommanded to chain bash commands in a .sh file. The writing of the .sh file was easy but running the file in my workflow was not. I watched youtube and tried it with the "script: sh ./pull.sh", but it did not work. Eventually I was succefull with
        "script: |
                 cd /home/CD_Assignment
                 bash pull.sh"
    I know this is not the best solution beacause I still need to write multiple commands in the yml itself. Eventually I discovered that I needed to adjust the path of the sh file like " script: sh /home/CD_Assignment/pull.sh" 
 
    
