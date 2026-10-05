# Nicole Robles NC 0120
import cv2

# Cargar la imagen
# Línea 4
imagen = cv2.imread("imagenes/garza 0120.webp")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original 0120", imagen)
cv2.imshow("Imagen suavizada - Filtro Gaussiano 0120", imagen_suavizada)

# Guardar resultado
cv2.imwrite(
    "garza 0120.webp",
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("garza 0120.webp")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Nicole Robles NC 0120")