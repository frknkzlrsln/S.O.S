# S.O.S

![Image](https://images-eu.ssl-images-amazon.com/images/I/51iNRRbgNoL.png)

Introduction
=================

Although it is not as complex as chess, I present to you this game that requires us to think one step ahead and at the same time entertains us.
No GUI libraries used.
You can easily run it with the Python compiler on your computer. Or you can run it using your computer's terminal screen.

## Table of Contents

- [About Game](#About-Game)
- [Game Rules](#Game-Rules)
- [Example](#Example)
- [License](#License)



### About Game

SOS is paper and pencil game for two or more players. It is similar to [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) and [dots and boxes](https://en.wikipedia.org/wiki/Dots_and_Boxes), but has greater complexity.

SOS , In terms of game theory, it is a zero-sum, sequential game with perfect information.


### Game Rules

- Before play begins, a square grid min 3x3 max 26x26 squares in size is drawn.
- Players take turns to add either an "S" or an "O" to any square, with no requirement to use the same letter each turn.
- The object of the game is for each player to attempt to create the straight sequence S-O-S among connected squares (either diagonally, horizontally, or vertically), and to create as many such sequences as they can.
- If a player succeeds in creating an SOS, that player immediately takes another turn, and continues to do so until no SOS can be created on their turn. Otherwise turns alternate between players after each move
- Once the grid has been filled up, the winner is the player who made the most SOSs
-  If the grid is filled up and the number of SOSs for each player is the same, then the game is a draw.


### Example

We start the game with a 3x3 playground

| A | B | C |  |
| :--: | :--: | :--: | :--: |
|  |  |  | A |
|  |  |  | B |
|  |  |  | C |

Player1 enters 'S'

| A | B | C |  |
| :--: | :--: | :--: | :--: |
|  |  |  | A |
|  |  |  | B |
| S |  |  | C |

Player2 enters 'S'

| A | B | C |  |
| :--: | :--: | :--: | :--: |
|  |  |  | A |
|  |  |  | B |
| S | S |  | C |

Player1 enters 'O'

| A | B | C |  |
| :--: | :--: | :--: | :--: |
|  |  |  | A |
|  | O|  | B |
| S | S |  | C |

Pleyer2 Enters 'S' and getting 1 Point 

| A | B | C |  |
| :--: | :--: | :--: | :--: |
|  | S |  | A |
|  | O|  | B |
| S | S |  | C |

Pleyer2 Enters 'S' and getting 1 more Point 

| A | B | C |  |
| :--: | :--: | :--: | :--: |
|  | S | S | A |
|  | O|  | B |
| S | S |  | C |


Pleyer2 Enters 'S' 

| A | B | C |  |
| :--: | :--: | :--: | :--: |
| S | S | S | A |
|  | O|  | B |
| S | S |  | C |



Pleyer1 Enters 'O' and getting 1 Point

| A | B | C |  |
| :--: | :--: | :--: | :--: |
| S | S | S | A |
| O | O|  | B |
| S | S |  | C |


Pleyer1 Enters 'S' and getting 1 more Point

| A | B | C |  |
| :--: | :--: | :--: | :--: |
| S | S | S | A |
| S | O|  | B |
| S | S | S | C |

Pleyer1 Enters 'S' and getting 1 more Point

| A | B | C |  |
| :--: | :--: | :--: | :--: |
| S | S | S | A |
| S | O| S | B |
| S | S | S | C |


So the last scrore is :

**Player1** : 3 

**Player2** : 2

The Winner is **Player 1**


### License

MIT License

Copyright (c) 2018 Yasin Toy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
