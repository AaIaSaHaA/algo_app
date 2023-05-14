algorithms_list = []
algorithms_features = []
feature_map = {}
a_desc_map = {}
a_implementation_map = {}

def preprocess():
    global algorithms_list, algorithms_features, feature_map, a_desc_map, a_implementation_map
    algorithms = open("access/algorithms.txt")
    algorithms_t = algorithms.read()
    algorithms_list = algorithms_t.split("\n")
    algorithms.close()
    
    for algo in algorithms_list:
        algorithm_s_file = open("access/Algorithm feature/" + algo + ".txt")
        algorithm_s_data = algorithm_s_file.read()
        s_list = algorithm_s_data.split("\n")
        algorithms_features.append(s_list)
        feature_map[str(s_list)] = algo
        algorithm_s_file.close()
        
        algorithm_s_file = open("access/Algorithm description/" + algo + ".txt")
        algorithm_s_data = algorithm_s_file.read()
        a_desc_map[algo] = algorithm_s_data
        algorithm_s_file.close()

def identify_algorithm(*arguments):
    feature_list = list(arguments)
    for feature in algorithms_features:
        if feature_list == feature:
            return feature_map[str(feature)]
    return None

def get_details(algorithm):
    return a_desc_map.get(algorithm, "")

def if_not_matched(algorithm):
    print("")
    id_algorithm = algorithm
    algorithm_details = get_details(id_algorithm)
    print("")
    print("The most probable disease that you have is %s\n" % id_algorithm)
    print("A short description of the disease is given below:\n")
    print(algorithm_details + "\n")

def main():
    
    preprocess()

    print("")
    print("Hi! I am ALGO, I am here to guess what Algorithm you think of.")
    print("For that, you'll have to answer a few questions about the algorithm")
    print("By entering the number of the answer, either 0 or 1\n")  
    
    ml= input("Is it a Machine Learning algorithm?")
    if ml == "1":
            dt = input("Does it split the data into smaller subsets based on certain criteria? ")
            rf = input("Does it combine multiple decision trees to make predictions? ")
            svm = input("Does it find the optimal hyperplane that separates the data into different classes? ")
            linear = input("Does it fit a line to a set of data points to make predictions? ")
            logistic = input("Does it use a sigmoid function to map the output to the range [0,1]? ")
            rein = input("Does it learn from experience through a system of rewards and punishments? ")
            knn = input("Does it classify data points based on their proximity to other data points? ")
            algorithm = identify_algorithm(ml,dt, rf, svm, linear, logistic,rein,knn)
            print("")
            print("The most probable algorithm that you think of is %s\n" % algorithm)
            algorithm_details = get_details(algorithm)
            print("Algorithm Details:")
            print(algorithm_details)

        
    else:
        dl = input("Is it a Deep Learning algorithm?")
        if dl == "1":    
            rnn = input("Does it use a hidden state to represent the network's memory? ")
            lstm = input("Does it have a cell state that can store information over long periods of time? ")
            trans = input("Does it use self-attention to model dependencies between input and output sequences? ")
            gan = input("Does it use two neural networks, a generator and a discriminator, to learn a generative model of the data? ")
            cnn = input("Does it commonly used in image or video processing? ")
            algorithm = identify_algorithm(dl,rnn, lstm, trans,gan, cnn)
            print("")
            print("The most probable algorithm that you think of is %s\n" % algorithm)
            algorithm_details = get_details(algorithm)
            print("Algorithm Details:")
            print(algorithm_details)


if __name__ == "__main__":
    main()
