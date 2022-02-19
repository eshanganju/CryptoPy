# Outline

Making a simple blockchain. Friday coding.

# Notes
Startig from a simple ideas

## Keys

-secret key (sk)
	This your personal signature

-public key (pk)
	This is the used to check if somehting has been signed by you


-signing a message
	Sign(message,sk) = Signature

-verification
	Vertify(Message,Signature,pk)=True/False
		Is the message signed using the secret key


Has a message been signed using the secret key (sk)?

-ledger
	Holds the transactions
	Holds the history of transactions
	Each update is linked to the previous state of the ledger

-decentralization
	The ledger is held by each member of the group using it 

-Computational work (Proof of work)
	The ledger trusted the most is the one which has the most "computationa work"

-Crypto hash function
	Input(any msg/file) -> Hash function -> Hash or digest(string of bits))
	It is "infeasible" to compute in the reverse direction
	Proof of work is established by computing what number when appended to the ledger would result in a certain hash 
	Possibly something that looks a certain way (fixed number of leading zeros etc.)

-Block chain
	- block
		- contains the latest ledger
		- proof of work
		- proof of work of previous block
	- chain 
		-link between the current ledger and the previous ledger

-Steps in addition of a new block to the chain
	- Listen - for latest blocks
	- Update - the ledger and compute the proof of work
	- Broadcast - the updated block for other members of the system to listen
	
-block reward
	- Each block creation is rewarded by some money

-conflict resolution
	- Trust the longest block chain - the maximum work
	- In case of tie - wait and select the chain that gets updated

-fradulent block
	- need greater than 50% of the compute power 

## Main ideas
1. Digital signture
2. Ledger is currency
3. Decentralization
4. Proof of work
5. Block chain




----------------------------------------------------------------------------------------
# References

## Websites
- https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
- https://learnmeabitcoin.com/


## Videos
- 3b1br: https://www.youtube.com/watch?v=bBC-nXj3Ng4 
