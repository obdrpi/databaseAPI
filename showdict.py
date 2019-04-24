from flask_table import Table, Col, LinkCol
 
class Results(Table):
    print "Hello"
    userid = Col('ID')
    password = Col('Pass')
    email = Col('Email')
