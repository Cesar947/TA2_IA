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
        n_patrones_entrada, _ = entradas_train.shape

        for i in range(self.iteraciones):
            
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
            resta = decision(resultado_capa_salida) - salidas_train 
            accuracy = self.precision(resta)
            #costo = self.error_cuadratico(error, n_patrones_entrada)

        
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

            if(accuracy >= 0.85 or (i == self.iteraciones - 1)):
                print(f"Iteraciones necesarias {self.iteraciones_reales}")
                print(f"Accuracy train {accuracy}")
                break
            
          
            

    def predecir(self, entradas_test, salidas_test):
        #Cálculo en la capa oculta
        activacion_capa_oculta = np.dot(entradas_test, self.pesos_ocultos)
        activacion_capa_oculta += self.umbral_oculto
        resultado_capa_oculta = self.sigmoide_activacion(activacion_capa_oculta)
  
        #Cálculo en la capa de salida
        activacion_capa_salida = np.dot(resultado_capa_oculta, self.pesos_salida)
        activacion_capa_salida += self.umbral_salida
        resultado_capa_salida = self.sigmoide_activacion(activacion_capa_salida)

        diferencia = decision(resultado_capa_salida) - salidas_test
        accuracy = self.precision(diferencia)

        print(f"Accuracy test: {accuracy}")
        return resultado_capa_salida

    def precision(self, diferencia):
        no_ceros = np.count_nonzero(diferencia)/diferencia.shape[0]
        return 1.0 - no_ceros
   
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


def seleccionar_enfrentamiento():
    pokemon_df = pd.read_csv("./Pokemon_Fight_App/Pokemon_matchups_V2.csv", delimiter=",")

    # Datos que se mostraran en el juego y de donde predecirá la red neuronal en ejecución
    data_game = pokemon_df.sample(frac=0.2,random_state=200)

    row = data_game.sample()
    test_label = row[['Winner']]
    test_label = test_label.to_numpy(dtype=np.float64)

    index = row[["Index"]].to_numpy()[0][0]
    diccionario = row.to_dict()

    nombre_pokemon_1 = diccionario["Pokemon_1"][index-1]
    nombre_pokemon_2 = diccionario["Pokemon_2"][index-1]
    ganador = diccionario["Winner"][index-1]
    
    row.pop("Pokemon_1")
    row.pop("Pokemon_2")
    row.pop("Winner")
    row.pop("Index")
    row.pop("Type_1")
    row.pop("Type_2")

    row_test = row.to_numpy(dtype=np.float64)
    stats_1 = row_test[0][0:6]
    stats_2 = row_test[0][6:]

    dict_pokemon = {
        "nombre_pokemon_1": nombre_pokemon_1,
        "nombre_pokemon_2": nombre_pokemon_2,
        "ganador_real": ganador,
        "stats_1": stats_1,
        "stats_2": stats_2,
        "fila_test": row_test 
    }
    
    return dict_pokemon, test_label
  
def decision(prediccion):
    pre = prediccion.copy()
    pre[pre >= 0.5] = 1
    pre[pre <= 0.5] = 0
    return pre


    

red = Backpropagation(0.001, 12, 2, 1, 10000)
train_features, train_labels, test_features, test_labels = crear_dataset()
enfrentamiento, test_label = seleccionar_enfrentamiento()

red.inicializarPesos()
red.entrenar(train_features, train_labels)
red.predecir(test_features, test_labels)

print("Precision de enfrentamiento")
print(f"Ganador verdadero: {enfrentamiento['ganador_real']}")
prediccion = red.predecir(enfrentamiento['fila_test'], test_label)
print(f"Prediccion: {1 if prediccion[0][0] >= 0.5 else 0}")


