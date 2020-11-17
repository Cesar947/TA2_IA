import numpy as np

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

    def error_cuadratico(self, x):
        power = np.power(x, 2)
        sum = np.sum(power)
        return sum/2

    def inicializarPesos(self):
        self.pesos_ocultos = np.random.uniform(size=(self.n_entradas, self.n_ocultas))
        self.pesos_salida = np.random.uniform(size=(self.n_ocultas, self.n_salidas))

        self.umbral_oculto = np.random.uniform(size=(1 , self.n_ocultas))
        self.umbral_salida = np.random.uniform(size=(1 , self.n_salidas))

    def entrenar(self, entradas_train, salidas_train):
        
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
            costo = self.error_cuadratico(error)

            #Si el erro cuadrático medio
            if(costo < 0.01):
                break

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
   


red = Backpropagation(0.01, 12, 4, 1, 6000)

inputs = np.array([
    [1,45,49,49,45,118,4,80,70,40,145,310.5],
    [1,60,62,63,60,155,4,70,90,70,40,254.5],
    [1,80,82,83,80,255,4,60,70,50,65,224.5],
    [1,80,100,123,80,293,4,65,90,40,75,245]])
expected_output = np.array([[0], [0], [1], [1]])
entradas_test = np.array([[2,39,52,43,65,189,4,25,20,20,45,6]])
red.inicializarPesos()
red.entrenar(inputs, expected_output)
print("Entrenamiento")
print(f"Iteraciones {red.iteraciones_reales}")
print(red.test(entradas_test))


