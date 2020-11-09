# Sparse Arrays

### 1. Problem
There is a collection of N strings ( There can be multiple occurences of a particular string ). There are also Q queries. For each query, you are given a string, and you need to find out how many times this string occurs in the given collection of N strings.Return an dict/list of the results. 

### 1.1 Example
#### Sample Input
|Array strings| ||||
|--| ------ | ------ |---|--|
|--|aba|baba|aba|xzxb|

|Array queries| |||
|--| ------ | ------ |---|
|--|aba| xzxb | ab |
#### Sample Output
|output|
|--|
|{'aba': 2, 'xzxb': 1, 'ab': 0}|
#### Explanation
Here, “aba” occurs twice, in the first and third string. The string “xzxb” occurs once in the fourth string, and “ab” does not occur at all.

### 1.2 Original problem & more details 
[Please click here](https://www.hackerrank.com/challenges/sparse-arrays/problem)
### 1.3 Maison du Monde problem & details
Please refer to the document:
📦mdmTest
  ┣ 📂doc_maison_du_monde
 ┃ ┗ 📜doc_test_technique_mdm.pdf

## 2. Solution 
### 2.1 Solution of Original problem
Find it here :
📦mdmTest
 ┣ 📂sparseArraysHackerrankSolution
 ┃ ┣ 📜readme.txt
 ┃ ┗ 📜sparseArraysHackerrankSolution.py
To run sparseArraysHackerrankSolution.py. Make sure to login to hackerrank [click here](https://www.hackerrank.com/challenges/sparse-arrays/problem) and copy/paste the code on the platform & run it.

### 2.2 Solution of Maison du Monde (mdm) problem
The solution provided in a tree structure :
📦mdmTest
 ┣ 📜main.py
 ┣ 📜sparseArray.py
 ┗ 📜strings.txt
Where sparseArray.py is a python module that main.py uses to solve the mdm problem, and strings.txt provide collection of N strings.

To run a code:
Let's take the example 3 of hackerrank [here](https://www.hackerrank.com/challenges/sparse-arrays/problem) for example you have 
>* collection of Queries : abcde  sdaklfj  asdjf  na  basdn
>* collection of Strings : strings.txt

You need to run the following commands in your terminal/cmd:
```sh
$ python main.py abcde sdaklfj asdjf na basdn
```
As an output you'll get a dict like this:
> resDict =  {'abcde': 1, 'sdaklfj': 3, 'asdjf': 4, 'na': 3, 'basdn': 2}
### 2.2.1 Docker containerization of mdmTest
Containerization of mdmTest see Dockerfile:
📦mdmTest
 ┣ 📜Dockerfile
Please find the Docker image of mdmTest on dockerHub [here](https://hub.docker.com/r/ocanis/mdmtest_do).

To run it:
* make sure you pull the docker image to your env
```sh
$ docker pull ocanis/mdmtest_do
```
* then run it
```sh
$ docker run ocanis/mdmtest_do:mdmtest abcde sdaklfj asdjf na basdn
```
You will get the same result as in part 2.2
## 3. SQL
Here you can find SQL queries 
📦mdmTest
┣ 📂sql
 ┃ ┗ 📜requete_sql.txt


License
----

MIT
