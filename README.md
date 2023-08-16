# CD_Assignment
Assignment CD Winc Back-end Development course

 3 Problems I encountered:
 -Login ssh key: 
  The first problem I encountered was this error "ssh: handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain"
  that I got everytime I tried to deploy my project. It took quite some time too solve this. I tried to solve it by making new ssh keypair and rewriting the yml file 
  over and over again with little adjustments. I also renewed my github secrets multiple times. Eventually I discouvered that I used the wrong username. I thought 
  that my username was the hostname of my VPS, but after some online research I found the wright one to use. After this discouvery it workt. But I think that the 
  changes I made before also somehow contributed.

  - systemcln restart error:
  - running .sh file: hi
    
