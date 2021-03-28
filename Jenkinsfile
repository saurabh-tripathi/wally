#!/usr/bin/env groovy

void dockerRun(image, command, extra='', returnStatus=false) {
  sh 'docker run --rm ' + "${extra} " + "${image} " + "sh -c '${command}'"
}

pipeline {
  agent any

  environment {
    BUILD_IMAGE = env.BUILD_TAG.toLowerCase().replaceAll(/[^a-z0-9]/, '-');
  }

  stages {
    stage('Prepare workspace') {
      steps {
        sh "rm -rf coverage && mkdir coverage"
      }
    }

    stage('Build image') {
      steps {
          sh "docker build -t ${env.BUILD_IMAGE} ."
        }
      }

    stage('Format check') {
      steps {
        dockerRun(env.BUILD_IMAGE, 'poetry run format')
      }
    }

    stage('Lint') {
      steps {
        dockerRun(env.BUILD_IMAGE, 'poetry run lint')
      }
    }

    stage('TypeCheck') {
      steps {
        dockerRun(env.BUILD_IMAGE, 'poetry run type_check')
      }
    }

    stage('PyDoc') {
      steps {
        dockerRun(env.BUILD_IMAGE, 'poetry run docs')
      }
    }

    stage('Unit test') {
      steps {
          dockerRun(env.BUILD_IMAGE, 'poetry run unit', '-v $(pwd)/coverage:/cerbo-feature-store/coverage')
          cobertura coberturaReportFile: 'coverage/coverage.xml'
        }
      }
  }
}
