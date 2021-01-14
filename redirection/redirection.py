from flask import Flask, redirect
from flask_mysqldb import MySQL
import os

redirection = Flask(__name__)

redirection.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
redirection.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
redirection.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
redirection.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
redirection.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(redirection)

def get_url(tiny_url):
    tiny_id = tiny_url.split('/')[-1]
    cur = mysql.connection.cursor()
    query="select url from url where tiny_key={};".format(tiny_id)
    cur.execute(query)
    response = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return response['url']

@redirection.route('/s/<tinyid>')
def redirect_it(tinyid):
    full_url = get_url(tinyid)
    print(full_url)
    return redirect(full_url)

if __name__ == '__main__':
	redirection.run(host='0.0.0.0')