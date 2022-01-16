properties([
  parameters([choice(choices: ['Dev', 'QA', 'Stage', 'PreProd', 'Prod'], description: 'Drop Down to Select Environment to run test against', name: 'Environment'),
              choice(choices: ['eNB', 'Edge', 'CSO', 'Sanity', 'Regression'], description: 'Select test suite to run', name: 'TestSuite'),
              string(defaultValue: 'dev', description: 'Input automation branch to use (default: dev)', name: 'Automation Branch', trim: true),
              booleanParam(description: 'Select to update testrails with test results', name: 'Update TestRails')])
          ])

pipeline {

  agent any
  
  stages {
    
    stage("build") {
      steps {
        echo 'Building the application ...'
        echo 'Application built...'
        echo '${Automation Branch}'
        script {
            def message = 4 + 3 > 6 ? 'cool' : 'not cool'
            echo message
        }
      }
    }
      stage("test") {
        steps {
          echo 'Testing the application ...'
          echo '${TestSuite'
          echo '${Environment}'
        }
      }

      stage("deploy") {
        steps {
          echo 'Deploying the application ...'
          echo '${Update Testrails}'
        }
      }

    }
}
