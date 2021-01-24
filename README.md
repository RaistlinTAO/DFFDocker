# Dummy Python Function for Docker Testing
 
## Python Function Requirement
> 1. Function should return or send result back to database/MQ immediately after internal process is complete in order to save cloud resources. 
>
> 2. Do not use Web framework like Flask, Django, web2py, Bottle or Tornado to handle API request, create function as entry point directly instead.

## Docker Requirement
> 1. Must not contains volume

## Auto Deployment Pipeline
> For Amazon ECR Document:
> 
> https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-ecs-ecr-codedeploy.html

> For Docker Hub Document:
> 
> https://docs.docker.com/docker-hub/builds/

## Implementation Steps
1. Create Python or Node APP
2. Dockerisation
3. Upload to ECR or Docker HUB
4. (optional) set up auto deployment pipeline
5. Create Fargate ECS
6. Task Definition (Link the docker image)
7. Profit



