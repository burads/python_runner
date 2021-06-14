node("mini") {
  stage('Print Env') {  
    sh 'printenv'
  }
  stage('checkout SCM') {  
    checkout scm
  }
  stage('build image'){
    def customImage = docker.build("python-runner:${env.BUILD_ID}")
  }
}
