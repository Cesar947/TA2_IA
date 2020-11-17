import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class Backpropagation:
    def __init__(self, factorAprendizaje, n_entradas, n_ocultas, n_salidas, iteraciones):
        self.factorAprendizaje = factorAprendizaje
        self.n_entradas = n_entradas
        self.n_ocultas = n_ocultas
        self.n_salidas = n_salidas
        self.pesos_ocultos = None
        self.pesos_salida = None
        self.umbral_oculto = None
        self.umbral_salida = None
        self.iteraciones = iteraciones
        self.iteraciones_reales = 0
        

    def sigmoide_activacion(self, x):
        return 1 / (1 + np.exp(-x))

    def derivada_sigmoide(self, x):
        return x * (1 - x)

    def error_cuadratico(self, x, n_patrones_entrada):
        power = np.power(x, 2)
        sum = np.sum(power)
        return sum/2

    def inicializarPesos(self):
        self.pesos_ocultos = np.random.uniform(size=(self.n_entradas, self.n_ocultas))
        self.pesos_salida = np.random.uniform(size=(self.n_ocultas, self.n_salidas))

        self.umbral_oculto = np.random.uniform(size=(1 , self.n_ocultas))#[[1, 1]]
        self.umbral_salida = np.random.uniform(size=(1 , self.n_salidas))#[[1]]


    def entrenar(self, entradas_train, salidas_train):
        
        for i in range(self.iteraciones):
            
            n_patrones_entrada, _ = entradas_train.shape

            #Cálculo en la capa oculta
            activacion_capa_oculta = np.dot(entradas_train, self.pesos_ocultos)
            activacion_capa_oculta += self.umbral_oculto
            resultado_capa_oculta = self.sigmoide_activacion(activacion_capa_oculta)
  
            #Cálculo en la capa de salida
            activacion_capa_salida = np.dot(resultado_capa_oculta, self.pesos_salida)
            activacion_capa_salida += self.umbral_salida
            resultado_capa_salida = self.sigmoide_activacion(activacion_capa_salida)
   
            #Error de la época
            error = salidas_train - resultado_capa_salida 
            costo = self.error_cuadratico(error, n_patrones_entrada)

        
            #Cálculo de deltas

            ### Delta para la capa de salida
            delta_capa_salida = error * self.derivada_sigmoide(resultado_capa_salida)
            
            ### Deltas para la capa oculta
            error_capa_oculta = delta_capa_salida.dot(self.pesos_salida.T)
            delta_capa_oculta = error_capa_oculta * self.derivada_sigmoide(resultado_capa_oculta)

            #Actualización de pesos
            self.pesos_salida += resultado_capa_oculta.T.dot(delta_capa_salida) * self.factorAprendizaje
            self.umbral_salida += np.sum(delta_capa_salida) * self.factorAprendizaje

            self.pesos_ocultos += entradas_train.T.dot(delta_capa_oculta) * self.factorAprendizaje
            self.umbral_oculto += np.sum(delta_capa_oculta) * self.factorAprendizaje
            self.iteraciones_reales += 1

            #Si el error cuadrático medio
            if(costo <= 0.01 or (i == self.iteraciones - 1)):
                print(resultado_capa_salida)
                break
                


    def test(self, entradas_test):
        #Cálculo en la capa oculta
        activacion_capa_oculta = np.dot(entradas_test, self.pesos_ocultos)
        activacion_capa_oculta += self.umbral_oculto
        resultado_capa_oculta = self.sigmoide_activacion(activacion_capa_oculta)
  
        #Cálculo en la capa de salida
        activacion_capa_salida = np.dot(resultado_capa_oculta, self.pesos_salida)
        activacion_capa_salida += self.umbral_salida
        resultado_capa_salida = self.sigmoide_activacion(activacion_capa_salida)

        return resultado_capa_salida

   
def crear_dataset():
        pokemon_df = pd.read_csv("./Pokemon_Fight_App/Pokemon_matchups_V2.csv", delimiter=",")

        pokemon_df.pop("Pokemon_1")
        pokemon_df.pop("Type_1")
        pokemon_df.pop("Pokemon_2")
        pokemon_df.pop("Type_2")
        pokemon_df.pop("Index")

        train = pokemon_df.sample(frac=0.8,random_state=200)
        test = pokemon_df.drop(train.index)

        train_features = train.copy(deep=True)
        train_features.pop("Winner")
        normalized_df = (train_features-train_features.min())/(train_features.max()-train_features.min())
        train_features = normalized_df.to_numpy(dtype=np.float64)

        train_labels = train.copy(deep=True)
        train_labels = train_labels[['Winner']]
        train_labels = train_labels.to_numpy(dtype=np.float64)

        test_features = test.copy(deep=True)
        test_features.pop("Winner")
        normalized_df = (test_features-test_features.min())/(test_features.max()-test_features.min())
        test_features = normalized_df.to_numpy(dtype=np.float64)

        test_labels = test.copy(deep=True)
        test_labels = test_labels[['Winner']]
        test_labels = test_labels.to_numpy(dtype=np.float64)

        return train_features, train_labels, test_features, test_labels


red = Backpropagation(0.001, 12, 2, 1, 10000)
train_features, train_labels, test_features, test_labels = crear_dataset()

red.inicializarPesos()
red.entrenar(train_features, train_labels)
print("Entrenamiento")
print(f"Iteraciones {red.iteraciones_reales}")
print(red.test(np.array([[12,50,105,125,50,330,3,50,54,54,40,145.5]], dtype=np.float64)))

