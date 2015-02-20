
"""

Configuration file for migrating SDBM. No account names or passwords should be stored in this file.

"""

import getpass
import os
import sys

import cx_Oracle
import MySQLdb

oracle_host = raw_input("Oracle hostname: ")
oracle_username = raw_input("Oracle username: ")
oracle_password = getpass.getpass("Oracle password: ")

oracle = cx_Oracle.connect(oracle_username, oracle_password, "(DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = %s)(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME = rsrcutf8)))" % (oracle_host,))

legacy_db_name = os.environ.get("SDBM_LEGACY_DB_NAME")
legacy_db_user = os.environ.get("SDBM_LEGACY_DB_USER")
legacy_db_password = os.environ.get("SDBM_LEGACY_DB_PASSWORD")
legacy_db_host = os.environ.get("SDBM_LEGACY_DB_HOST")

mysql = MySQLdb.connect(
    db=legacy_db_name,
    user=legacy_db_user,
    passwd=legacy_db_password,
    host=legacy_db_host,
    use_unicode=True,
    charset='utf8')

tables = (
    'MANUSCRIPT',
    'MANUSCRIPT_ARTIST',
    'MANUSCRIPT_AUTHOR',
    'MANUSCRIPT_CATALOG',
    'MANUSCRIPT_CATALOG_CHANGE_LOG',
    'MANUSCRIPT_CHANGE_LOG',
    'MANUSCRIPT_DROPBOX',
    'MANUSCRIPT_LANGUAGE',
    'MANUSCRIPT_PLACE',
    'MANUSCRIPT_PROVENANCE',
    'MANUSCRIPT_USER',
)
