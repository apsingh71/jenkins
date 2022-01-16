properties([
  parameters([choice(choices: ['Dev', 'QA', 'Stage', 'PreProd', 'Prod'], description: 'Drop Down to Select Environment to run test against', name: 'Environment'),
              choice(choices: ['eNB', 'Edge', 'CSO', 'Sanity', 'Regression'], description: 'Select test suite to run', name: 'TestSuite'),
              string(defaultValue: 'dev', description: 'Input automation branch to use (default: dev)', name: 'AutomationBranch', trim: true),
              booleanParam(defaultValue: false, description: 'Select to update testrails with test results', name: 'UpdateTestRails')])
          ])

pipeline {

  agent any
  
  stages {
    
    stage("build") {
      steps {
        echo 'Building the application ...'
        echo 'Application built...'
        echo "Automation Branch: ${params.AutomationBranch}"
        script {
            def message = 4 + 3 > 6 ? 'cool' : 'not cool'
            echo message
        }
      }
    }
      stage("test") {
        steps {
          echo 'Testing the application ...'
          echo "Test Suite: ${params.TestSuite}"
          echo "Pipeline Environment: ${params.Environment}"
        }
      }

      stage("deploy") {
        steps {
          echo 'Deploying the application ...'
          echo "Update Testrails: ${params.UpdateTestrails}"
        }
      }

    }
}
