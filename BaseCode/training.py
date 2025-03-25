import TicTacToe as ttt
import copy
def main():

	# Players
	rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
	rlAgent.name = 'RL Agent'

	partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
	partner.name = "Random"

	# Training Session 1
	rlAgent.initTraining(0.8, 0.1, 0.2)
	ttt.train(rlAgent, partner, 47105) #46980, Best result 25105 - 1292, 45105 - , 47980 - 1280
	#
	#
	# Training Session 2 Optional
	rlAgent.initTraining(0.8, 0.1, 0.2)
	ttt.train(partner, rlAgent, 47105)#45105
	# # #
	#
	# for i in range(20):
	# 	rlAgent.initTraining(0.7 , 0.1, 0.7)
	# 	ttt.train(rlAgent, partner, 45105)
	# 	rlAgent.initTraining(0.7, 0.1, 0.7)
	# 	ttt.train(partner, rlAgent, 45105)

	# rlAgent.initTraining(0.9, 0.1, 0.9)
	# ttt.train(rlAgent, partner, 45105)
	# This method has to be called after all the training sessions are
	# done
	rlAgent.save()
	#
	# Evaluation
	rlAgent.setMode(ttt.PLAYING_MODE)
	tournament = ttt.Tournament()
	tournament.start(rlAgent, partner, 5)
	tournament.start(partner, rlAgent, 5)
	tournament.printStats([rlAgent, partner])


main()
