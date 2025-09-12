pipeline{
    agent any
    stages{
        stage("Build"){
            steps{
                echo "Build Docker Image"
                bat "docker build -t formapp ."
            }
        }
        stage("Run"){
            steps{
            echo "Running"
            bat "docker rm -f mycontainer || exit 0"
            bat "docker run -d -p 5000:5000 -name mycontainer formapp"
            }
        }
    }

post{
    success{
        echo "Pipeline completed successfully!"
    }
    failure{
        echo "Pipeline failed. please check the logs."
    }
}
}