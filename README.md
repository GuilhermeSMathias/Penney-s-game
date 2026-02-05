### The Game
**Penney's game**, also known as **Penney Ante**, named after its inventor *Walter Penney*, is a binary (head/tail) sequence-generating game between two players.

Player A selects a sequence of heads and tails (of length 3 or larger) and shows this sequence to player B. 
 
Player B then selects another sequence of heads and tails of the same length. 
 
Subsequently, a fair coin is tossed until either player A's or player B's sequence appears as a consecutive subsequence of the coin toss outcomes. 
 
The player whose sequence appears first wins.

### Explanation

At first glance, the game seems fair: each coin toss has the same probability of occurring, and all tosses are independent events.  
Because of this, one might assume there is no perfect sequence to beat an opponent… but that assumption would be wrong.

There is a strategy for this game. It relies on playing after your opponent. Once your opponent declares their chosen sequence (assuming a three-sequence game), you can follow a simple algorithm to determine the optimal counter-sequence.

The algorithm works as follows: take the second position of your opponent’s sequence, move it to the first position, flip its value, and then select the first three symbols.

For example, if your opponent chooses "THT", you take the middle symbol ("H"), place it first, flip it to "T", forming "TTHT", and then select the first three symbols. Your resulting sequence is "TTH".  
With this setup, you gain a winning probability of 2/3 (66%) against your opponent.

### The Math

The math behind this strategy is surprisingly simple. Given an ever-growing sequence of equally likely coin flips, some sequences of length N are bound to occur earlier than others.  
By choosing your sequence in relation to your opponent’s, you increase the probability that your sequence appears first.

Let’s look at an example. 

Suppose your opponent chooses "HHH". The optimal response is "THH". Once the coin flips begin, your opponent’s only chance of winning is if the first three flips are all heads.  
Otherwise, the moment another "HHH" sequence starts to form, you would win.

The probability of getting "HHH" on the first three flips is 1/8 (12.5%), while your probability of winning the game is 7/8 (87.5%), which includes every other possible outcome for the increasing sequence.

Suppose the first three flips are:

"HHT"

Neither player wins. At this point, your opponent can no longer win the game as another flip occurs:

"HHTH"

As the sequence continues, "THH" is guaranteed to appear before "HHH". Once a tail appears, forming the pattern "T", any future occurrence of "HHH" would require "THHH", but "THH" would already have appeared first, thus guaranteeing a victory.

For example:

"HHTHTTHTHHH"

Here, "THH" appears after "HHH".

This elegant piece of mathematics is what locks your opponent into a losing game disguised as a fair one.

### Extra

In case of a more detailed explanation of this specific concept, I suggest watching the YouTube video below:

[Penney's Game - Numberphile](https://www.youtube.com/watch?v=Sa9jLWKrX0c)
