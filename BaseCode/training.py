import TicTacToe as ttt

def main():

	# Players
	rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
	rlAgent.name = 'RL Agent'

	partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
	partner.name = "Random"

	# Training Session 1
	rlAgent.initTraining(0.6, 0.1, 0.1)
	ttt.train(rlAgent, partner, 47980) #46980, Best result 25105 - 1292, 45105 - , 47980 - 1280


	# Training Session 2 Optional
	# rlAgent.initTraining(0.6, 0.1, 0.2)
	# ttt.train(partner, rlAgent, 25105)#45105
	# #
	# max = 1200
	# lst = []
	# for i in range(0,10):
	# 	for j in range(0,10):
	# 		for k in range(0,10):
	# 			rlAgent.initTraining(i/10, j/10, k/10)
	# 			ttt.train(rlAgent, partner, 100)
	# 			if rlAgent.valueOfState('X') > max:
	# 				print(i,j,k)
	# 				max = rlAgent.rating
	# 				lst = [i/10,j/10,k/10]
	# print(lst)
	# This method has to be called after all the training sessions are 
	# done
	rlAgent.save()
	
	# Evaluation
	rlAgent.setMode(ttt.PLAYING_MODE)
	tournament = ttt.Tournament()
	tournament.start(rlAgent, partner, 5)
	tournament.start(partner, rlAgent, 5)
	tournament.printStats([rlAgent, partner])



main()
