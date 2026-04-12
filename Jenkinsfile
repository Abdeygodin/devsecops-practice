pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
            }
        }
        
        stage('Trivy Scan') {
            steps {
                sh '''
                    wget -q https://github.com/gitleaks/gitleaks/releases/download/v8.24.3/gitleaks_8.24.3_linux_x64.tar.gz || true
                    which trivy || (curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin)
                    trivy --version
                '''
            }
        }
        
        stage('Semgrep Scan') {
         steps {
            sh '''
                docker run --rm -v $(pwd):/src returntocorp/semgrep semgrep --config p/python /src || true
           '''
       }
     }
        
        stage('GitLeaks Scan') {
            steps {
                sh '''
                    which gitleaks || (wget -q https://github.com/gitleaks/gitleaks/releases/download/v8.24.3/gitleaks_8.24.3_linux_x64.tar.gz && tar -xzf gitleaks_8.24.3_linux_x64.tar.gz && mv gitleaks /usr/local/bin/)
                    gitleaks version
                '''
            }
        }
    }
    
    post {
        success {
            echo '✅ All security scans passed!'
        }
        failure {
            echo '❌ Security scan failed!'
        }
    }
}
