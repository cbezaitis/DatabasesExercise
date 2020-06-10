# ----- CONFIGURE YOUR EDITOR TO USE 4 SPACES PER TAB ----- #
import settings
import sys,os
import pymysql as db
import copy 

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
        textOfReview=results
        # pira to text tis Review
        # if results ==():
        #     return [("This Review Id is wrong",)]
    except :
        print("error")
        

    sql= """
            SELECT b.name
            FROM reviews r,business b
            WHERE r.review_id='""" +stringReview + "'AND b.business_id=r.business_id;"

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        biznaName=results # pira to text tis Review
    except :
        print("error2")

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

    reReview=textOfReview 
    textOfReview=str(textOfReview[0][0])

    print("\n to text tou review")
    print(textOfReview)
    print("\n\n\n")




    kalaSxolia= []
    listOfPosTerm = [a[0] for a in posterm]
    for i in range(3,0,-1):  
        ngrammata=extract_ngrams(textOfReview,i)
        kalaSxolia.append(list(set(ngrammata).intersection(listOfPosTerm)))
    

    kakaSxolia= []
    listOfNegTerm = [a[0] for a in negterm]
    print("\nKalaSxolia")
    print(listOfNegTerm)
    print("\n\n\n")
    for i in range(3,0,-1):  
        ngrammata=extract_ngrams(textOfReview,i)
        kakaSxolia.append(list(set(ngrammata).intersection(listOfNegTerm)))

    print("\nKalaSxolia")
    print(kalaSxolia)
    print("\n\n\n")

    print("\nKaKaSxolia")
    print(kakaSxolia)
    print("\n\n\n")

    kainouriaKalaSxolia= []
    for sublist in kalaSxolia:
        for item in sublist:
            for item1 in item.split():
                kainouriaKalaSxolia.append(item1)

    kainouriaKalaSxolia = list(set(kainouriaKalaSxolia))
    print("\nkainouriaKalaSxolia")
    print(kainouriaKalaSxolia)
    print("\n\n\n")

    kainouriaKakaSxolia= []
    for sublist in kakaSxolia:
        for item in sublist:
            for item1 in item.split():
                kainouriaKakaSxolia.append(item1)

    kainouriaKakaSxolia = list(set(kainouriaKakaSxolia))
    print("\nkainouriaKakaSxolia")
    print(kainouriaKakaSxolia)
    print("\n\n\n")

    METRITIS=len(kainouriaKalaSxolia)-len(kainouriaKakaSxolia)
    print("\n")
    print(METRITIS)
    print("\n\n\n")
    if METRITIS>0:
        result="kalo sxolio"
    else:
        result="kako sxolio"
    
    return [("Business Name","Text of Review","Kalo / kako sxolio"),(str(biznaName[0][0]),str(reReview[0][0]),str(result))] 

def extract_ngrams(text, num): 
    ngrams = [] 
    if num==3:
        m=-1
    elif num==2:
        m=0
    else:
        m=1  
    void = text.count(' ') 
    for i in range(void + m): 
        ngrams.append(' '.join(text.split()[i:i+num])) 
    return ngrams 


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

