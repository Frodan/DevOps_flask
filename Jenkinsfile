pipeline {
  agent {
    docker {
      image 'python:3.8.2-alpine'
    }
  }
  environment {
    USER_LOGIN = 'test'
    USER_PASS = 'test'
  }
  stages {
    stage('Test') {
      steps {
        dir('app_python'){
          sh 'pip install -r requirements.txt'
          sh 'python test.py'
        }
      }
    }
    stage('Docker Build') {
      agent any
      steps {
        dir('app_python'){
          sh 'docker build . --file Dockerfile --tag frodan/dev_ops'
        }
      }
    }
    stage('Docker Push') {
      agent any
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push frodan/dev_ops:latest'
        }
      }
    }
  }
}