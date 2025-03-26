// Reemplaza 'YOUR_API_KEY' con tu clave de API de OpenWeatherMap
const API_KEY = 'b3c00c360b119aa09fd055754dddb14b';
const BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';

// Función para obtener datos del clima por ciudad
async function getWeatherByCity(city) {
    try {
        const response = await fetch(`${BASE_URL}?q=${city}&appid=${API_KEY}&units=metric`);
        if (!response.ok) {
            throw new Error(`Error: ${response.status} - ${response.statusText}`);
        }
        const data = await response.json();
        console.log(`Clima en ${city}:`);
        console.log(`Temperatura: ${data.main.temp}°C`);
        console.log(`Descripción: ${data.weather[0].description}`);
        console.log(`Humedad: ${data.main.humidity}%`);
    } catch (error) {
        console.error('Error al obtener los datos del clima:', error.message);
    }
}

// Ejemplo de uso
getWeatherByCity('Madrid');