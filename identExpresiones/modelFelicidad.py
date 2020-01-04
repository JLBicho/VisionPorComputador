from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import ensemble
from sklearn import neighbors
import pandas as pd
import pickle


def crearModelo(X_train, X_test, y_train, y_test, clasificador, nombre):
    model = clasificador.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print("Score: " + str(score))
    filename = ('ModelosFelicidad(80-20)/' + nombre + 'Classifier ['
                + ("{0:.3f}".format(score)) + '].sav')
    # Guarda el modelo en un archivo
    pickle.dump(model, open(filename, 'wb'))
    return model


if __name__ == "__main__":
    datos = pd.read_csv('Database/dataBaseAUs.csv')
    X = datos.iloc[:, 1:]
    y = datos.Feliz
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    lm = linear_model.PassiveAggressiveClassifier()
    model = crearModelo(X_train, X_test, y_train, y_test, lm, 'pasivoAgresivo')
    lm = linear_model.LogisticRegression()
    model = crearModelo(X_train, X_test, y_train, y_test, lm, 'LogisticRegression')
    lm = linear_model.RidgeClassifier()
    model = crearModelo(X_train, X_test, y_train, y_test, lm, 'Ridge')
    lm = linear_model.SGDClassifier()
    model = crearModelo(X_train, X_test, y_train, y_test, lm, 'SGD')
    lm = ensemble.RandomForestClassifier(3)
    model = crearModelo(X_train, X_test, y_train, y_test, lm, 'RandomForest')
    lm = ensemble.GradientBoostingClassifier()
    model = crearModelo(X_train, X_test, y_train, y_test, lm, 'GradientBoosting')
    lm = ensemble.AdaBoostClassifier()
    model = crearModelo(X_train, X_test, y_train, y_test, lm, 'AdaBoost')
    lm = neighbors.KNeighborsClassifier()
    model = crearModelo(X_train, X_test, y_train, y_test, lm, 'KNeighbors')
    # Ejemplo para cargar modelo
    """
    filename = 'ModelosFelicidad/' + 'pasivoAgresivoClassifier [0.927].sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    """
