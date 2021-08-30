pipeline {
    agent {
        docker {
            image 'python:3.8.2-alpine'
        }
    }
    stages {
        stage('Test') {
            steps {
              dir('app_python'){
                sh 'pip install -r requirements.txt'
                sh 'export USER_LOGIN=test'
                sh 'export USER_PASS=test'
                sh 'python test.py'
              }
            }
        }
    }
}
// fuck jenkins
// pipeline {
//   agent none
//   stages {
//     stage('Docker Build') {
//       agent any
//       steps {
//         dir('app_python'){
//           sh 'docker build . --file Dockerfile --tag frodan/dev_ops'
//         }
//       }
//     }
//     stage("Tests") {
//       agent any
//       steps {
//         echo "OK";
//       }
//     }
//     stage('Docker Push') {
//       agent any
//       steps {
//         withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
//           sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
//           sh 'docker push frodan/dev_ops:latest'
//         }
//       }
//     }
//   }
// }