import collections 
from sklearn.preprocessing import normalize

def get_human_action_vectors(cdata, k_classes):
    human_action_vectors = np.zeros(shape=(len(cdata["users"]), k_classes))
    for i, user in enumerate(cdata["users"]):
        cur_dict = dict(collections.Counter(cdata['user_data'][user]['y']))

        for elem in cur_dict:
            cur_dict[elem] = cur_dict[elem]/len(cdata['user_data'][user]['y'])
        for key in cur_dict.keys():
            human_action_vectors[i, int(key)] = cur_dict[key]
        
    #human_action_vectors = np.exp(human_action_vectors) / np.exp(human_action_vectors).sum(1).reshape(-1, 1)
    human_action_vectors = normalize(human_action_vectors, norm='l2')
    
    return human_action_vectors

def get_human_sim_matrix(human_action_vectors):
    matrix = human_action_vectors @ human_action_vectors.T
    min_matrix, max_matrix = matrix.min(), matrix.max()
    return matrix
