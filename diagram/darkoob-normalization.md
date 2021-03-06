Darkoob's DataBase Normalization Diagram
========================================
At first step we should specific all data and first's plan of tables and specific all functional dependencies.

Preliminary Tables
------------------

### Table 1

	
		-----------------------------------------------------------------------------------------------------------------
		|         |           |       |      |       |      |      |        |          |           |          |         |
		|         V           V       V      V       V      V      V        V          V           V          V         V
	-----------------------------------------------------------------------------------------------------------------------------
	|user_name|first_name|last_name|email|password|gender|mobile|city_id|city_name|country_id|country_name|school_id|school_name|
	-----------------------------------------------------------------------------------------------------------------------------
			                                                         |         ^         ^ |         ^  ^         |         ^
									                                 |         |         | |         |  |         |         |
									                                 ---------------------------------  |         -----------
			                                                                               |            |
			                                                                               --------------

	

##### Functional Dependencies
1.	user_name -> Table 1
2.	city_id -> city_name, country_id, country_name 
3.	country_id -> country_name 
4.	school_id -> school_name


### Table 2

	
		 ----------------------------------------------------------------------------------------------------------------------------
		 |                    |        |         |              |               |            |              |                       |
		 V                    |        V         V              V               V            V              V                       V
	-----------------------------------------------------------------------------------------------------------------------------------------------
	|post_author_user_name|post_id|post_title|post_text|post_submitted_time|comment_id|comment_text|submited_comment_time|comment_author_user_name|
	-----------------------------------------------------------------------------------------------------------------------------------------------
		                                                                         |            ^                ^                     ^
		                                                                         |            |                |                     |
		                                                                         -----------------------------------------------------
	

##### Functional Dependencies

1.	post_id -> Table 2
2.	comment_id -> comment_text, submited_comment_time, comment_author_user_name

### Table 3

	

		-----------------------------------------------------------------------------------------------------------------------------------------------------------
		|       |            |              |            |          |            |           |          |            |              |             |       |       |
		|       V            V              V            V          V            V           V          V            V              V             V       V       V
	--------------------------------------------------------------------------------------------------------------------------------------------------------------------
	|book_id|book_title|publisher_id|publisher_name|language_id|language_name|author_id|author_name|author_rate|translator_id|translator_name|book_rate|tag_id|tag_name|
	--------------------------------------------------------------------------------------------------------------------------------------------------------------------
		                      |            ^              |           ^           |           ^          ^            |              ^                     |      ^
		                      |            |              |           |           |           |          |            |              |                     |      |
		                      --------------              -------------           ------------------------            ----------------                     --------

	

##### Functional Dependencies

1.	publisher_id -> publisher_name 
2. 	language_id -> language_name
3.	author_id -> author_name, author_rate
4.	translator_id -> translator_name
5.	tag_id -> tag_name
6.	book_id -> Table 3

### Table 4

	
		          ------------------------------------------------------
		          |                                                    V
	--------------------------------------------------------------------------
	|user_name|book_id|review_text|review_rate|review_submited_time|review_id|
	--------------------------------------------------------------------------
		 ^         ^          ^           ^              ^              |
		 |         |          |           |              |              |
		 ----------------------------------------------------------------

	

##### Functional Dependencies

1.	book_id -> review_id
2.	review_id -> Table 4

### Table 5

	
		 --------------------------------------------
		 |              |               |           |
		 |              V               V           V
	---------------------------------------------------------
	|user_name|followed_user_name|followed_date|followship_id|
	---------------------------------------------------------
		                ^               ^            |
		                |               |            |
		                ------------------------------
	

##### Functional Dependencies

1. user_name -> Table 5
2. followship -> followed_date, followed_user_name

All field's are atomic and in one normal form.

Normalization of Table1
-----------------------

user_name is a condidate key, In second normal form we should remove all partial dependancy. There are not exisits any partial dependancy in Table1 so Table1 is in second normal form.
In third normal forms we should remove all transitive dependance.
	 
	
### Table 1.1
	
		---------------------------------------------------------------------
		|         |           |       |      |       |      |      |        | 
		|         V           V       V      V       V      V      V        V       
	-------------------------------------------------------------------------------
	|user_name|first_name|last_name|email|password|gender|mobile|city_id|school_id|
	-------------------------------------------------------------------------------

	

This table is BC normal form(BCNF).
This table has multi-value dependency in mobile and school_id, so we should correction our table's:

#### Table 1.1.1
	
	    -----------
	    |         |
	    |         V
	------------------
	|user_name|mobile|
	------------------
	

#### Table 1.1.2
	
	     -----------
	     |         |
	     |         V
	---------------------
	|user_name|school_id|
	---------------------
	

#### Table 1.1.3
	
	    ------------------------------------------------------
	    |         |           |       |      |       |       |
	    |         V           V       V      V       V       V
	--------------------------------------------------------------
	|user_name|first_name|last_name|email|password|gender|city_id|
	--------------------------------------------------------------
	

### Table 1.2
	
	-----------------------
	|school_id|school_name|
	-----------------------
		 |         ^
		 |         |
		 -----------
	
This table is BCNF 

### Table 1.3
	
	------------------------------
	|city_id|city_name|country_id|
	------------------------------
	   |         ^         ^
	   |         |         | 
	   --------------------- 
	
This table is BCNF 

### Table 1.4
	
		  ------------
		  |          |
		  |          V
	-------------------------
	|country_id|country_name|
	-------------------------
	
This table is BCNF 

Normalization of Table 2
-----------------------

(post_id) is a candidate key, there are no exesits any partial dependency, so this table in second normal form ,but this isn't a 3NF(a transitive dep exsist):



### Table 2.1
	 
	------------------------------------------------------------------------
	|comment_id|comment_text|submited_comment_time|comment_author_user_name|
	------------------------------------------------------------------------
		   |            ^                ^                     ^
		   |            |                |                     |
		   -----------------------------------------------------
	
This table is BCNF 

### Table 2.2
	
		 ------------------------------------------------------------------------
		 |                    |        |         |              |               | 
		 V                    |        V         V              V               V
	-----------------------------------------------------------------------------------
	|post_author_user_name|post_id|post_title|post_text|post_submitted_time|comment_id|
	-----------------------------------------------------------------------------------

	
table 2.1 and table 2.2 are 3NF


there is a MVD in post_id and comment_id (becuase a post can have been many comments)
	
#### Table 2.2.1
	
	   -----------
	   |         |
	   |         V
	--------------------
	|post_id|comment_id|
	--------------------
	
This table is BCNF 

	
#### Table 2.2.2
	
	     --------------------------------------------------------
	     |                    |        |         |              |
	     V                    |        V         V              V 
	------------------------------------------------------------------------
	|post_author_user_name|post_id|post_title|post_text|post_submitted_time|
	------------------------------------------------------------------------
		
This table is BCNF
	
                          
Normalization of Table 3
-----------------------
book_id is condidate key of this table, In second normal form we should remove all transitive dependance. There are not exsists any transitive dependancy, so this table in second normal form.
In third normal forms we should remove all transitive dependance.


### Table 3.1
	
		------------------------------------------------------------------------------
		|       |            |            |          |          |            |       |
		|       V            V            V          V          V            V       V  
	--------------------------------------------------------------------------------------
	|book_id|book_title|publisher_id|language_id|author_id|translator_id|book_rate|tag_id|
	--------------------------------------------------------------------------------------
	
We see Multi value dependency(MVD) in tag_id and author_id and translator_id, so we have modified:


#### Table 3.1.1
	
	    ----------------------------------------------
	    |       |            |            |          |         
	    |       V            V            V          V          
	-------------------------------------------------------
	|book_id|book_title|publisher_id|language_id|book_rate|
	-------------------------------------------------------
		
This table is BCNF 

#### Table 3.1.2
	
	     --------
	     |      |
	     |      V
	-------------------
	|book_id|author_id|
	-------------------
		
This table is BCNF 

#### Table 3.1.3
	
	     --------
	     |      |
	     |      V
	-----------------------
	|book_id|translator_id|
	-----------------------
		
This table is BCNF 

#### Table 3.1.4

	
	     --------
	     |      |
	     |      V
	----------------
	|book_id|tag_id|
	----------------
		
This table is BCNF 




### Table 3.2
	
	-----------------------------
	|publisher_id|publisher_name|
	-----------------------------
		  |            ^              
		  |            |    
		  -------------- 
	
This table is BCNF 

### Table 3.3
	
	---------------------------
	|language_id|language_name|
	---------------------------
		  |            ^              
		  |            |    
		  --------------
	

This table is BCNF 

### Table 3.4 
	
	-----------------------------------
	|author_id|author_name|author_rate|
	-----------------------------------
		 |         ^            ^  
		 |         |            |
		 ------------------------
	
This table is BCNF 

### Table 3.5
	
	-------------------------------
	|translator_id|translator_name|
	-------------------------------
		  |              ^              
		  |              |    
		  ---------------- 
	
This table is BCNF 

### Table3.6
	
	-----------------
	|tag_id|tag_name|
	-----------------
	   |       ^              
	   |       |    
	   --------- 
	
This table is BCNF 

Normalization of Table 4
-----------------------

there is not exeist any partial dependency and transitive dependency, but this table isn't BCNF

### Table 4.1 

	
		---------
		|       |
		|       V
	-------------------
	|book_id|review_id|
	-------------------

	
This table is BCNF 

### Table 4.2
	
	------------------------------------------------------------------
	|user_name|review_text|review_rate|review_submited_time|review_id|
	------------------------------------------------------------------
		 ^         ^          ^                   ^             |
		 |         |          |                   |             |
		 --------------------------------------------------------
	
This table is BCNF 

Normalizattion of Table5
------------------------

user_name is a condidate key for this table, and there are no exsist any partial depandency.
for convert this table to third normal form we should remove all transitive dependancy.

### Table 5.1
	
		 --------------
		 |            |   
		 |            V   
	-------------------------
	|user_name|followship_id|
	-------------------------

	
This table is BCNF 


### Table 5.2
	
	------------------------------------------------
	|followed_user_name|followed_date|followship_id|
	------------------------------------------------
		     ^               ^            |
		     |               |            |
		     ------------------------------
	

This table is BCNF 








Final Table's After Normalization
---------------------------------
*	user_mobile(user_name, mobile)
*	user_school(user_name, school_id)
*	user_profile(user_name, first_name, last_name, email, password, gender, city_id)
*	schools(school_id, school_name)
*	cites(city_id, city_name, country_id)
*	countries(country_id, country_name)
*	post_comment(post_id, comment_id)
*	posts(post_author_user_name, post_id, post_title, post_text, post_submitted_time)
*	books(book_id, book_title, publisher_id, language_id, book_rate)
*	book_author(book_id, book_author)
*	book_translator(book_id, translator_id)
*	book_tag(book_id, tag_id)
*	publishers(publisher_id, publisher_name)
*	languages(language_id, language_name)
*	authors(author_id, author_name, author_rate)
*	translators(translator_id, translator_name)
*	tags(tag_id, tag_name)
*	book_review(book_id, review_id)
*	reviews(review_id, user_name, review_text, review_rate, review_submited_time)
*	user_followship(user_name, followship_id)
*	followship(followed_user_name, followed_date, followship_id)


Functional Dependence:


	
	    -----------
	    |         |
	    |         V
	------------------
	|user_name|mobile|
	------------------
	

	
	     -----------
	     |         |
	     |         V
	---------------------
	|user_name|school_id|
	---------------------
	

	
	    ------------------------------------------------------
	    |         |           |       |      |       |       |
	    |         V           V       V      V       V       V
	--------------------------------------------------------------
	|user_name|first_name|last_name|email|password|gender|city_id|
	--------------------------------------------------------------
	

	
	-----------------------
	|school_id|school_name|
	-----------------------
		 |         ^
		 |         |
		 -----------
	

	
	------------------------------
	|city_id|city_name|country_id|
	------------------------------
	   |         ^         ^
	   |         |         | 
	   --------------------- 
	

	
		  ------------
		  |          |
		  |          V
	-------------------------
	|country_id|country_name|
	-------------------------
	

	
	   -----------
	   |         |
	   |         V
	--------------------
	|post_id|comment_id|
	--------------------
	
	

	

	     --------------------------------------------------------
	     |                    |        |         |              |
	     V                    |        V         V              V 
	------------------------------------------------------------------------
	|post_author_user_name|post_id|post_title|post_text|post_submitted_time|
	------------------------------------------------------------------------
		

	
	    ----------------------------------------------
	    |       |            |            |          |         
	    |       V            V            V          V          
	-------------------------------------------------------
	|book_id|book_title|publisher_id|language_id|book_rate|
	-------------------------------------------------------
		

	
	     --------
	     |      |
	     |      V
	-------------------
	|book_id|author_id|
	-------------------
		

	
	     --------
	     |      |
	     |      V
	-----------------------
	|book_id|translator_id|
	-----------------------
		

	
	     --------
	     |      |
	     |      V
	----------------
	|book_id|tag_id|
	----------------
	
	
	
	-----------------------------
	|publisher_id|publisher_name|
	-----------------------------
		  |            ^              
		  |            |    
		  -------------- 
	

	
	---------------------------
	|language_id|language_name|
	---------------------------
		  |            ^              
		  |            |    
		  --------------
	 

	
	-----------------------------------
	|author_id|author_name|author_rate|
	-----------------------------------
		 |         ^            ^  
		 |         |            |
		 ------------------------
	

	
	-------------------------------
	|translator_id|translator_name|
	-------------------------------
		  |              ^              
		  |              |    
		  ---------------- 
	

	
	-----------------
	|tag_id|tag_name|
	-----------------
	   |       ^              
	   |       |    
	   --------- 
	

	
		---------
		|       |
		|       V
	-------------------
	|book_id|review_id|
	-------------------

	

	
	------------------------------------------------------------------
	|user_name|review_text|review_rate|review_submited_time|review_id|
	------------------------------------------------------------------
		 ^         ^          ^                   ^             |
		 |         |          |                   |             |
		 --------------------------------------------------------
	

	
		 --------------
		 |            |   
		 |            V   
	-------------------------
	|user_name|followship_id|
	-------------------------

	

	
	------------------------------------------------
	|followed_user_name|followed_date|followship_id|
	------------------------------------------------
		     ^               ^            |
		     |               |            |
		     ------------------------------
	



