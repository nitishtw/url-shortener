## URL Shortener by Nitish Tiwari
* URL Shortener consiste of two sevices:

#### Shortening Service
- Takes a long URL as input and generates a random short URL for it
- Store the mapping between shortened URL and long URL in the datastore.

![alt text](https://github.com/AdvikEshan/url-shortener/blob/main/shortening-service.png?raw=true)

#### Redirection Service
- When a generated short URL is visited, redirect the user to the corresponding long URL stored
- Retrieve the mapping from the datastore

![alt text](https://github.com/AdvikEshan/url-shortener/blob/main/redirection-service.png?raw=true)
----
### Directory Structure
1. **db**:  This directory contains init script to create table inside database.
2. **shortening**: This directory contains the Dockerfile, requirements.txt and script to run the shortening app.
3. **redirection**: This directory contains the Dockerfile, requirements.txt and script to run the redirection app.
4. **web**: This directory contains the configuration file for nginx to proxy pass between two app containers.
5. ***config.env***: This is the env file for docker-compose to pass the environment variables.
6. ***docker-compose.yml***: The compose file to automate the local deployemnt using containers.
 
## Setup :anchor:
### Requirements :heavy_check_mark:
* Docker Compose

**Setup Command**: ``` docker-compose up -d```

Once the compose is up, URL Shortening service can be accessed at ```http://localhost``` :smile:

***Note***: _This compose file uses port 80 for web server. Make sure it's not bind to any other service._

### Pending :heavy_exclamation_mark:
* Automate the deployment on cloud through Terraform/Ansible.

### Improvements :raised_hands:
* Use minimal docker base images such as Alpine to reduce the setup time.
* Regex expression for URL validitaion.
* MySQL Data dir to persist the data.
