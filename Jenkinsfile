node
{
        stage('Build') {
	    checkout scm
        }
	stage('list source') {
	    sh "ls -lrt"
        }
        stage('Deploy') {
            sh "rsync -av ./* /opt/getRS9HardwareID/"
        }
	stage('Run filter'){
	    sh "cd /opt/getRS9HardwareID/"
            sh "grep -e '<Name.*[0-9][0-9][0-9][0-9].*</Name><Type dt:dt=\"ui4\">1</Type>' -e 'TD.*THV' -e 'TD.*THU' /opt/serialNumber/2x-gorehill.dat>THVU9.txt"
	}
        stage('Run batch get'){
            sh "/opt/getRS9HardwareID/HardwareIDreader.py &>/opt/getRS9HardwareID/RS9_THVU_DTV_SN.csv"
            sh "cp /opt/getRS9HardwareID/RS9_THVU_DTV_SN.csv /opt/serialNumber/"
	}
}

