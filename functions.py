import numpy as np

#Усредненное значение параметров
def mean_mfcc(cell):
    return np.mean(cell)


#Дисперсия
def dispersion(cell):
    c = cell
    M_x2 = (mean_mfcc(c))**2
    Mx2 =  mean_mfcc(c**2)
    D = Mx2 - M_x2
    return D


def create_params(mfcc,size,m_mean = False,m_dispersion = False):
    param = np.zeros([size,size])
    
    if m_mean:
        for i in range(size):
            param[0,i]= mean_mfcc(mfcc[:,i])
            
    if m_dispersion: 
        for i in range(size):
            param[0,i]= dispersion(mfcc[:,i])
        
    return param[0]


#Нормализация кепстральных коэффициентов
def cepnorm(block):
    #TODO: just do it
    b = block
    return b-sum(b)/len(b)


#Кепстральное взвешивание
def cepweight(block):
    #TODO: just do it
    b = block
    cepnorm(b)
    numcep = len(b)-1
    b[1:] = [(1 + (numcep/2)*np.sin((np.pi*n)/numcep))*b[n] for n in range(1,numcep+1)]
    return b

#Вычисление производных

def Derivative(mfcc,fDer = False, sDer = False):
    _mfcc = mfcc
    
    if fDer:
       # fd = [firstDerivative(_mfcc[i]) for i in range(_mfcc.shape[0])]
      #  f_der = fd[1:,:]
        return ([firstDerivative(_mfcc[i]) for i in range(_mfcc.shape[0])])[:,1:]
    
    if sDer:
        sd = [secondDerivative(_mfcc[i]) for i in range (_mfcc.shape[1])]
        s_der = sd[:,1:]
        return s_der

#Первая производная
def firstDerivative(_block):
    d1 = _block
  #  d1[1:]= [d1[i]-d1[i-1] for i in range(1,len(d1))]
    return  [d1[i]-d1[i-1] for i in range(1,len(d1))]


#Вторая производная
def secondDerivative(_block):
    d2 = _block
    #firstDerivative(d2)
    #firstDerivative(d2)[1:-1]= [firstDerivative(d2)[i-1]-2*firstDerivative(d2)[i]+firstDerivative(d2)[i+1] for i in range(1,len(d2)-1)]
    return [firstDerivative(d2)[i-1]-2*firstDerivative(d2)[i]+firstDerivative(d2)[i+1] for i in range(1,len(d2)-1)]
    

