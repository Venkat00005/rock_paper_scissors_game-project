# rock_paper_scissors_game-project
This is a simple rock, paper, scissors game created using python.
It is a game between computer and user.

RULES:

1. In rock-paper/paper-rock condition: paper will get a point
2. In paper-scissors/scissors-paper condition: scissors will get a point
3. In scissors-rock/rock-scissors condition: rock will get a point
4. If both the choices are equal then no one will get point.


1.1 I counted computer score in "computer" variable and user score in "user" variable.

2. first it will take user name as input and store it in "user_name" variable.

3. Then took user choice (rock,paper,scissors) and stored in "user_choice" variable.

4. Used random module and random.shuffle() to select computer choice randomly.

5. computer select it's choice from the list created with "computer_choice" variable with rock,paper and scissors as list elements.

6. I used while loop to repeat the choice selection process between user and computer till, anyone of them wins.

6. Then used if, elif and else conditions to check and give score to the computer or user.

7. In the Tie situation, I used the "continue" keyword to skip it and in this situation computer or user will get 0 points.

8. If user or computer scores 3 points , then while loop will breaks.

9. Used if,else to declare winner.

10. At last, we can change the points to win from 3 to any other number by replacing 3 from while loop and winner deciding block.



