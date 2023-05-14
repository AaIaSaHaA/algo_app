from django.shortcuts import render
from .models import Game
#from access.code import identify_algorithm, get_details

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
    #print('lists: ',algorithms_features)
    for feature in algorithms_features:
        if feature_list == feature:
            #print("here one list",feature_map[str(feature)])
            return feature_map[str(feature)]
    return None

def get_details(algorithm):
    return a_desc_map.get(algorithm, "")

def note(request):
    return render(request,'access/note.html')

def algorithm_guess(request):
    preprocess()
    if request.method == 'POST':
        ml = request.POST.get('ml')
        dl = request.POST.get('dl')
        dt = request.POST.get('dt')
        rf = request.POST.get('rf')
        svm = request.POST.get('svm')
        linear = request.POST.get('linear')
        logistic = request.POST.get('logistic')
        rein = request.POST.get('rein')
        knn = request.POST.get('knn')
        rnn = request.POST.get('rnn')
        lstm = request.POST.get('lstm')
        trans = request.POST.get('trans')
        gan = request.POST.get('gan')
        cnn = request.POST.get('cnn')

        ml = ml if ml is not None else '0'
        dt = dt if dt is not None else '0'
        rf = rf if rf is not None else '0'
        svm = svm if svm is not None else '0'
        linear = linear if linear is not None else '0'
        logistic = logistic if logistic is not None else '0'
        rein = rein if rein is not None else '0'
        knn = knn if knn is not None else '0'
        dl = dl if dl is not None else '0'
        rnn = rnn if rnn is not None else '0'
        lstm = lstm if lstm is not None else '0'
        trans = trans if trans is not None else '0'
        gan = gan if gan is not None else '0'
        cnn = cnn if cnn is not None else '0'

        #Send the data to DB (models)
        v_game = Game(ml=ml, dt=dt, rf=rf, svm=svm, linear=linear, logistic=logistic, rein=rein, knn=knn, dl=dl, rnn=rnn, lstm=lstm, trans=trans, gan=gan, cnn=cnn)
        v_game.save()
        if ml == '1':
            algorithm = identify_algorithm(ml, dt, rf, svm, linear, logistic, rein, knn)
        elif ml == '0':
            if dl == '1':
                algorithm = identify_algorithm(dl, rnn, lstm, trans, gan, cnn)
            else:
                algorithm = None
        else:
            algorithm = None
        
        if algorithm is not None:
            algorithm_details = get_details(algorithm)
            return render(request, 'access/result.html', {'algorithm': algorithm, 'algorithm_details': algorithm_details})
        else:
            algorithm_details = get_details(algorithm)
            return render(request, 'access/error.html')
    
    return render(request, 'access/algorithm_guess.html')

def result(request):
    return render(request,'access/result.html')

def error(request):
    return render(request,'access/error.html')