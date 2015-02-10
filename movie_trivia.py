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
        #movieInfo[actor] = set(movies)
        movieInfo[actor] = movies
        #should we change this, so we can further edit and append?
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
    ratings_Db[movie] = ratings
    #what if duplicate?
def delete_movie(movie, movie_Db, ratings_Db):
    del ratings_Db[movie]
    movies_of_all_actors = movie_Db.values()
    for movies_list in movies_of_all_actors:
        if movie in movies_list:
            movies_list.remove(movie)
        #problems here!!

def select_where_actor_is(actorName, movie_Db):
    #return movie_Db(actorName)
    return movie_Db[actorName]
def select_where_movie_is(movieName, movie_Db):
    all_actors_list = movie_Db.keys()
    actors_list = []
    for actor in all_actors_list[0:]:
        if movieName in movie_Db[actor]:
            actors_list.append(actor)
            #the last item cannot be got, because the value missing in first movie_Db!!
    return actors_list

def select_where_rating_is(targeted_rating, comparison, is_critic, ratings_Db):
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
    
        
   
#USER QUESTION!!!!!!!!!!

#def get_co_actors(actorName, moviedb):




def main():
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    # PLEASE TAKE THE NEXT FEW PRINTING LINES OUT
    # ONCE YOU HAVE CONFIRMED THIS WORKS
##    print actor_DB.keys()
##    print ratings_DB.keys()
##    print '\n'
##    print actor_DB['Humphrey Bogart']
##    print ratings_DB['Rambo']
##    #name=select_where_movie_is('Mrs. Miniver', ratings_DB)
##    #print name
##    print ratings_DB['The Avengers']
##    print 'The Avengers' in actor_DB.values()
##    print 'MASH' in actor_DB.values()[0]
##    #print 'The Avengers' in ratings_DB
##    print actor_DB.values()
##    print len(actor_DB)
##    print 'Walter Pidgeon' in actor_DB
##    
##    print len(ratings_DB)
    #result=select_where_rating_is(65, '=', False, ratings_DB)
    #result=select_where_rating_is(99,'>',True,ratings_DB)
##    result=select_where_rating_is(28,'<',False,ratings_DB)
##    print result
##    print len(result)
    
if __name__ == '__main__':
    main()

