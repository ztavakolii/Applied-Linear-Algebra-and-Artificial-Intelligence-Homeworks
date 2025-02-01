import numpy as np
import math

payoff_table=np.array([[2,3,5,8],[4,1,2,1],[7,0,3,2],[2,3,4,5]])
optimal_path=0

def evaluate_board(path):
    value=0
    global payoff_table
    path=path[::-1]
    i=path[0]
    for k in range(1,len(path)):
        if k % 2 == 1:
            j=path[k]
            value -= payoff_table[i-1][j-1]
        else:
            i=path[k]
            value += payoff_table[i-1][j-1]

    #path=path[::-1]
    return value



def alpha_beta_pruning(max_moves:set,min_moves:set,is_max:bool,benefit:float,path:list): # benefit = opponent 's benefit - min player prunes the tree for max player and max player prunes the tree for min player
    global optimal_path
    number_of_pruned_nodes=0
    if is_max: # max player
        max_benefit=float('-inf')
        count=0

        if len(max_moves) == 0:
            return evaluate_board(path) , 0 , path

        for i in max_moves:
            temp=max_moves.copy()
            count+=1
            temp.remove(i)
            path.insert(0,i)
            value,x,path=alpha_beta_pruning(temp,min_moves,False,max_benefit,path)
            
            number_of_pruned_nodes += x
            if value > max_benefit:
                max_benefit=value
                if len(path) == 8:
                    optimal_path=path.copy()
                if path != []:
                    path=path[1:]
            if max_benefit >= benefit:
                if path != []:
                    path=path[1:]
                return max_benefit , (len(max_moves)-count)*math.factorial(len(max_moves)-1)*math.factorial(len(min_moves)) + number_of_pruned_nodes , path
        if path != []:
            path=path[1:]
        return max_benefit , number_of_pruned_nodes , path
    
    else: # min player
        min_benefit=float('inf')
        count=0

        if len(min_moves) == 0:
            return evaluate_board(path) , 0 , path

        for i in min_moves:
            temp=min_moves.copy()
            count+=1
            temp.remove(i)
            path.insert(0,i)
            value,x,path=alpha_beta_pruning(max_moves,temp,True,min_benefit,path)
            
            number_of_pruned_nodes += x
            if value < min_benefit: 
                min_benefit=value
                if len(path) == 8:
                    optimal_path=path.copy()
                if path != []:
                    path=path[1:]
            if min_benefit <= benefit:
                if path != []:
                    path=path[1:]
                return min_benefit , (len(min_moves)-count)*math.factorial(len(min_moves)-1)*math.factorial(len(max_moves)) + number_of_pruned_nodes , path
        if path != []:
                    path=path[1:]
        return min_benefit, number_of_pruned_nodes , path


max_moves={1,2,3,4}
min_moves={1,2,3,4}
path=[]
max_player_benefit,number_of_pruned_nodes,path=alpha_beta_pruning(max_moves,min_moves,True,float('inf'),path)
path=path[::-1]
print('The benefit of max player is: ',max_player_benefit)
print('Number of pruned nodes is: ',number_of_pruned_nodes)
print('The optimal strategy is:')
optimal_path=optimal_path[::-1]
for i in range(len(optimal_path)):
    if i%2 == 0:
        print('max select column ',optimal_path[i])
    else:
        print('min select column ',optimal_path[i])



