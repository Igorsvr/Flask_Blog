import os

#class Config:
#SECRET_KEY = os.environ.get('SECRET_KEY')
#    MAIL_SERVER = 'smtp.googlemail.com'
#    MAIL_PORT = 587
#    MAIL_USE_TLS = True
#    MAIL_USERNAME = os.environ.get('buldozerom@gmail.com')
#    MAIL_PASSWORD = os.environ.get('Igorogisko')

#db_user = os.environ.get("DB_USER")
#db_password = os.environ.get("DB_PASS")
#print(db_user)
#print(db_password)

#export MAIL_SERVER=smtp.googlemail.com
#export MAIL_PORT=587
#export MAIL_USE_TLS=1
#export MAIL_USERNAME=<your-gmail-username>
#export MAIL_PASSWORD=<your-gmail-password>
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLCLCHEMY_RECORD_QUERIES = True
    CSRF_ENABLED = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'buldozerom@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'Igorogisko')
    MAIL_SENDER = os.environ.get('MAIL_SENDER', 'Project Admin<buldozerom@gmail.com>')
    PROJECT_ADMIN = os.environ.get('PROJECT_ADMIN', 'PROJECT_ADMIN')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))  #'465'
    MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS', False))
    MAIL_USE_SSL = int(os.environ.get('MAIL_USE_SSL', True))
    MAIL_SUBJECT_PREFIX = '[PROJECT]'
