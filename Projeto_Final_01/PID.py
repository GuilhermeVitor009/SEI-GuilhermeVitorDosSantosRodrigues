import numpy as np
import control
import pygame
from pygame.locals import *
from control.matlab import *
from game import *

import sys
# Vetor dos erros de posição
eP_ = np.zeros([2, 1])
ePm1 = 0 # erro posição k-1 (passo anterior)
eVm1 = 0 # erro atitude k-1 (passo anterior)

# Constanstes do modelo
m = 0.25 # massa
g = 9.81 # aceleração da gravidade
l = 0.1 # tamanho
kf = 1.744e-08 # constante de força
Iz = 2e-4 # momento de inércia
tal = 0.05
Fe = np.array([-m*g])

# Restrições do controle
phi_max = 15*np.pi/180. # ângulo máximo
w_max = 15000
Fc_max = kf*w_max**2 # Força de controle máximo
Tc_max = l*kf*w_max**2
h = 4e-3

# Vetor de estados
# State vector
# x = [ w r_xy v_xy phi omega]' \in R^8
#x = np.zeros([8, tam])
#k = 0
#x[:,0] = np.array([0.,1.,2,3,4,5,6,7,])
x = np.array([0., 0., 1, 2.4, 0., .0, 0*np.pi/180., 0*np.pi/180.])

# Runge Kutta de 4ª órdem
def rk4(tk, h, xk, uk):
    k1 = x_dot(tk , xk , uk)
    k2 = x_dot(tk + h/2.0, xk + h*k1/2.0, uk)
    k3 = x_dot(tk + h/2.0, xk + h*k2/2.0, uk)
    k4 = x_dot(tk + h , xk + h*k3 , uk)
    xkp1 = xk +(h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    return xkp1

def x_dot(t, x, w_):
    # State vector
    # x = [ w r_xy v_xy phi omega]' \in R^8
    #print('x: ', x)
    #print('w_: ', w_)
    ## Parâmetros
    w_max = 15000. # velocidade máxima do motor
    m = 0.25 # massa
    g = 9.81 # aceleração da gravidade
    l = 0.1 # tamanho
    kf = 1.744e-08 # constante de força
    Iz = 2e-4 # momento de inércia
    tal = 0.005
    Fg = np.array([[0], [-m*g]])
    ## Estados atuais
    w = x[0:2]
    r = x[2:4]
    v = x[4:6]
    phi = x[6]
    ome = x[7]
    ## Variáveis auxiliares
    # forças
    f1 = kf * w[0]**2
    f2 = kf * w[1]**2
    # Torque
    Tc = l * (f1 - f2)
    # Força de controle
    Fc_B = np.array([[0], [(f1 + f2)]])
    # Matriz de atitude
    D_RB = np.array([[ np.cos(phi), -np.sin(phi)], [ np.sin(phi), np.cos(phi)]])
    ## Derivadas
    w_dot = (-w + w_)/tal
    r_dot = v
    v_dot = (1/m)*(D_RB @ Fc_B + Fg)
    v_dot = v_dot.reshape(2,)
    phi_dot = np.array([ome])
    ome_dot = np.array([Tc/Iz])
    xkp1 = np.concatenate([ w_dot, r_dot, v_dot, phi_dot, ome_dot ])
    return xkp1


def executePID(x, destino, t):
    eP = [0,0]
    destinoX = destino[0]
    destinoY = destino[1]
    # Extrai os dados do vetor
    r_k = x[2:4]
    v_k = x[4:6]
    phi_k = x[6]
    ome_k = x[7]
    # Comando de posição
    v_ = np.array([0,0])
    #####################
    # Controle de Posição
    kpP = np.array([.05])
    kdP = np.array([0.25])
    eP[0] = destinoX - r_k[0]
    eP[1] = destinoY - r_k[1]
    #print(r_k[1])
    eV = v_ - v_k
    eP_ = eP
    Fx = kpP * eP[0] + kdP * eV[0]
    Fy = kpP * eP[1] + kdP * eV[1] - Fe
    Fy = np.maximum(0.2*Fc_max, np.minimum(Fy, 0.8*Fc_max))
    #####################
    # Controle de Atitude
    phi_ = np.arctan2(-Fx, Fy)
    if np.abs(phi_) > phi_max:
    #print(phi_*180/np.pi)
        signal = phi_/np.absolute(phi_)
        phi_ = signal * phi_max
    # Limitando o ângulo
        Fx = Fy * np.tan(phi_)
    Fxy = np.array([Fx, Fy])
    Fc = np.linalg.norm(Fxy)
    f12 = np.array([Fc/2.0, Fc/2.0])
    # Constantes Kp e Kd
    kpA = np.array([.75])
    kdA = np.array([0.05])
    ePhi = phi_ - phi_k
    eOme = 0 - ome_k
    Tc = kpA * ePhi + kdA * eOme
    Tc = np.maximum(-0.4*Tc_max, np.minimum(Tc, 0.4*Tc_max))
    # Delta de forças
    df12 = np.absolute(Tc)/2.0
    # Forças f1 e f2 final f12' = f12 + deltf12
    if (Tc >= 0.0):
        f12[0] = f12[0] + df12
        f12[1] = f12[1] - df12
    else:
        f12[0] = f12[0] - df12
        f12[1] = f12[1] + df12
    # Comando de rpm dos motores
    w1_ = np.sqrt(f12[0]/(kf))
    w2_ = np.sqrt(f12[1]/(kf))
    #
    # Limitando o comando do motor entre 0 - 15000 rpm
    w1 = np.maximum(0., np.minimum(w1_, w_max))
    w2 = np.maximum(0., np.minimum(w2_, w_max))
    # Determinação do comando de entrada
    w_= np.array([w1, w2])

    # Simulação um passo a frente

    x = rk4(t, h, x, w_)
    x = rk4(t, h, x, w_)
    x = rk4(t, h, x, w_)
    x = rk4(t, h, x, w_)
    x = rk4(t, h, x, w_)
    x = rk4(t, h, x, w_)
    x = rk4(t, h, x, w_)
    x = rk4(t, h, x, w_)
    
    return x, eP, ePhi


if __name__ == '__main__':
    x[2:4] = [580.38215261, 135.887583]
    a, e1, e2 = executePID(x, [578, 134], 0.01666/1000)
    print(e2)


