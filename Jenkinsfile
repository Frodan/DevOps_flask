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
    stage("Tests") {
          agent any
          steps {
              sh 'python -m pip install -r app_python/requirements.txt'
       //       sh 'python -m unittest app_python/test/test_main.py'
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