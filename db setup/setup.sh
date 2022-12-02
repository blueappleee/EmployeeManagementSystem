#! /bin/sh
export MYSQLPASS="cs4471pass"
export EMPMANAGEMENTPASS="cs4471pass"
sudo apt-get -q -y upgrade
sudo apt -q -y install wget
sudo apt -q -y install nano
sudo apt -q -y install git
sudo apt -q -y install python3
sudo apt -q -y install python3-pip
pip3 install -q mysql-connector-python
pip3 install -q pyfiglet
pip3 install -q tabulate
sudo apt -q -y install mysql-server
sudo systemctl stop mysql.service
sudo systemctl set-environment MYSQLOPTS="--skip-networking --skip-grant-tables"
sudo systemctl start mysql.service
echo ${MYSQLPASS}
sudo mysql -u root <<EOF   
FLUSH PRIVILEGES;
USE mysql;                                                 
ALTER USER 'root'@'localhost' IDENTIFIED BY '${MYSQLPASS}';
exit
EOF
sudo systemctl unset-environment MYSQLOPTS
sudo systemctl revert mysql
sudo killall -u mysql
sudo systemctl restart mysql.service
sudo mysql_secure_installation -p${MYSQLPASS} -D
sed -i "/CREATE USER if not exists 'empManagement'@'localhost' IDENTIFIED BY 'tmppass'/c\CREATE USER if not exists 'empManagement'@'localhost' IDENTIFIED BY '${EMPMANAGEMENTPASS}'" setupScript.sql
sudo mysql -nvvf --verbose -p${MYSQLPASS} < setupScript.sql > setupOutput.txt 2>&1
sudo mysql -nvvf --verbose -p${MYSQLPASS} < dummyValues.sql > dummyOutput.txt 2>&1


mkdir /home/vboxuser/cs4471program
mkdir /home/vboxuser/cs4471program/EMS
git clone "https://github.com/blueappleee/EmployeeManagementSystem" /home/vboxuser/cs4471program/EMS
sudo chown -R vboxuser /home/vboxuser/cs4471program/
# this sed can be used if the empManagementPass changes from cs4471 to replace the connector pass in the file
#sed -i "/connection = mysql.connector.connect(host='localhost',database='empManagementdb',user='empManagement',password='cs4471pass')/c\connection = mysql.connector.connect(host='localhost',database='empManagementdb',user='empManagement',password='${EMPMANAGEMENTPASS}')" ~/cs4471program/EmployeeManagementSystem/src/login_cmdUI/db/dbConnection.py

