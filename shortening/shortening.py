from flask import Flask, render_template, url_for, request
from flask_mysqldb import MySQL
import os, hashlib

tiny_baseurl = 'http://localhost/s'

shortening = Flask(__name__)

shortening.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
shortening.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
shortening.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
shortening.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
shortening.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(shortening)

def generate_tiny(destination_url):
    tiny_key = int(hashlib.sha224(destination_url.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
    return tiny_key

def put_url(destination_url):
    tiny_id = generate_tiny(destination_url)
    cur = mysql.connection.cursor()

    ## Check if already exist
    query="select distinct tiny_key from url;"
    
    cur.execute(query)
    response = cur.fetchall()
    mysql.connection.commit()
    existing_keys = list(i['tiny_key'] for i in response)
    print(existing_keys)

    ## Insert if do not exist
    if str(tiny_id) not in existing_keys:
    	query="insert into url(tiny_key,url)values('{}','{}');".format(tiny_id, destination_url)
    	cur.execute(query)
    	mysql.connection.commit()
    cur.close()

    tiny_url = '{}/{}'.format(tiny_baseurl, tiny_id)
    return tiny_url

@shortening.route('/')
def main():
    return render_template('index.html')

@shortening.route('/result', methods=['GET', 'POST'])
def result():
    url = request.form["url"]
    
    tiny_url = put_url(str(url))
    return render_template('result.html', tiny_url=tiny_url)


if __name__ == '__main__':
	shortening.run(host='0.0.0.0')