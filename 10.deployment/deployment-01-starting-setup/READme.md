EC2(Elastic Compute Cloud) Instance (full control and responsibilty of creator)
    EC2 is a service which allows us to create a machine remotely on cloud.
    Create the instance with key pair (ssh file required for connecting to machine remotely) 
    Launch the instance
    Follow the steps required for connecting to that instance from WSL(UBUNTU Terminal) / Putty
        Navigate to the folder where key-pair (ssh) file is stored
        Execute the commands given in aws console for connecting
            After Connection is established:- 
                sudo yum update -y --- update the remote machine packages to latest
                sudo amazon-linux-extras install docker --- amazon-linux-extras is command available to install extra apps on remote machine
                sudo service docker start --- starts docker on remote machine

Deploying to Remote Machine
1. Copy source code from Host to Remote
    Build an image on remote 
    Run the container based on that image on remote
2. Build the image on Host (Convenient ans Widely used)
    Push the image to Repository (Docker hub)
    Pull the image in Remote
    Run the container based on that pulled image on remote

By Default EC2 instance accepts traffic from SSH and 22 port
In order to accept requests from our container that exposes HTTP 80, we need to add a Security Group in EC2 instance that allows traffic from HTTP 80 requests.
After that we can access our app through Public DNS or Public IPv4 Address.