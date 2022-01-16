pipeline {

  agent any
  
  stages {
    
    stage("build") {
      steps {
        echo 'Building the application ...'
        echo 'Application built...'
        script {
            def message = 4 + 3 > 6 ? 'cool' : 'not cool'
            echo message
        }
      }
    }
      stage("test") {
        steps {
          echo 'Testing the application ...'
        }
      }

      stage("deploy") {
        steps {
          echo 'Deploying the application ...'
        }
      }

    }
}
