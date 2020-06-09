# ----- CONFIGURE YOUR EDITOR TO USE 4 SPACES PER TAB ----- #
import settings
import sys,os
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
        textOfReview=results # pira to text tis Review
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
    # Apo sql exo parei negterm, posterm , textOfReview

    textOfReview=str(textOfReview[0][0])

    print("\n to text tou review")
    print(textOfReview)
    print("\n\n\n")

    ngrammata=extract_ngrams(list(textOfReview.split()),3)

    print("\n ngrammata")
    print(ngrammata)
    print("\n\n\n")

    listOfPosTerm = [a[0] for a in posterm]

    print("\nlist of posterm")
    print(listOfPosTerm)
    print("\n\n\n")
    kalaSxolia= []
    for i in range(3,0,-1):
        ngrammata=extract_ngrams(list(textOfReview.split()),i)
        kalaSxolia.append(list(set(ngrammata).intersection(listOfPosTerm)))
    print("\nKalaSxolia")
    print(kalaSxolia)
    print("\n\n\n")
    # sostaKalaSxolia = kalaSxolia
    # for sublista in reversed(kalaSxolia):
    #     for itema in sublista:
    #         for substring in itema.split():
    #             for substring1 in itema.split():
    #                 if substring==substring1:
    #                     for each in kalaSxolia:
    #                         for eachItem in each:
    #                             if substring==eachItem:
    #                                 kalaSxolia.each.remove(eachItem)


  


    print("\n Kala Sxolia")
    print(kalaSxolia)
    print("\n\n\n")

    return textOfReview


def extract_ngrams(wordlist, n):   
    ngrams = []
    sostiLista= []    
    for i in range(len(wordlist)-(n-1)):
        ngrams.append(wordlist[i:i+n])

    for sublist in ngrams:
        sumOfStrings=" ".join(sublist)
        sostiLista.append(sumOfStrings)
    return sostiLista



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

