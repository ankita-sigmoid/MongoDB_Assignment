# MongoDB_Assignment
By **Ankita Priya**

## Purpose of this repository
It consists of MongoDB Assignments assigned @ Sigmoid on week 3 of training as a Data Engineer.

## Tech stack used 
- Python version: 3.10.1
- IDE: PyCharm
- MongoDB shell version: v4.4.11
- GUI tool: MongoDB Compass

## Questions

Tasks -

Q1. Create a Python application to connect to MongoDB.


Q2. Bulk load the JSON files in the individual MongoDB collections using Python. MongoDB collections -

  a. comments
  
  b. movies
  
  c. theaters
  
  d. users
  
  ```
  for filename in for filename in ~/Downloads//sample_mflix/*; do mongoimport --db mflix3 --file $filename; done 
  ```

Q3. Create Python methods and MongoDB queries to insert new comments, movies, theaters, and users into respective MongoDB collections.


Q4. Create Python methods and MongoDB queries to support the below operations -

  a. comments collection
  
    i. Find top 10 users who made the maximum number of comments
    
    ii. Find top 10 movies with most comments
    
    iii. Given a year find the total number of comments created each month in that year


  b. movies collection
  
    i. Find top `N` movies - 
    
      1. with the highest IMDB rating
      
      2. with the highest IMDB rating in a given year
      
      3. with highest IMDB rating with number of votes > 1000
      
      4. with title matching a given pattern sorted by highest tomatoes ratings
      
      
    ii. Find top `N` directors -
    
      1. who created the maximum number of movies
      
      2. who created the maximum number of movies in a given year
      
      3. who created the maximum number of movies for a given genre
      

    iii. Find top `N` actors - 
    
      1. who starred in the maximum number of movies
      
      2. who starred in the maximum number of movies in a given year
      
      3. who starred in the maximum number of movies for a given genre
      

    iv. Find top `N` movies for each genre with the highest IMDB rating
    

  c. theatre collection
  
    i. Top 10 cities with the maximum number of theatres
    
    ii. top 10 theatres nearby given coordinates
