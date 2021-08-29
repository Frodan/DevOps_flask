pipeline {
  agent none
  stages {
    stage('Docker Build') {
      agent any
      steps {
        dir('app_python'){
          sh 'docker build . --file Dockerfile --tag frodan/dev_ops'
        }
      }
    }
    stage('test') {
         agent {
              docker {
                   image 'qnib/pytest'
              }
         }
         steps {
              sh 'virtualenv venv && . venv/bin/activate && pip install -r app_python/requirements.txt && python app_python/test/test_main.py'
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