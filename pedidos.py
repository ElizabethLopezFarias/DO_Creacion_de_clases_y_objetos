from te import Te
#Permite al usuario ingresar los datos para generar un pedido de té
#Solicita los valores al usuario de tipo y formato
sabor = int(input (f"""Escoja el tipo de té:
                   TIPOS DE TÉ
                        # 1: Té negro
                        # 2: Té verde
                        # 3: Infusión de hierbas                
                   """))

formato = int(input (f""" Elija el formato:
                     # FORMATOS
                        # 300: 300 gr
                        # 500: 500 gr
                     """))
#almacena los retornos de los métodos
tiempo, recomendacion = Te.retornar_tiempo_y_recomendacion(sabor)
precio = Te.retornar_precio(formato)

#establece la variable sabor_texto
if sabor == 1:
    sabor_texto = "Té Negro"
elif sabor == 2:
    sabor_texto = "Té Verde"
elif sabor == 3:
    sabor_texto = "Infusión de Hierbas"

#entrega el detalle del pedido
print (f""" El detalle de su pedido es el siguiente:
            Sabor del tipo de té: {sabor_texto}
            Formato: {formato}
            Precio: $ {precio}
            Tiempo de infusión: {tiempo} minutos
            Recomendación para disfrutar: {recomendacion}
       """)