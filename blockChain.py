"""Creating a simple blockchain

Refs: 
	https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
	https://bitcoin.org/bitcoin.pdf
	http://www.weidai.com/bmoney.txt
	3B1Br Bitcoin: https://www.youtube.com/watch?v=bBC-nXj3Ng4
	

"""

import hashlib
import json
from time import time


class BlockChain(object):


	def __init__(self):

		# The chain in which the blocks will be added
		self.chain=[]

		# The pending transactions on the blockchain
		self.pending_transactions=[]

		# When new blocks will be added to the chain
		self.new_block(previous_hash="itiswhatitis47906",proof=100)


	def new_block(self, proof, previous_hash=None):

		# Json block variable
		block={
			'index':len(self.chain) + 1,
			'timestamp':time(),
			'transactions':self.pending_transactions,
			'proof':proof,
			'previous_hash':previous_hash or self.hash( self.chain[ -1 ] ),
		}

		self.pending_transactions=[]
		self.chain.append(block)

		return block

	@property
	def last_block(self):
		return self.chain[-1]


	def new_transaction(self, sender, recipient, amount):
		transaction={
			'sender':sender,
			'recipient':recipient,
			'amount':amount
		}

		self.pending_transactions.append(transaction)
		return self.last_block['index'] + 1
