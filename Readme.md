```
mkdir eb-flask
cd eb-flask
python3 -m venv eb_venv
source eb_ven/bin/activate
pip install -r requirements.txt

```

####1- Initialize your Elastic Beanstalk repository

`eb init -p python-3.7 <application name>  --region eu-west-1`

or 

`eb init`  

This last command will walk the user through the options to set and it will enable the possibility to set a key pair to access to the EC2 instance with ssh

######Note: the eb init step will automatically create the needed config file: `.elasticbeanstalk/config.yml` at the root of the project

####2- Create an environment and deploy the application
`eb create <environment name>`


####3- Open the web application
`eb open`

####4- Create another environment
`eb create <another environment name>`


####5- Deploy a new version into one of the environments 
`eb deploy <enviroment name>`
