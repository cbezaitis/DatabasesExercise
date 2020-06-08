# ----- CONFIGURE YOUR EDITOR TO USE 4 SPACES PER TAB ----- #
import settings
import sys,os
sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'lib'))
import pymysql as db

def connection():
    ''' User this function to create your connections '''
    con = db.connect(
        settings.mysql_host, 
        settings.mysql_user, 
        settings.mysql_passwd, 
        settings.mysql_schema)
    
    return con

def classify_review(reviewid):
    
    # Create a new connection
    # Create a new connection
    con=connection()
    # Create a cursor on the connection
    cur=con.cursor()
    stringReview=str(reviewid) # kano to reviewid na eimai sigouros
    sql= """
            SELECT r.text
            FROM reviews r
            WHERE r.review_id='""" +stringReview + "';"

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        text=results
    except :
        print("error")

    sql= """
            SELECT *
            FROM posterms ;
         """

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        posterm=results # pira ta posterms logika einai tupple?
    except :
        print("error")

    sql= """
            SELECT *
            FROM negterms ;
         """

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        negterm=results # pira ta negterms logika einai tupple?
    except :
        print("error")

    print(posterm)
    print(results)
    return negterm


def updatezipcode(business_id,zipcode):
    
   # Create a new connection
    
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    
 
    return [("result",),]

def selectTopNbusinesses(category_id,n):

    # Create a new connection
    
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    
    return [("business_id", "numberOfreviews"),]

def traceUserInfuence(userId,depth):
    # Create a new connection
    con=connection()

    # Create a cursor on the connection
    cur=con.cursor()

    return [("user_id",),]

