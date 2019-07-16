pipeline {
    agent none
    stages {
        stage("Build") {
            agent {
                docker {
                    image 'ifergu/python-barcode:firsttry'
                }
            }
            steps {
                sh 'python -m py_compile download.py upload.py helpers.py main.py'
            }
        }
        stage("Download Data") {
            agent {
                docker {
                    image 'ifergu/python-barcode:firsttry'
                }
            }
            steps {
                sh 'python download.py'
            }
        }
        stage('Initiate Tester') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            stages {
                stage('Testing') {
                    parallel {
                        stage('Download Test') {
                            steps {
                                sh 'py.test --verbose --junit-xml test-reports/results_download.xml test_data_downloaded.py'
                            }
                            post {
                                always {
                                    junit 'test-reports/results_download.xml'
                                }
                            }
                        }
                        stage('Functions Test') {
                            steps {
                                sh 'py.test --verbose --junit-xml test-reports/results.xml test_functions.py'
                            }
                            post {
                                always {
                                    junit 'test-reports/results.xml'
                                }
                            }
                        }
                    }
                }
            }
        }
        stage('Upload Results') {
            agent {
                docker {
                    image 'ifergu/python-barcode:firsttry'
                }
            }
            steps {
                sh 'python helpers.py'
                sh 'python upload.py'
            }
        }
    }
}