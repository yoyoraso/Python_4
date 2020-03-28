Python_4
========
1--given two points repersented as x1, y1, x2, y2
return float distance, between them considering the fllowing the distance equation
consider dividing a string into two halves
case1: the length is even, the front and  back halves are the same length
case 2:
the length is odd, we'll say the extra char goes in the front half,
e.g
abcde', the front half is 'abc', the back half'de.

---------------------------------------------------------------------------------------------
2--given 2 strings, a and b, return a string of the form:
(a-front + b-front) + (a-back + b-back)

---------------------------------------------------------------------------------------------
3--program takes command line arg this arg is the name of a txt.file
the program reads all the txt and split them and calc the 20 common used word
file name: popular_wods.txt
hint, my_str.split()

----------------------------------------------------------------------------------------------
4--guess game
1- generate a random number and
2- give only 10 tries for the user to guess that number
3- get user input and compare it with the random number.
4- display a hint message to the user in case the user number is smaller or bigger of the random number
5- if user type a number out of range(100),
display a message that is not allowed and don't count this a s a try
6- in case the user entered a correct number within the 10 tries, display a congratulations message and let your application guess another random number
with the reamin number of traies.
* if user finish his all tries, display a message to ask hom
if he want to play a gain or not.

* Next time the user open the game, he receives a welcome message tells him the nimebr of
games he played, how many times he won and how many he lost,
