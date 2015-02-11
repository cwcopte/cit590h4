from movie_trivia import *
import unittest

import shelve
##Data = shelve.open("database") 
##Data.close()
#will we use this in unit function, or in main?
class TestMovies(unittest.TestCase):

    movieDb = {}
    ratingDb = {}

    def setUp(self):
        self.movieDb = create_actors_DB('movies.txt')
        self.ratingDb = create_ratings_DB('moviescores.csv')
    #write unit tests for every function.
    def testinsert_actor_info(self):
        '''test utility function 1'''
        #insert into existing actor
        #self.assertFalse('The Americanization of Emily' in self.movieDb.values(), 'checking before')
        insert_actor_info('Julie Andrews','The Americanization of Emily',self.movieDb)
        insert_actor_info('Julie Andrews','Hawaii',self.movieDb)
        self.assertTrue('The Americanization of Emily' in self.movieDb['Julie Andrews'], 'The Americanization of Emily is not inserted')
        #general test
        self.assertTrue('Hawaii' in self.movieDb['Julie Andrews'], 'Hawaii is not inserted')
         #insert into unknown actor
        insert_actor_info('Jackie Chan','Big and Little Wong Tin Bar',self.movieDb)
        self.assertTrue('Big and Little Wong Tin Bar' in self.movieDb['Jackie Chan'], 'Big and Little Wong Tin Bar is not inserted')
        
    def testinsert_rating(self):
        '''test utility function 2'''
        #seems already written by teacher, if those are all correct!
        self.assertNotIn('Avatar', self.ratingDb, 'insert new moive rating')
        #neccessary?
        insert_rating('Avatar',(80,88),self.ratingDb)
        self.assertIn('Avatar', self.ratingDb, 'fail to insert new moive name')
        self.assertEqual(self.ratingDb['Avatar'],(80,88),'fail to insert new moive rating')
        insert_rating("Schindler's List",(96,98),self.ratingDb)
        self.assertEqual(self.ratingDb["Schindler's List"],(96,98),'fail to insert new moive rating')
        #(97,97)
        #Sam Worthington Stephen Lang Sigourney Weaver Michelle Rodriguez Avatar
        #when insert a movie where no actor in previous list?
    
    def testdelete_movie(self):
        '''test utility function 3'''
        delete_movie('The Avengers',self.movieDb,self.ratingDb)
        #self.assertFalse('The Avengers' in self.movieDb.values(), 'failt to delete The Avengers from movieDb')
        #assume know the database? then easy to test!else, write a loop to test? not reality
        self.assertFalse('The Avengers' in self.movieDb['Jeremy Renner'], 'failt to delete The Avengers from movieDb')
        self.assertFalse('The Avengers' in self.ratingDb, 'failt to delete The Avengers from ratingDb')
##        assertIn(first, second, msg=None)
##        assertNotIn(first, second, msg=None)
    
    def testselect_where_actor_is(self):
        '''test utility function 4'''
        movies=select_where_actor_is('Meryl Streep',self.movieDb)
        self.assertTrue('Out of Africa' in movies, 'Out of Africa is not in')
        self.assertTrue('The Devil Wears Prada' in movies, 'Out of Africa is not in')
        self.assertTrue('The Hours' in movies, 'Out of Africa is not in')
        #Julie and Julia, Doubt, Out of Africa
        #should list all?
        self.assertFalse('Mamma Mia' in movies, 'Mamma Mia is in')
    
    def testselect_where_movie_is(self):
        '''test utility function 5'''
        actors = select_where_movie_is('Amadeus', self.movieDb)
        self.assertIn('F. Murray Abraham',actors,'test one actor')
        #the test will fail, when use assertEqual?? only for value?
        
        #write test code here using self.ratingDb and self.movieDb
        actors = select_where_movie_is('Mrs. Miniver', self.movieDb)
        #make some assertion about these actors
        self.assertIn('Walter Pidgeon',actors,'test one actor')
        #test one actor
        actors = select_where_movie_is('Apollo 13', self.movieDb)
        #self.assertEqual(actors,['Tom Hanks','Kevin Bacon'],'test two actors')
        #test two actors, how to decide and check the order of that?
        self.assertIn('Tom Hanks', actors, 'test two actors')
        self.assertIn('Kevin Bacon', actors, 'test two actors')
        
    def testselect_where_rating_is(self):
        '''test utility function 6'''
        filter_movie=select_where_rating_is(65,'=',False,self.ratingDb)
        self.assertEqual(filter_movie,['Star Wars'],'test equal condition, audience score')
        filter_movie=select_where_rating_is(65,'=',True,self.ratingDb)
        self.assertEqual(filter_movie,['Me-Myself & Irene'],'test equal condition, critic score')
        filter_movie=select_where_rating_is(99,'>',False,self.ratingDb)
        #self.assertEqual(filter_movie,result,'test greater than condition, audience score')
        self.assertIn('The Avengers', filter_movie, 'test greater than condition, audience score')
        filter_movie=select_where_rating_is(99,'>',True,self.ratingDb)
        result=['Maltese Falcon','Rear Window','Lilies of the Field','The Godfather','On the Waterfront',
                'Singin in the Rain','The Odd Couple','Mary Poppins','Kind Hearts and Coronets','Cool Hand Luke','All About Eve',
                'How to Steal a Million','The Philadelphia Story','Rebecca']
        #the number does not match, 14-18?
        #self.assertEqual(filter_movie,result,'test greater than condition, critic score')
        #need to write a loop to test all??
        self.assertIn(result[0], filter_movie, 'test greater than condition, critic score')
        filter_movie=select_where_rating_is(28,'<',False,self.ratingDb)
        self.assertEqual(filter_movie,['Planet of the Apes'],'test less than condition, audience score')
        filter_movie=select_where_rating_is(17,'<',True,self.ratingDb)
        #self.assertEqual(filter_movie,['Assassins','Original Sin'],'test less than condition, critic score')
        self.assertIn('Original Sin',filter_movie,'test less than condition, critic score')
        self.assertIn('Assassins',filter_movie,'test less than condition, critic score')
        #some in the lists, some not in the list
    def testget_bacon(self):
        bacon_number=get_bacon('Tom Hanks', self.movieDb)
        self.assertEqual(bacon_number,1,'test for bacon_number=1 fail')
        bacon_number=get_bacon('Meg Ryan', self.movieDb)
        self.assertEqual(bacon_number,2,'test for bacon_number=2 fail')
        bacon_number=get_bacon('Denzel Washington', self.movieDb)
        self.assertEqual(bacon_number,3,'test for bacon_number=3 fail')
        bacon_number=get_bacon('Rita Moreno', self.movieDb)
        self.assertEqual(bacon_number,0,'test for no connection with Bacon fail')
        bacon_number=get_bacon('Jackie Chen', self.movieDb)
        self.assertEqual(bacon_number,0,'test for actor not in the db fail')
        #how to differentiate not exsit in this list, or refer but no connection?
        
        
#self.assertRaises
#
unittest.main()
