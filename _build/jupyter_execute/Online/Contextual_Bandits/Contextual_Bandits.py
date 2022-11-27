#!/usr/bin/env python
# coding: utf-8

# # Contextual Bandits
# 
# 
# disjoint linear models...finite arm
# 
# 
# The bandit problems have received increasing attention recently and have been widely applied to areas such as clinical trials [1], finance [2], and recommendation systems [3], among others. The most classical version of it is the multi-armed bandit (MAB) [4], where an agent will sequentially select an item (arm) from a few and then receive a random reward for the item selected. Since the reward distributions are unknown in most real applications, the central task of a MAB algorithm is to learn the distributions from feedback received and find the optimal item to maximize the cumulative rewards or, equivalently, to minimize the cumulative regret. This chapter focuses on the MAB problems by illustrating a group of classical algorithms to tackle the well-known exploration-exploitation trade-off.
# 
# ## Problem Setting
# Let $T$ be the total number of rounds, and $K$ be the number of arms (actions to be selected). The agent would choose one arm at each round $t = 1, \dots, T$. Then the agent will receive the corresponding stochastic reward $R_t$ from the environment. Denote the expected reward for each arm $i$ as $r_{i}$. Since, in most real applications, such a reward distribution is always unknown, the agent needs to learn the reward distribution from feedback received. Overall, the objective is to find a bandit algorithm to maximize the cumulative Reward $\sum_{t=1}^{T}R_{t}$.
# 
# MAB has been extensively studied and widely applied to different areas, including healthcare, recommender system, and finance, to name a few. See [4] for a detailed review of MAB and [5] for a survey of practical applications. Among them, the ultimate goal of a learning algorithm is always to strike a good balance between exploration (try an unfamiliar action to learn more information) and exploitation (take the action that has the highest estimated reward so far) so as to maximize the cumulative reward. In the following, we will briefly illustrate three popular and classical categories of algorithms to handle the exploration-exploitation trade-off: i) $\epsilon$-greedy, ii) Upper Confidence Bound (UCB), and iii) Thompson Sampling (TS). 

# ## Real Data
# **1. MovieLens**
# 
# Movie Lens is a website that helps users find the movies they like and where they will rate the recommended movies. [MovieLens 1M dataset](https://grouplens.org/datasets/movielens/1m/) is a dataset including the observations collected in an online movie recommendation experiment and is widely used to generate data for online bandit simulation studies. The goal of the simulation studies below is to learn the reward distribution of different movie genres and hence to recommend the optimal movie genres to the users to optimize the cumulative user satisfaction. In other words, every time a user visits the website, the agent will recommend a movie genre ($A_t$) to the user, and then the user will give a rating ($R_t$) to the genre recommended. We assume that users' satisfaction is fully reflected through the ratings. Therefore, the ultimate goal of the bandit algorithms is to optimize the cumulative ratings received by finding and recommending the optimal movie genre that will receive the highest rating. In this chapter, we mainly focus on the top 5 Genres, including 
# 
# - **Comedy**: $a=0$,
# - **Drama**: $a=1$,
# - **Action**: $a=2$,
# - **Thriller**: $a=3$,
# - **Sci-Fi**: $a=4$.
# 
# Therefore, $K=5$. For each user, feature information, including age, gender and occupation, are available:
# 
# - **age**: numerical, from 18 to 56,
# - **gender**: binary, =1 if male,
# - **college/grad student**: binary, =1 if a college/grad student,
# - **executive/managerial**: binary, =1 if a executive/managerial,
# - **academic/educator**: binary, =1 if an academic/educator,
# - **technician/engineer**: binary, =1 if a technician/engineer,
# - **writer**: if a writer, then all the previous occupation-related variables = 0 (baseline).
# 
# Furthermore, there are two different types of the reward $R_t$:
# 
# - **Gaussian Bandit**: $R_t$ is a numerical variable, taking the value of $\{1,2,3,4,5\}$, where 1 is the least satisfied and 5 is the most satisfied.
# - **Bernoulli Bandit**: $R_t$ is a binary variable, =1 if the rating is higher than 3.
# 
# In the following, we evaluated the empirical performance of the supported algorithms on the MovieLens dataset under either the Gaussian bandit or Bernoulli bandit settings.

# ## Simulation 1: Gaussian Bandit
# We repeat the experiment over **100** random seeds, with $T = 100$.

# ## Simulation 1: Bernoulli Bandit
# We repeat the experiment over **100** random seeds, with $T = 100$.

# ## Reference
# [1] Durand, A., Achilleos, C., Iacovides, D., Strati, K., Mitsis, G. D., and Pineau, J. (2018). Contextual bandits for adapting treatment in a mouse model of de novo carcinogenesis. In Machine learning for healthcare conference, pages 67–82. PMLR.
# 
# [2] Shen, W., Wang, J., Jiang, Y.-G., and Zha, H. (2015). Portfolio choices with orthogonal bandit learning. In Twenty-fourth international joint conference on artificial intelligence.
# 
# [3] Zhou, Q., Zhang, X., Xu, J., and Liang, B. (2017). Large-scale bandit approaches for recommender systems. In International Conference on Neural Information Processing, pages 811–821. Springer.
# 
# [4] Slivkins, A. (2019). Introduction to multi-armed bandits. arXiv preprint arXiv:1904.07272.
# 
# [5] Bouneffouf, D. and Rish, I. (2019). A survey on practical applications of multi-armed and contextual bandits. arXiv preprint arXiv:1904.10040.
# 
# [6] Sutton, R. S. and Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press
# 
# [7] Auer, P., Cesa-Bianchi, N., and Fischer, P. (2002). Finite-time analysis of the multiarmed bandit problem. Machine learning, 47(2):235–256.
# 
# [8] Russo, D., Van Roy, B., Kazerouni, A., Osband, I., and Wen, Z. (2017). A tutorial on thompson sampling. arXiv preprint arXiv:1707.0203
# 
# [9] Lattimore, T. and Szepesv´ari, C. (2020). Bandit algorithms. Cambridge University Press.
# 
# [10] Li, L., Chu, W., Langford, J., and Schapire, R. E. (2010). A contextual-bandit approach to personalized news article recommendation. In Proceedings of the 19th international conference on World wide web, pages 661–670
# 
# [11] Li, L., Lu, Y., and Zhou, D. (2017). Provably optimal algorithms for generalized linear contextual bandits. In International Conference on Machine Learning, pages 2071–2080. PMLR.
# 
# [12] Kveton, B., Zaheer, M., Szepesvari, C., Li, L., Ghavamzadeh, M., and Boutilier, C. (2020). Randomized exploration in generalized linear bandits. In International Conference on Artificial Intelligence and Statistics, pages 2066–2076. PMLR.
# 
# [13] Agrawal, S. and Goyal, N. (2013). Thompson sampling for contextual bandits with linear payoffs. In International conference on machine learning, pages 127–135. PMLR.
# 

# In[ ]:




