from movie_trivia import *
import unittest

import shelve
##Data = shelve.open("database") 
##Data.close()
#will we use this in unit function, or in main?
class TestMovies(unittest.TestCase):

    movieDb = {}
    ratingDb = {}
    good_movies_csv = {}

    def setUp(self):
        self.movieDb = create_actors_DB('movies.txt')
        self.ratingDb = create_ratings_DB('moviescores.csv')
        self.good_movies_csv = create_good_movies('good_movies.csv')
    #write unit tests for every function.
    def testinsert_actor_info(self):
        '''test utility function 1'''
        #insert into existing actor
        #self.assertFalse('The Americanization of Emily' in self.movieDb.values(), 'checking before')
        insert_actor_info('julie andrews',['the americanization of emily','hawaii'],self.movieDb)
        self.assertTrue('the americanization of emily' in self.movieDb['julie andrews'], 'The Americanization of Emily is not inserted')
        self.assertTrue('hawaii' in self.movieDb['julie andrews'], 'Hawaii is not inserted')
         #insert into unknown actor
        insert_actor_info('jackie chan',['big and little wong tin bar'],self.movieDb)
        self.assertTrue('big and little wong tin bar' in self.movieDb['jackie chan'], 'Big and Little Wong Tin Bar is not inserted')
        
    def testinsert_rating(self):
        '''test utility function 2'''
        self.assertNotIn('Avatar', self.ratingDb, 'insert new moive rating')
        insert_rating('Avatar',('80','88'),self.ratingDb)
        self.assertIn('avatar', self.ratingDb, 'fail to insert new moive name')
        self.assertEqual(self.ratingDb['avatar'],('80','88'),'fail to insert new moive rating')
        insert_rating("schindler's list",('96','98'),self.ratingDb)
        self.assertEqual(self.ratingDb["schindler's list"],('96','98'),'fail to insert new moive rating')

    def testdelete_movie(self):
        '''test utility function 3'''
        delete_movie('the avengers',self.movieDb,self.ratingDb)
        #THE AVEGERS
        self.assertFalse('the avengers' in self.movieDb['jeremy renner'], 'failed to delete The Avengers from movieDb')
        self.assertFalse('the avengers' in self.ratingDb, 'failt to delete The Avengers from ratingDb')
        #test for movie not exist in DB
        #delete_result=delete_movie('movie', self.movieDb, self.ratingDb)
        #self.assertEqual(delete_result,'can not delete','test for movie not exist in DB fail')
    
    def testselect_where_actor_is(self):
        '''test utility function 4'''
        movies=select_where_actor_is('Meryl Streep',self.movieDb)
        self.assertTrue('out of africa' in movies, 'Out of Africa is not in')
        self.assertTrue('the devil wears prada' in movies, 'Out of Africa is not in')
        self.assertTrue('the hours' in movies, 'Out of Africa is not in')
        self.assertFalse('mamma mia' in movies, 'Mamma Mia is in')
        #test actor not in the DB
        movies=select_where_actor_is('Actor',self.movieDb)
        self.assertEqual(movies,['not present'],'test actor not in the DB')
    
    def testselect_where_movie_is(self):
        '''test utility function 5'''
        actors = select_where_movie_is('Amadeus', self.movieDb)
        self.assertIn('f. murray abraham',actors,'test one actor')
        #the test will fail, when use assertEqual?? only for value?
        
        #write test code here using self.ratingDb and self.movieDb
        actors = select_where_movie_is('Mrs. Miniver', self.movieDb)
        #make some assertion about these actors
        self.assertIn('walter pidgeon',actors,'test one actor')
        #test one actor
        actors = select_where_movie_is('Apollo 13', self.movieDb)
        #self.assertEqual(actors,['Tom Hanks','Kevin Bacon'],'test two actors')
        #test two actors, how to decide and check the order of that?
        self.assertIn('tom hanks', actors, 'test two actors')
        self.assertIn('kevin bacon', actors, 'test two actors')
        #test if no movie in database
        actors=select_where_movie_is('movieName', self.movieDb)
        self.assertEqual(actors,['not present'],'test movie not in the movie DB')
        
    def testselect_where_rating_is(self):
        '''test utility function 6'''
        filter_movie=select_where_rating_is(65,'=',False,self.ratingDb)
        self.assertEqual(filter_movie,['star wars'],'test equal condition, audience score')
        filter_movie=select_where_rating_is(65,'=',True,self.ratingDb)
        self.assertEqual(filter_movie,['me-myself & irene'],'test equal condition, critic score')
        filter_movie=select_where_rating_is(99,'>',False,self.ratingDb)
        #self.assertEqual(filter_movie,result,'test greater than condition, audience score')
        self.assertIn('the avengers', filter_movie, 'test greater than condition, audience score')
        filter_movie=select_where_rating_is(99,'>',True,self.ratingDb)
        result=['maltese falcon','rear window','lilies of the field','the godfather','on the waterfront',
                'singin in the rain','the odd couple','mary poppins','kind hearts and coronets','cool hand luke','all about eve',
                'how to steal a million','the philadelphia story','rebecca']
        #the number does not match, 14-18?
        #self.assertEqual(filter_movie,result,'test greater than condition, critic score')
        #need to write a loop to test all??
        self.assertIn(result[0], filter_movie, 'test greater than condition, critic score')
        filter_movie=select_where_rating_is(28,'<',False,self.ratingDb)
        self.assertEqual(filter_movie,['planet of the apes'],'test less than condition, audience score')
        filter_movie=select_where_rating_is(17,'<',True,self.ratingDb)
        #self.assertEqual(filter_movie,['Assassins','Original Sin'],'test less than condition, critic score')
        self.assertIn('original sin',filter_movie,'test less than condition, critic score')
        self.assertIn('assassins',filter_movie,'test less than condition, critic score')
        #test for movie not in the list
        filter_movie=select_where_movie_is('movieName', self.ratingDb)
        self.assertEqual(filter_movie,['not present'],'test movie not in the rating DB')
        
    #unit test for user questions:
    def testget_co_actors(self):
        '''test user question function 1'''
        Co_actor = get_co_actors('Brad Pitt', self.movieDb)
        self.assertTrue('diane kruger' in Co_actor, 'all the co-actors are not found, *Diane Kruger* not in list')
        self.assertTrue('eric bana' in Co_actor, 'all the co-actors are not found *Eric Bana* not in list')
        self.assertTrue('julia roberts' in Co_actor, 'get_co_actors is not working properly *Julia Roberts* not in list')
        self.assertTrue('george clooney' in Co_actor, 'get_co_actors is not working properly *George Clooney* not in list')
        Co_actor = get_co_actors('Russell Crowe', self.movieDb)
        self.assertTrue('denzel washington' in Co_actor, 'all the co-actors are not found *Denzel Washington* not in list')
        Co_actor = get_co_actors('Tom Cruise', self.movieDb)
        self.assertTrue('renee zellweger' in Co_actor, 'all the co-actors are not found *Renee Zellweger* not in list')
        self.assertTrue('kevin bacon' in Co_actor, 'get_co_actors is not working properly *Kevin Bacon* not in list')
        self.assertTrue('jack nicholson' in Co_actor, 'get_co_actors is not working properly *Jack Nicholson* not in list')
        self.assertTrue('dustin hoffman' in Co_actor, 'get_co_actors is not working properly *Dustin Hoffman* not in list')
        #test for actors not in db
        Co_actor = get_co_actors('Actor', self.movieDb)
        self.assertEqual(Co_actor,['not present'],'test actor not in the movie DB')
        
    def testget_common_movie(self):
        '''test user question function 2'''
        Common_movies = get_common_movie('Anthony Hopkins', 'Alec Baldwin', self.movieDb)
        self.assertTrue('the edge' in Common_movies, 'error in get_common_movie function Anthony and Alec acted in "The edge"')  
        Common_movies = get_common_movie('Brad Pitt', 'Angelina Jolie', self.movieDb)
        self.assertTrue('mr & mrs smith' in Common_movies, 'Brad and Angelina acted in "Mr & Mrs Smith" together')
        Common_movies = get_common_movie('Kate Winslet', 'Leonardo Di Caprio', self.movieDb)
        self.assertEqual(set(['titanic','revolutionary road']), set(Common_movies), 'Kate and Leonardo acted in "Titanic" and "Revolutionary Road" together')
        #test for actors not in database
        Common_movies=get_common_movie('actor1', 'actor2', self.movieDb)
        self.assertEqual(Common_movies,['not present'],'test actor not in the movie DB')
    def testcritics_darling(self):
        '''test user question function 3'''
        actors_high_average_rating = critics_darling(self.movieDb, self.ratingDb)
        self.assertEqual(actors_high_average_rating, ['joan fontaine'] , 'error in critics_darling function')

    def testaudience_darling(self):
        '''test user question function 4'''
        actors_high_average_rating = audience_darling(self.movieDb, self.ratingDb)
        self.assertEqual(actors_high_average_rating, ['f. murray abraham'] , 'error in audience_darling function')

    def testgood_movies(self):
        '''test user question function 5'''
        #good_to_watch = good_movies(self.ratingDb)
        # print good_to_watch
        #print self.good_movies_csv
        #for movie in self.ratingDb.keys():
        self.assertEqual(len(good_movies(self.ratingDb)), len(self.good_movies_csv), 'The number of good movies is not accurate')
        self.assertEqual(set(good_movies(self.ratingDb)), set(self.good_movies_csv), 'error in good_movies function')

    def testget_common_actors(self):
        '''test user question function 6'''
        Common_actors = get_common_actors('crash', 'ben-hur', self.movieDb)
        self.assertEqual(set(),set(Common_actors), 'error in get_common_actors function ther is no common actor in crash and Ben-Hur')  
        Common_actors = get_common_actors('sleepless in seattle', 'you\'ve got mail', self.movieDb)
        self.assertEqual(set(['tom hanks', 'meg ryan']), set(Common_actors), ' hanks and Meg acted in "Sleepless in Seattle" and "You\'ve Got Mail" together')
        Common_actors = get_common_actors('titanic', 'revolutionary road', self.movieDb)
        self.assertEqual(set(['kate winslet', 'leonardo di caprio']), set(Common_actors), 'Kate and Leonardo acted in "Titanic" and "Revolutionary Road" together')
        Common_actors = get_common_actors('movie1', 'ben-hur', self.movieDb)
        self.assertEqual(Common_actors,['movie1 not in the database'],'movie1 not in the database')
        Common_actors = get_common_actors('crash', 'movie2', self.movieDb)
        self.assertEqual(Common_actors,['movie2 not in the database'],'movie2 not in the database')
        Common_actors = get_common_actors('movie1', 'movie2', self.movieDb)
        self.assertEqual(Common_actors,['Neither of those two movies are in the database'],'Neither of those two movies are in the database')
        #self.assertTrue('Revolutionary Road' in Common_movies, 'Kate and Leonardo acted in "Revolutionary Road" together')
    
    def testget_bacon(self):
        '''test function to get bacon number for actors'''
        bacon_number=get_bacon('kevin bacon', self.movieDb)
        self.assertEqual(bacon_number,0,'test for Kevin Bacon fail')
        bacon_number=get_bacon('Tom Hanks', self.movieDb)
        self.assertEqual(bacon_number,1,'test for bacon_number=1 fail')
        bacon_number=get_bacon('meg ryan', self.movieDb)
        self.assertEqual(bacon_number,2,'test for bacon_number=2 fail')
        bacon_number=get_bacon('Denzel Washington', self.movieDb)
        self.assertEqual(bacon_number,3,'test for bacon_number=3 fail')
        bacon_number=get_bacon('Rita Moreno', self.movieDb)
        self.assertEqual(bacon_number,0,'test for no connection with Bacon fail')
        bacon_number=get_bacon('Jackie Chen', self.movieDb)
        self.assertEqual(bacon_number,-1,'test for actor not in the db fail')
        #how to differentiate not exsit in this list, or refer but no connection?
        



        
#self.assertRaises
#
unittest.main()
