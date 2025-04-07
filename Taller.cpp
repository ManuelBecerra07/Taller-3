#include <iostream>
using namespace std;
float km_to_miles = 0.621371; //Variable Global
int temp_celsius; //Nombre a la variable
void convertirUnidades() {
    short distancia_km = 10;
    long resultado_millas;
    double temp_fahrenheit = 32.0;
    resultado_millas = distancia_km * km_to_miles;
    cout << distancia_km << " km equivale a " << resultado_millas << " millas" << endl;
    float temp_celsius;     
    temp_celsius = 25.5;//Error el numero tiene comillas como si fuera un String
    temp_fahrenheit = temp_celsius * 9/5 + 32;
    cout << temp_celsius << " °C equivale a " << temp_fahrenheit << " °F" << endl;
    char unidad = 'C'; //Error la unidad Char solo equivale a un caracter numerico no a un String
    cout << "Unidad: " << unidad << endl;
}
int main() {
    convertirUnidades();
    cout << "Temperatura global: " << temp_celsius << endl;
    return 0;
    }
    