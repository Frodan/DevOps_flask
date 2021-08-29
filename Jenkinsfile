pipeline {
  agent none
  stages {
   //stage("Tests") {
   //   agent any
   //   steps {
   //       sh 'python3 -m venv .'
   //       sh 'pip install -r app_python/requirements.txt'
   //       sh 'python -m unittest app_python/test/test_main.py'
   //   }
    //}
    stage('Docker Build') {
      agent any
      steps {
        dir('app_python'){
          sh 'sudo docker build . --file Dockerfile --tag frodan/dev_ops'
        }
      }
    }
    stage('Docker Push') {
      agent any
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "sudo docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'sudo docker push frodan/dev_ops:latest'
        }
      }
    }
  }
}