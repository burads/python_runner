node("mini") {
  stage('checkout SCM') {  
    checkout scm
  }
  try{
    stage('build image'){
      def customImage = docker.build("python-runner:${env.BUILD_ID}")
      print customImage
    }
  } finally {
    stage('Cleanup'){
      sh "docker rmi ${customImage.id}"
    }
  }
}
