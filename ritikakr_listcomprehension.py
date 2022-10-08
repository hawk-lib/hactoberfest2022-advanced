listnum = [[5,6,7,'C#'], ['C++',2,3]]
 
flatten_list = [ele for sublist in listnum for ele in sublist]
 
print('flatten list =',flatten_list)
