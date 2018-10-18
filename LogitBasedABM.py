#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:40:08 2018

@author: lejoflores
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt

# =============================================================================
# 
# x = np.linspace(-20.0,20.0,num=100)
# 
# alpha1 = 1.0
# alpha2 = 0.2
# alpha3 = 1.8
# 
# y1 = special.expit(alpha1*x)
# y2 = special.expit(alpha2*x)
# y3 = special.expit(alpha3*x)
# 
# plt.figure(figsize=(10,8))
# plt.plot(x,y1,label=r'$\alpha =$ '+str(alpha1))
# plt.plot(x,y2,label=r'$\alpha =$ '+str(alpha2))
# plt.plot(x,y3,label=r'$\alpha =$ '+str(alpha3))
# plt.legend()
# plt.show()
# =============================================================================


Nt = 20

AgeInit = 45.0
DistFromCityInit = 20.0
OnFIInit = 45000.0
OffFIInit = 20000.0

OnFI_agr = 0.03
OffFI_agr = 0.05

FarmerAge = np.zeros((Nt,1))
FarmerDistToCity = np.zeros((Nt,1))
FarmerOnFarmInc = np.zeros((Nt,1))
FarmerOffFarmInc = np.zeros((Nt,1))

class Farmer:
    def __init__(self, Age, DistFromCity, OnFarmIncome, OffFarmIncome):
        self.Age = Age
        self.DistFromCity = DistFromCity
        self.OnFarmIncome = OnFarmIncome
        self.OffFarmIncome = OffFarmIncome

    def UpdateAge(self):
        self.Age += 1
        
    def UpdateDistFromCity(self,dx):
        self.DistFromCity += dx
    
    def UpdateOnFarmIncome(self,loc=0.0,scale=1.0):
        self.OnFarmIncome *= scale
        self.OnFarmIncome += loc

    def UpdateOffFarmIncome(self,loc=0.0,scale=1.0):
        self.OffFarmIncome *= scale
        self.OffFarmIncome += loc
        
        
myF = Farmer(AgeInit, DistFromCityInit, OnFIInit, OffFIInit)

for t in np.arange(Nt,dtype=int):
    

    DeltaDistToCity = ((-0.1 - -0.2)*np.random.random() - 0.2)
    
    OnFI_gr = 1.0 + OnFI_agr*((2.0 - -1.0)*np.random.random() + -1.0)    

    OffFI_gr = 1.0 + OffFI_agr*((2.0 - -1.0)*np.random.random() + -1.0)

    myF.UpdateAge()
    myF.UpdateDistFromCity(DeltaDistToCity)
    myF.UpdateOnFarmIncome(scale=OnFI_gr)
    myF.UpdateOffFarmIncome(scale=OffFI_gr)
    
    
    FarmerAge[t] = myF.Age
    FarmerDistToCity[t] = myF.DistFromCity
    FarmerOnFarmInc[t] = myF.OnFarmIncome
    FarmerOffFarmInc[t] = myF.OffFarmIncome

    
plt.figure(figsize=(10,12))
plt.subplot(3,1,1)
plt.plot(np.arange(Nt),FarmerAge)
plt.title('Farmer Age [years]')
plt.subplot(3,1,2)
plt.plot(np.arange(Nt),FarmerDistToCity)
plt.title('Farm Distance from City [km]')
plt.subplot(3,1,3)
plt.plot(np.arange(Nt),FarmerOnFarmInc,label='On Farm Income')
plt.plot(np.arange(Nt),FarmerOffFarmInc,label='Off Farm Income')
plt.ylim([0,80000])
plt.title('Farmer Income [$]')
plt.legend()

    

