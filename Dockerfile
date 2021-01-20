# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /

# copy the dependencies file to the working directory
# No additional requirement

# install dependencies
# RUN pip install -r requirements.txt
# No pip install

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python", "./main.py" ]