# LMS API Service

A RESTful API service for Learning Management System (LMS) built with DRF and PostgreSQL.

## Features

- User authentication (JWT)
- Course management
- Lesson management
- User management (automatic blocking of inactive users)
- Payment service
- Courses subscription feature (be aware of all updates of a course you're interested at)
- API documentation with Swagger

## Installation

1. Set up dependencies:
```commandline
sudo apt update
sudo apt upgrade
```
2. Set up Docker:
Чтобы установить Docker, воспользуйтесь инструкцией по установке с официального сайта: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
3. Firewall:
```commandline
sudo ufw status
sudo ufw enable
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
```
4. Clone the repository:
```commandline
git clone https://github.com/mikhailsorochinskiy/sky_drf.git
cd sky_drf/
```
5. Set your environment variables:
Fill in '.env.sample' file. Don't forget to rename the file to .env!

6. Start the container:
```commandline
docker-compose up
```
7. Congratulations! The project is set up successfully! To enjoy all the features go to http://localhost:8000/users/users/
and create a user account.

## Workflows
when committing commits and sending them to a remote repository, you need to set the host to localhost in .env

## API Documentation

After starting the container, access the API documentation at:

Swagger UI: http://localhost:8000/swagger/
Redoc UI: http://localhost:8000/redoc/