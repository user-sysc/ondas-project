import numpy as np
import matplotlib.pyplot as plt

# Parámetros de cada tipo de onda (en metros)
ondas = {
    "Rayos Gamma": 1e-12,
    "Rayos X": 1e-10,
    "Ultravioleta": 1e-8,
    "Luz Visible": 5e-7,  # Valor aproximado para el centro del espectro visible
    "Infrarrojo": 1e-5,
    "Microondas": 1e-2,
    "Ondas de Radio": 1  # Longitud de onda de 1 metro para ondas de radio
}

# Crear una figura con subgráficas
fig, axes = plt.subplots(len(ondas), 1, figsize=(10, 2 * len(ondas)))
fig.suptitle("Representación de Ondas Electromagnéticas")

# Generar cada gráfica de onda
for ax, (tipo_onda, longitud_onda) in zip(axes, ondas.items()):
    frecuencia = 3e8 / longitud_onda  # Frecuencia usando f = c / λ
    x = np.linspace(0, 5 * longitud_onda, 1000)  # 5 ciclos de la longitud de onda
    y = np.sin(2 * np.pi * frecuencia * x / 3e8)  # Onda sinusoidal
    
    ax.plot(x, y, color="purple")
    ax.set_title(tipo_onda)
    ax.set_xlabel("Posición (m)")
    ax.set_ylabel("Amplitud")
    ax.grid(True, linestyle="--", linewidth=0.5)

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajustar para no superponer el título
plt.show()
