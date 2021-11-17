from node import node

def process_nodes(node_list):
    key_list = node_list.keys()
    for key in key_list:
        target_node = node_list[key]
        target_node.node_type()

def bellman(target_node, nl, df):
    score = cal_score(target_node, nl)
    return target_node.reward + df * score

def cal_score(target_node, nl):
    if target_node.isChance:
        total_sum = 0
        for count, edge in enumerate(target_node.edges):
            total_sum += target_node.prob[count]*nl[edge].value
        return total_sum
    if target_node.isDecision:
        total_sum = 0
        main_prob = target_node.prob[0]
        rem_prob = (1-main_prob)/(len(target_node.edges) - 1)
        policy = target_node.cur_policy
        for _, edge in enumerate(target_node.edges):
            if edge == policy:
                total_sum+= main_prob*nl[edge].value
            else:
                total_sum+= rem_prob*nl[edge].value
            # print(total_sum, edge, nl[edge].value)
        # print(target_node.name, main_prob, rem_prob, policy, total_sum)
        return total_sum
    return 0

def cal_policy(target_node, nl, arg_min):
    main_prob = target_node.prob[0]
    rem_prob = (1-main_prob)/(len(target_node.edges) - 1)
    cur_value = target_node.value
    for _, main_edge in enumerate(target_node.edges):
        total_sum = 0
        for side_edge in target_node.edges:
            if main_edge == side_edge:
                total_sum+= main_prob*nl[side_edge].value
            else:
                total_sum+= rem_prob*nl[side_edge].value
        # print("=> ", main_edge, cur_value, total_sum, nl[main_edge].value)
        if arg_min and total_sum < cur_value:
            target_node.cur_policy = main_edge
            cur_value = total_sum
        elif total_sum > cur_value:
            target_node.cur_policy = main_edge
            cur_value = total_sum
    # print(target_node.name, cur_value)
    return target_node.cur_policy

def markov_solver(node_list, df, arg_min, tol, arg_iter):
    for key in node_list.keys():
        if node_list[key].isTerminal == False:
            node_list[key].cur_policy = node_list[key].edges[0]

    while True:
        # Value Iteration Loop
        for _ in range(arg_iter):
            value_flag = value_iteration(node_list, tol, df)
            if not value_flag:
                break

        # Policy Iteration Loop
        policy_flag = policy_iteration(node_list, arg_min)
        if not policy_flag:
            break
            
def value_iteration(node_list, tol, df):
    value_flag = False
    for key in node_list.keys():
        new_value = bellman(node_list[key], node_list, df)
        if (abs(new_value - node_list[key].value) > tol):
            value_flag = True
        node_list[key].value = new_value
    return value_flag    

def policy_iteration(node_list, arg_min):
    policy_flag = False
    for key in node_list.keys():
        target_node = node_list[key]
        if target_node.isDecision:
            old_policy = target_node.cur_policy 
            new_policy = cal_policy(target_node, node_list, arg_min)
            if old_policy != new_policy:
                policy_flag = True
            target_node.cur_policy = new_policy
    return policy_flag
    