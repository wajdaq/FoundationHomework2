import TicTacToe as ttt

def main():

	# Players
	rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
	rlAgent.name = 'RL Agent'

	partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
	partner.name = "Random"

	# Training Session 1
	rlAgent.initTraining(0.8, 0.1, 0.3)
	ttt.train(rlAgent, partner, 45105) #46980


	# Training Session 2 Optional
	# rlAgent.initTraining(0.8, 0.1, 0.3)
	# ttt.train(partner, rlAgent, 45105)

	# max = 1200
	# lst = []
	# for i in range(0,10):
	# 	for j in range(0,10):
	# 		for k in range(0,10):
	# 			rlAgent.initTraining(i/10, j/10, k/10)
	# 			ttt.train(rlAgent, partner, 24052)
	# 			if rlAgent.rating> max:
	# 				print(i,j,k)
	# 				max = rlAgent.rating
	# 				lst = [i/10,j/10,k/10]
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
