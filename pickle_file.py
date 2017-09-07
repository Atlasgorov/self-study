import os
import pickle

var = [1,2,3,['zjg loves zjy'],{13:14}]

os.chdir(r'C:\Users\Atlas_ZJG\Desktop\desk_test')
with open('testing.pkl','wb') as f0:
    pickle.dump(var,f0)

del var
with open('testing.pkl','rb') as f1:
    temp = pickle.load(f1)
print(temp)
