# PyChessMaster
PyChessMate: Your ultimate Python chess game. Play against the computer or challenge friends. Improve your skills, customize and learn with ease. Join now!

Welcome to the Chess Game

Firstly we, included all the libraries that are to be used. Math is included for using infinities of both positive and negative for minmax algorithm. Random is used for doing random move from ai and Chess.
Firstly, we included the board of chess and then there are some functions of checkmate, stalemate and draws defined to check wins and draws.

Firstly, we print the board and then a function for playerMove() is defined. In which using while loop if it is allowed move then it is done else a prompt is given to input again.

In the aiMove() alpha and beta are initialized with negative infinity and none respectively now we get a random choice of move out of all the legal moves and push it in the minimax function to get the score and push at the end onto the board.

In the minmax algorithm, firstly we are checking if the game is over then it returns to the evaluation function else if the function is Maximizing then the if condition of our move goes first using alpha else the enemy bot does the move using beta and returns the score at the end.

In the evaluate function if checkmate, stalemate or draw happens the function returns else we give the pieces values and loop it. In the loop if the piece can be placed on board then the score updates.

In the main, while the game is not over firstly the player move happens and then the ai move and check for the validations concurrently.

