# movie trivia.py
# Jubi, Wei Chen

#use these first 2 functions to create your 2 dictionaries
import csv
def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        #should we change this, so we can further edit and append?
        #movieInfo[actor] = set(movies)
        movieInfo[actor] = movies
        #movieInfo[actor]=set([])
        #movieInfo.get(actor).union(set(cleaned_movies))
    f.close()
    return movieInfo

def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict
##########

def insert_actor_info(actor, movies, movie_Db):
    '''insert into/updat movie_Db using actor and movies data'''
    #movie_list = []
    #typo
    movies_list = []
    if actor in movie_Db:
        movies_list = movie_Db[actor]
    #movies_list.extend(movies)
    movies_list.append(movies)
    movie_Db[actor] = movies_list
    #why this?
    

def insert_rating(movie, ratings, ratings_Db):
    ''' insert into/updat ratings_Db using ratings and movies data'''
    ratings_Db[movie] = ratings

def delete_movie(movie, movie_Db, ratings_Db):
    ''' delete all information from the database that corresponds to this movie'''
    del ratings_Db[movie]
    movies_of_all_actors = movie_Db.values()
    for movies_list in movies_of_all_actors:
        if movie in movies_list:
            movies_list.remove(movie)
        #problems here!!

def select_where_actor_is(actorName, movie_Db):
    '''given an actor, return the list of all movies'''
    return movie_Db[actorName]

def select_where_movie_is(movieName, movie_Db):
    '''given a movie, return the list of all actors'''
    all_actors_list = movie_Db.keys()
    actors_list = []
    for actor in all_actors_list[0:]:
        if movieName in movie_Db[actor]:
            actors_list.append(actor)
            #the last item cannot be got, because the value missing in first movie_Db!!
    return actors_list

def select_where_rating_is(targeted_rating, comparison, is_critic, ratings_Db):
    ''' returns a list of movies that satisfy an inequality or equality based
on the comparison argument and the targeted rating argument'''
    movies_with_target = []
    all_movies_list = ratings_Db.keys()
    for movie in all_movies_list:
        rating_tuple = ratings_Db[movie]
        if is_critic:
            rating = int(rating_tuple[0])
        else:
            rating = int(rating_tuple[1])
        if comparison == '=':
            if rating == targeted_rating:
                movies_with_target.append(movie)
        if comparison == '<':
            if rating < targeted_rating:
                movies_with_target.append(movie)
        if comparison == '>':
            if rating > targeted_rating:
                movies_with_target.append(movie)
    #return movie_with_target
    #typo
    return movies_with_target

#another coding for function 6!!!!!!!
##def select_where_rating_is(targeted_rating, comparison, is_critic, ratings_Db):
##    movies_with_target = []
##    all_movies_list = ratings_Db.keys()
##    if comparison == '=':
##        for movie in all_movies_list:
##            rating_tuple = ratings_Db[movie]
##            if is_critic == True:
##                rating = rating_tuple[0]
##            else:
##                rating = rating_tuple[1]
##            if rating == targeted_rating:
##                movies_with_target.append(movie)
##    if comparison == '<':
##        for movie in all_movies_list:
##            rating_tuple = ratings_Db[movie]
##            if is_critic == True:
##                rating = rating_tuple[0]
##            else:
##                rating = rating_tuple[1]
##            if rating < targeted_rating:
##                movies_with_target.append(movie)
##    if comparison == '>':
##        for movie in all_movies_list:
##            rating_tuple = ratings_Db[movie]
##            if is_critic == True:
##                rating = rating_tuple[0]
##            else:
##                rating = rating_tuple[1]
##            if rating > targeted_rating:
##                movies_with_target.append(movie)
##    #return movie_with_target
##    return movies_with_target
    
#


def get_co_actors(actorName, moviedb):
    co_actors = []
    movies_acted = moviedb[actorName]
    for movie in movies_acted:
        for actor in moviedb.keys():
            if movie in moviedb[actor] and actor != actorName:
                co_actors.append(actor)
    return co_actors

def get_common_movie(actor1, actor2, moviedb):
    common_movies = []
    movies_actor1_acted = moviedb[actor1]
    for movie in movies_actor1_acted:
        if movie in moviedb[actor2]:
            common_movies.append(movie)
    return common_movies

##def critics_darling(movie_Db, ratings_Db):
##actor_and_rating = {}
##actors_wid_hi_rating = []
##highest_rating = 0
##for actor in movie_Db.keys():
##sum_of_rating = 0
###should the average be float??
##no_of_movies = 0
##for movie in movie_Db[actor]:
##if movie in ratings_Db.keys():
##rating_tuple = ratings_Db[movie]
##sum_of_rating += int(rating_tuple[0])
##no_of_movies += 1
##average_rating = sum_of_rating / no_of_movies
##actor_and_rating[actor] = average_rating
##if highest_rating < average_rating:
##highest_rating = average_rating
##for actor in actor_and_rating.keys():
##if actor_and_rating[actor] == highest_rating:
##actors_wid_hi_rating.append(actor)
##return actors_wid_hi_rating
   
#USER QUESTION!!!!!!!!!!

#def get_co_actors(actorName, moviedb):

def audience_darling(movie_Db, ratings_Db):
    '''finding the actor whose movies have the highest average rotten tomatoes rating, as per the audience.This returns a list of actors '''
    freq={}
    #select_where_actor_is(actorName, movie_Db)
    movie_Db.values()
    for actor in movie_Db.keys():
        i=0
        #how to deal with the error, cannot find relative rating in another db?
        for movies in movie_Db[actor]:
            i+=1
            if movies in ratings_Db.keys():
                rate_per_audience=ratings_Db[movies]
                #takes care of word not being in dict initially
                freq[actor] = freq.get(actor,0) + int(rate_per_audience[0])
        #freq[actor]=freq[actor]/float(len(movie_Db[actor]))
        freq[actor]=freq[actor]/float(i)
        #what if not all the movies are in ratingDB
    for actor in freq.keys():
        if freq[actor]==max(freq.values()):
            #return actor
            #only one return?
            audience_darling=actor
    #print audience_darling
    return audience_darling

def good_movies(ratings_Db):
    ''' returns the set of movies that both critics and the audience have rated above 85 (greater than equal to 85). '''
    good_movies=[]
    audience_rate1=select_where_rating_is(85, '=', False, ratings_Db)
    udience_rate2=select_where_rating_is(85, '>', False, ratings_Db)
    for movies in udience_rate2:
        audience_rate1.append(movies)
    #print audience_rate1
    #print len(audience_rate1)
    critics_rate1=select_where_rating_is(85, '=', True, ratings_Db)
    critics_rate2=select_where_rating_is(85, '>', True, ratings_Db)
    for movies in critics_rate2:
        critics_rate1.append(movies)
    #print critics_rate1
    #print len(critics_rate1)
    for moives in audience_rate1:
        if moives in critics_rate1:
            good_movies.append(moives)
    #print good_movies
    #print len(good_movies)
    return good_movies
#might not be the optimal one, but this could use former constructed code
    
def get_common_actors(movie1, movie2, movies_Db):
    ''' Given a pair of movies, return a list of actors that acted in both'''
    actors_list=[]
    actors_list1=select_where_movie_is(movie1, movies_Db)
    actors_list2=select_where_movie_is(movie2, movies_Db)
    for actors in actors_list1:
        if actors in actors_list2:
            actors_list.append(actors)
    print actors_list
    return actors_list
    #what if no common actors? return a message?

def get_bacon(actor, movieDb):
    ''' Get an actor's Bacon number'''
    actor_list=['Kevin Bacon']
    co_actors=get_co_actors('Kevin Bacon', movieDb)
    for co_actor in co_actors:
        actor_list.append(co_actor)
    actor_list=set(actor_list)
    actor_list=list(actor_list)
    co_actors_list=[]
    i=0
    #set? list?
    #print len(set(movieDb.keys()))
    #print len(actor_list)
    #print len(movieDb)
    #while len(actor_list)!=3:
    while len(actor_list)!=63:
        #caculate with the outcome, how can we get at first??
        #what if the database changes?
        i+=1
        if actor in co_actors:
            return i
            #break
        else:
            #print i
            for next_actor in co_actors:
                co_actors_next=get_co_actors(next_actor, movieDb)
                for every_actor in co_actors_next:
                    co_actors_list.append(every_actor)
                    actor_list.append(every_actor)
                #print co_actors_list
                co_actors_list=set(co_actors_list)
                co_actors_list=list(co_actors_list)
                co_actors=co_actors_list
        actor_list=set(actor_list)
        actor_list=list(actor_list)
        #print len(actor_list),'len'
        #print actor_list
    return 0

def main():
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    # PLEASE TAKE THE NEXT FEW PRINTING LINES OUT
    # ONCE YOU HAVE CONFIRMED THIS WORKS
##    print actor_DB.keys()
##    print ratings_DB.keys()
##    print '\n'
##    print actor_DB['Humphrey Bogart']
    #print ratings_DB['Rambo']
##    #name=select_where_movie_is('Mrs. Miniver', ratings_DB)
##    #print name
##    print ratings_DB['The Avengers']
##    print 'The Avengers' in actor_DB.values()
##    print 'MASH' in actor_DB.values()[0]
##    #print 'The Avengers' in ratings_DB
##    print actor_DB.values()
    #print len(actor_DB)
##    print 'Walter Pidgeon' in actor_DB
##    
    #print len(ratings_DB)
    #good_movies(ratings_DB)
    #audience_darling(actor_DB, ratings_DB)
    
    #get_common_actors('The Philadelphia Story', 'Rear Window', actor_DB)
    #result=select_where_rating_is(65, '=', False, ratings_DB)
    #result=select_where_rating_is(99,'>',True,ratings_DB)
##    result=select_where_rating_is(28,'<',False,ratings_DB)
##    print result
##    print len(result)
    print get_bacon('Tom Hanks', actor_DB),'tom'
    print get_bacon('Meg Ryan', actor_DB),'meg'
    print get_bacon('Denzel Washington', actor_DB),'Denzel'
    print get_bacon('Angelina Jolie', actor_DB),'Angelina Jolie'
    print get_bacon('Rita Moreno', actor_DB),'Rita Moreno'
    #how to differentiate not exsit in this list, or refer but no connection?
    #print get_common_movie('Kevin Bacon', 'Tom Hanks', actor_DB)
    #print get_common_movie('Kevin Bacon', 'Tom', actor_DB)
    #should return none, or do something
if __name__ == '__main__':
    main()

