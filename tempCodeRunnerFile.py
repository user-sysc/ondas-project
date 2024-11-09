import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constantes físicas
h = 6.626e-34      # Constante de Planck (J·s)
c = 3e8            # Velocidad de la luz (m/s)
k_B = 1.38e-23     # Constante de Boltzmann (J/K)

# Función de la ley de Planck
def planck_law(wavelength, temperature):
    numerator = 2 * h * c**2 / wavelength**5
    denominator = np.exp((h * c) / (wavelength * k_B * temperature)) - 1
    return numerator / denominator

# Configuración inicial de longitud de onda en metros y temperatura
wavelengths = np.linspace(1e-7, 2e-6, 500)  # Rango de longitud de onda inicial (de 0.1 µm a 2 µm)
initial_temperature = 5850  # Temperatura inicial en Kelvin

# Calcular la densidad espectral de potencia inicial
intensity = planck_law(wavelengths, initial_temperature)

# Crear la gráfica inicial
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.35)  # Ajuste de espacio para los sliders
line, = ax.plot(wavelengths * 1e6, intensity, color="orange", label=f"T = {initial_temperature} K")  # Convertir a µm para el eje x
ax.set_xlabel("Longitud de onda (µm)")
ax.set_ylabel("Densidad de potencia espectral (W/m²/µm)")
ax.set_title("Distribución espectral de un cuerpo negro")

# Resaltar las regiones ultravioleta, visible e infrarroja
ax.axvspan(0.1, 0.4, color='purple', alpha=0.3, label="Ultravioleta")
ax.axvspan(0.4, 0.7, color='grey', alpha=0.3, label="Visible")
ax.axvspan(0.7, 2, color='red', alpha=0.3, label="Infrarrojo")

# Escala logarítmica en el eje y para mayor detalle en valores bajos
ax.set_yscale("log")

# Añadir slider de temperatura
ax_temp = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor="lightgoldenrodyellow")
temp_slider = Slider(ax=ax_temp, label="Temperatura (K)", valmin=1000, valmax=10000, valinit=initial_temperature)

# Añadir slider para el rango máximo de longitud de onda en µm
ax_lambda = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightblue")
lambda_slider = Slider(ax=ax_lambda, label="Longitud de onda máxima (µm)", valmin=1, valmax=3, valinit=2)

# Función para actualizar la gráfica cuando los sliders cambian
def update(val):
    # Obtener valores actuales de los sliders
    temperature = temp_slider.val
    lambda_max = lambda_slider.val * 1e-6  # Convertir de µm a metros

    # Actualizar el rango de longitud de onda
    wavelengths = np.linspace(1e-7, lambda_max, 500)
    intensity = planck_law(wavelengths, temperature)
    
    # Actualizar la curva
    line.set_xdata(wavelengths * 1e6)  # Convertir a µm para el eje x
    line.set_ydata(intensity)
    line.set_label(f"T = {int(temperature)} K")
    ax.set_xlim(0.1, lambda_slider.val)  # Ajustar el límite del eje x en µm

    # Actualizar leyenda y redibujar
    ax.legend(loc="upper right")
    fig.canvas.draw_idle()

# Conectar los sliders con la función de actualización
temp_slider.on_changed(update)
lambda_slider.on_changed(update)

# Mostrar leyenda y gráfica inicial
ax.legend(loc="upper right")
plt.show()
