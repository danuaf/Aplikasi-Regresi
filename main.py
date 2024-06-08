import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit


if __name__ == "__main__":

    # Input data
    df = pd.read_csv('assets/Student_Performance.csv')
    TB = df['Hours Studied']
    NL = df['Sample Question Papers Practiced']
    NT = df['Performance Index']

    # Problem 2 dengan metode linear
    X_nl = NL.values.reshape(-1, 1)
    y_nt = NT.values

    linear_model = LinearRegression()
    linear_model.fit(X_nl, y_nt)
    y_pred_linear = linear_model.predict(X_nl)
    rms_linear = np.sqrt(mean_squared_error(y_nt, y_pred_linear))

    # Problem 2 dengan metode eksponensial
    def exponential_model(x, a, b):
        return a * np.exp(b * x)

    params, covariance = curve_fit(exponential_model, NL, NT)
    y_pred_exp = exponential_model(NL, *params)
    rms_exp = np.sqrt(mean_squared_error(NT, y_pred_exp))

    # Problem 2 dengan metode polinomial
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X_nl)
    poly_model = LinearRegression()
    poly_model.fit(X_poly, y_nt)
    y_pred_poly = poly_model.predict(X_poly)
    rms_poly = np.sqrt(mean_squared_error(y_nt, y_pred_poly))


    # plot untuk ketiga metode 

    # plot untuk regresi linear
    plt.figure(figsize=(16, 7))
    plt.subplot(1,3,1)
    plt.scatter(NL, NT, color='orange', label='Data')
    plt.plot(NL, y_pred_linear,'--', color='Red', label='Linear Fit')
    plt.title('Regresi Linear')
    plt.xlabel('Jumlah Latihan Soal')
    plt.ylabel('Nilai Ujian')
    plt.legend()

    # plot untuk regresi eksponensial
    plt.subplot(1, 3, 2)
    plt.scatter(NL, NT, color='orange', label='Data')
    plt.plot(NL, y_pred_exp,'--', color='green', label='Exponential Fit')
    plt.title('Regresi Ekponensial')
    plt.xlabel('Jumlah Latihan Soal')
    plt.ylabel('Nilai Ujian')
    plt.legend()

    # plot untuk regresi polinomial
    plt.subplot(1, 3, 3)
    plt.scatter(NL, NT, color='orange', label='Data')
    plt.plot(NL, y_pred_poly,'--', color='blue', label='Polynomial Fit')
    plt.title('Regresi Polinomial')
    plt.xlabel('Jumlah Latihan Soal')
    plt.ylabel('Nilai Ujian')
    plt.legend()

    # plot untuk kompoarasi ketiga metode
    plt.figure(figsize=(16, 7))
    plt.scatter(NL, NT, color='orange', label='Data')
    plt.plot(NL, y_pred_linear,'--', color='Red', label='Linear Fit')
    plt.plot(NL, y_pred_exp,'--', color='green', label='Exponential Fit')
    plt.plot(NL, y_pred_poly,'--', color='blue', label='Polynomial Fit')
    plt.title('Komparasi')
    plt.xlabel('Jumlah Latihan Soal')
    plt.ylabel('Nilai Ujian')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # print nilai RMS untuk ketiga metode
    print(f"RMS Metoder Linear: {rms_linear}")
    print(f"RMS Metode Eksponential : {rms_exp}")
    print(f"RMS Metode Polinomial: {rms_poly}")
