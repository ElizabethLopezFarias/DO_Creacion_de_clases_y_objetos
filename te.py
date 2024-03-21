# TIPOS DE TÉ
# 1: Té negro
# 2: Té verde
# 3: Infusión de hierbas

# FORMATOS
# 300 gr
# 500 gr

# PRECIOS
# 300 gr $3000
# 500 gr $5000

# DURACIÓN - atributo de clase
# 1 año o 365 días

# TIEMPO DE PREPARACION
# 1: 3 min
# 2: 5 minutos
# 3: 6 minutos

# RECOMENDACIÓN
# 1: Desayuno
# 2: Medio día
# 3: Atardecer

class Te():
    #todos los té duran lo mismo
    duracion = 365
# 2. Tiempo y Recomendación
    @staticmethod
    def retornar_tiempo_y_recomendacion(sabor:int):
        if sabor == 1:
            return 3, "Al Desayunar"
        elif sabor == 2:
            return 5, " Al Medio día"
        elif sabor == 3:
            return 6, "Al Atardecer"
        
# tiempo, recomendacion = Te.retornar_tiempo_y_recomendacion(1)
# print("Tiempo de preparación:", tiempo, "minutos")
# print("Recomendación:", recomendacion)

#3. PRECIO Y FORMATO
    @staticmethod
    def retornar_precio(formato:int):
        if formato == 300:
            return 3000
        if formato == 500:
            return 5000 

# Comprobación
# precio_300_gr = Te.precio_formato(300)
# precio_500_gr = Te.precio_formato(500)

# print("Precio de 300 gr:", precio_300_gr)
# print("Precio de 500 gr:", precio_500_gr)

