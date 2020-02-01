import gym
from app.worker.egistic_navigation.global_support import simple_logger


def main():
	env=gym.make('Egistic_Nav_Env:nav_env-v0')
	simple_logger.debug('env.action_space:\n%s',env.action_space)
	# simple_logger.debug('env.action_space:\n%s',env.env)
	simple_logger.debug('env.metadata:\n%s',env.metadata)
	simple_logger.debug('env.observation_space:\n%s',env.observation_space)
	simple_logger.debug('env.reward_range:\n%s',env.reward_range)
	simple_logger.debug('env.spec:\n%s',env.spec)
	simple_logger.debug('env.action_space:\n%s',env.action_space)
	
	# gym.make('gym_foo:foo-v0')
	pass

if __name__=='__main__':
	main()
