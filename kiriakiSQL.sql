-- 1 
SELECT u.user_id
FROM user u
WHERE name = 'Lisa' AND u.review_count >500
ORDER BY  u.yelping_since;

-- 2 
SELECT 
EXISTS  (
			SELECT *
            FROM business b, reviews r , user u
            WHERE u.user_id = r.user_id and r.business_id = b.business_id and b.name = 'Gab & Eat' and u.name = 'Lisa'
		) AS YparxeiTetoiaAnafora;

-- 21 
SELECT COUNT(r.review_id) AS IF_EXISTS 
FROM reviews r 
WHERE EXISTS ( 
				SELECT r.* 
                FROM user u, business b 
                WHERE u.user_id = r.user_id AND r.business_id = b.business_id AND b.name = 'Gab & Eat' AND u.name = 'Lisa'
                ); 

-- 3
SELECT 'Yes' as Answer
where EXISTS (
				SELECT rpn.positive 
				FROM business b ,reviews_pos_neg rpn , reviews r
				WHERE b.business_id=r.business_id and  b.business_id = 'OmpbTu4deR3ByOo7btTTZw' and rpn.review_id=r.review_id and rpn.positive=1 
			)
UNION
SELECT 'No' as Answer
where not EXISTS (
				SELECT rpn.positive 
				FROM business b ,reviews_pos_neg rpn , reviews r
				WHERE b.business_id=r.business_id and  b.business_id = 'OmpbTu4deR3ByOo7btTTZw' and rpn.review_id=r.review_id and rpn.positive=1 
			);


-- 4
SELECT COUNT(*) as HowMany FROM (
								SELECT distinct(b.business_id) 
								FROM business b, reviews r
								WHERE r.business_id = b.business_id AND r.date=2014
								GROUP BY b.business_id
								HAVING COUNT(r.review_id) > 10) poses;

-- 41
-- SELECT *
-- FROM  business b, reviews r
-- WHERE r.business_id = b.business_id AND IN (  
-- 		SELECT rpn.*
-- 		FROM  reviews_pos_neg rpn 
-- 		WHERE  r.review_id = rpn.review_id AND r.date=2014
--         GROUP BY b.business_id
-- 		HAVING COUNT(r.review_id) > 10
-- 	);
                                
                                
-- 5
SELECT u.user_id, COUNT(DISTINCT r.review_id) AS Reviews
FROM reviews r, user u , business b , business_category bc , category c
WHERE r.business_id=b.business_id AND bc.business_id=b.business_id AND r.user_id=u.user_id AND bc.category_id=c.category_id AND c.category='Mobile Phones' 
GROUP BY u.user_id ;


-- 6
SELECT u.user_id , r.votes_useful
FROM reviews r, user u , business b 
WHERE u.user_id=r.user_id AND b.business_id=r.business_id and b.name='Midas'
ORDER BY r.votes_useful DESC;
