# oracle2mysql

Simple script to convert tables from Oracle to MySQL. This was created for the Schoenberg Database of Manuscripts project.

## Installation

You will need to install the following python packages:

```
MySQLdb 
cx_Oracle
```

Note that finding the right
[cx_Oracle](http://cx-oracle.sourceforge.net) package to use with your
Oracle installation can be tricky. The SDBM dev environment, running
on CentOS 5 and Python 2.6, uses cx_Oracle-5.1.2-10g-py26-1.x86_64.rpm.

Edit the oracle2mysql_conf.py and specify the hostnames, accounts, and
passwords for your two databases.

## Running the script

```
python oracle2mysql.py oracle2mysql_conf
```

For help, run the script without any arguments.

