#! /bin/sh
export MYSQLPASS="cs4471test"
export EMPMANAGEMENTPASS="notpassword"
sudo apt-get -q -y upgrade
sudo apt -q -y install wget
sudo apt -q -y install nano
sudo apt -q -y install git
sudo apt -q -y install python3
sudo apt -q -y install python3-pip
pip3 install -q mysql-connector-python
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
sed -i "/CREATE USER if not exists 'empManagement'@'localhost' IDENTIFIED BY 'tmppass'/c\CREATE USER if not exists 'empManagement'@'localhost' IDENTIFIED BY '${EMPMANAGEMENTPASS}'" test.sql
sudo mysql -nvvf --verbose -p${MYSQLPASS} < setupScript.sql > setupOutput.txt 2>&1

# this sed line will need to repalce var = and something.py so it enters the set password into the python code
#sed -i "/var = mysql.connector.connect(host='localhost',user='test',password='password')/c\var = mysql.connector.connect(host='localhost',user='test',password='${EMPMANAGEMENTPASS')" something.py

