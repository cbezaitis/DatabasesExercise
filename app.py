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
    con=connection()
    # Create a cursor on the connection
    cur=con.cursor()
    string_of_review=str(reviewid) # kano string to reviewid na eimai sigouros
    
    sql= """
            SELECT r.text
            FROM reviews r
            WHERE r.review_id='""" +string_of_review + "';"

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        text_of_review=results
        if results ==():
            return [("This Review ID is wrong",)]
    except :
        print("error")
        

    sql= """
            SELECT b.name
            FROM reviews r,business b
            WHERE r.review_id='""" +string_of_review + "'AND b.business_id=r.business_id;"

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        business_name=results # pira to onoma tis epixeirisis
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
    # Apo sql exo parei negterm, posterm , text_of_review

    re_review=text_of_review 
    text_of_review=str(text_of_review[0][0])

    print("\n to text tou review")
    print(text_of_review)
    print("\n\n\n")




    positive= []
    list_of_posterm = [a[0] for a in posterm]
    for i in range(3,0,-1):  
        ngrammata=extract_ngrams(text_of_review,i)
        print("\n to text tou review")
        print(ngrammata)
        print("\n\n\n")
        positive.append(list(set(ngrammata).intersection(list_of_posterm)))
    

    negative= []
    list_of_negterm = [b[0] for b in negterm]
    print("\nKalaSxolia")
    print(list_of_negterm)
    print("\n\n\n")
    
    for i in range(3,0,-1):  
        ngrammata=extract_ngrams(text_of_review,i)
        negative.append(list(set(ngrammata).intersection(list_of_negterm)))

    print("\nKalaSxolia")
    print(positive)
    print("\n\n\n")

    print("\nKaKaSxolia")
    print(negative)
    print("\n\n\n")

    positive_clean= []
    for sublist in positive:
        for item in sublist:
            for item1 in item.split():
                positive_clean.append(item1)

    positive_clean = list(set(positive_clean))
    print("\nkainouriaKalaSxolia")
    print(positive_clean)
    print("\n\n\n")

    negative_clean= []
    for sublist in negative:
        for item in sublist:
            for item1 in item.split():
                negative_clean.append(item1)

    negative_clean = list(set(negative_clean))
    print("\nkainouriaKakaSxolia")
    print(negative_clean)
    print("\n\n\n")

    review_counter=len(positive_clean)-len(negative_clean)
    print("\n")
    print(review_counter)
    print("\n\n\n")
    if (review_counter > 0):
        result="This is good!"
    else:
        result="This is bad!"
    
    return [("Business Name","Text of Review","Positive / Negative"),(str(business_name[0][0]),str(re_review[0][0]),str(result))] 

def extract_ngrams(text, num): 
    ngrams = [] 
    void = text.count(' ') 
    if num==3:
        m=-1
    elif num==2:
        m=0
    else:
        m=1  
    for i in range(void + m): 
        ngrams.append(' '.join(text.split()[i:i+num])) 
    return ngrams 


def updatezipcode(business_id,zipcode):
    
   # Create a new connection
    
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    sql = "SELECT EXISTS " +"("+ " SELECT "+"*"+" FROM business b WHERE business_id='"+str(business_id)+"');"
    try : 
        cur.execute(sql)
        results=cur.fetchall()
        print("To result tou prwtou SQL")
        print(results)
        if(results[0][0]==0):
            return [("there is no such business",),]
    except :
        print("error")

    sql = "UPDATE  yelp.business SET zip_code = "+zipcode+" WHERE business_id='"+business_id+"';"
    print("to zip code : =%s",zipcode)
    print("\n\nedo einai to business_id %s\n",business_id)
    val = (zipcode, business_id)

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        print(results)
        print(cur.rowcount,"posa rows xalasa")
        negterm=results # pira ta negterms logika einai tupple?
    except :
        print("error")
    
    con.commit()
    if(cur.rowcount==0):
        result="The zipcode is the same"
    elif(cur.rowcount==1):
        result="OK"
    else :
        result="Sovaro Provlima"
    # Ean yparxei i epixeirisi alla den allaxei to zipcode giati einai idio me to proigoumeno
    #den allazei to rowcount kai ara vgazei error. Mporoume na to allaxoume me mia select exists  akoma 
    return [(result,),]

def selectTopNbusinesses(category_id,n):

    # Create a new connection
    
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    
    string_of_category=str(category_id)


    sql= """
            SELECT DISTINCT b.business_id, COUNT(rpn.positive)
            FROM  business b, reviews_pos_neg rpn, reviews r, business_category bc , category c
            WHERE r.business_id = b.business_id AND r.review_id = rpn.review_id AND bc.business_id=b.business_id AND bc.category_id=c.category_id AND rpn.positive = TRUE
                                                AND c.category_id= """ +string_of_category + """ 
            GROUP BY b.business_id
            ORDER BY COUNT(rpn.positive) desc;
         """

    try : 
        cur.execute(sql)
        results=cur.fetchall() # orea tha itane na douleue h fetchmany
        best_of_all=results 
    except :
        print("error")
        return["PROBLEM"]
    

    best_of_N= list()
    kati=("Business ID","Number of Positive Reviews")
    best_of_N.append(kati)  # Vazo tin kefali tou table pou tha paei stin othoni
    for i in range(int(n)):
        kati=(best_of_all[i][0],str(best_of_all[i][1]))
        best_of_N.append(kati) # simplirono to upoloipo table

    print(best_of_N)    # dokimastiki ektiposi sto terminal 1

    best_of_N=tuple(best_of_N)  # metatropi tis listas se tupple 
                                 # gia ektiposi sto site
    
    print("\n\n\n")            
    print(best_of_N) # domikastiki ektiposi sto terminal 2
    # return [best_of_N]
    return best_of_N

def traceUserInfuence(userId,depth):
    depth=int(depth)
    # Create a new connection
    con=connection()

    # Create a cursor on the connection
    cur=con.cursor()

    print(sql_different_business(cur,userId))
    print("\n\n\n")

    friends_business=sql_different_business(cur,userId)

    list_of_lists=[]
    for i in range(depth):
        list_of_lists.append([])

    print("\n\n\n")
    print(friends_business)
    # Vazoume se mia lista apo listes tous vathos 1 epireasmenous filous kai tis epixeiriseis 
    list_of_lists[0].extend([list(sql_different_business(cur,userId))])

    print("\nfilos id 0 : \n")
    print(list_of_lists[0][0][0][0])
    print("\n\n\n")
    
    print("\nfilos id 1: \n")
    print(list_of_lists[0][0][1][0])
    print("\n\n\n")

    print("\nbuzna id 0: \n")
    print(list_of_lists[0][0][0][1])
    print("\n\n\n")

    print("\nbuzna id 1: \n")
    print(list_of_lists[0][0][1][1])
    print("\n\n\n")

    print(sql_same_business(cur,list_of_lists[0][0][0][0],list_of_lists[0][0][0][1]))
    print("\n\n\n")

    for i in range(len(list_of_lists[0][0])):
        print("\n")
        print(sql_same_business(cur,list_of_lists[0][0][i][0],list_of_lists[0][0][i][1]))
        print("\n")



    return [("user_id",),]



def sql_different_business(cur,user_Id):
    string_of_user = str(user_Id)
    print(string_of_user)

    sql= """
            SELECT f.friend_id, ru.business_id
            FROM friends f, user u, reviews ru, reviews rf
            WHERE u.user_id = f.user_id AND ru.business_id = rf.business_id AND u.user_id = ru.user_id 
                                        AND rf.user_id = f.friend_id AND ru.date < rf.date AND u.user_id = '"""+string_of_user+"""' ;
         """

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        friends=results 
    except :
        print("errooooor")
        return None
           
    return results

def sql_same_business(cur,friend_as_user,same_business_id):
    
    string_business = str(same_business_id)
    friend_as_user  = str(friend_as_user)

    sql= """
            SELECT f.friend_id
            FROM friends f, user u, reviews ru, reviews rf
            WHERE u.user_id = f.user_id AND ru.business_id = rf.business_id AND u.user_id = ru.user_id 
                            AND rf.user_id = f.friend_id AND ru.date < rf.date AND u.user_id = '"""+friend_as_user+"' AND rf.business_id = '"+string_business+"""';
         """

    try : 
        cur.execute(sql)
        results=cur.fetchall()
        influenced=results 
    except :
        print("error323423")
        return None

    return results 