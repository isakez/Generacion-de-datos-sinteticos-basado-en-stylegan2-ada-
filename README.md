# AUMENTO DE DATOS BASADO EN GANS PARA LA CLASIFICACIÓN DE PLANOS CEREBRALES DE INFANTES PREMATUROS
Proyecto del TFG donde exploramos técnicas de aprendizaje automático en un contexto médico. Nos centramos en la generación de imágenes sintéticas mediante un modelo entrenado a partir del repositorio de StyleGAN2-ADA.

El objetivo es evaluar el rendimiento de un clasificador de imágenes de planos cerebrales de infantes prematuros, entrenado en distintos casos.
1. Con el dataset completo etiquetado, aplicando un aprendizaje supervisado
2. Con un porcentaje del dataset etiquetado y otro dataset mucho mayor de imágenes generadas por nuestro modelo, este segundo conjunto de datos esta sin etiquetar por lo que aplicamos un aprendizaje semi-supervisado mediante pseudo-etiquetas.

Para llevar a cabo este proyecto hemos hecho uso del entorno de programación de fast.ai, el repositorio https://github.com/NVlabs/stylegan2-ada-pytorch y los servidores de paperspace.

## Extraccion.ipynb

En este notebook, extraemos los planos sagitales y coronales a partir de los volúmenes nrrd. Además los procesamos para convertirlos en RGB y reescalamos las imágenes para que tengan el mismo tamaño de 256x256 píxeles. 
Después de ejecutar este notebook deberiamos tener el conjunto de datos de entrenamiento en distintas carpetas según su etiqueta.

![3D_slicer](https://github.com/isakez/TFG/assets/42270381/b5c65a2e-a5a2-477b-ac35-9514af3fddd6)

![planos_aumento (1)](https://github.com/isakez/TFG/assets/42270381/aeebc5fe-77db-48e9-be05-1b485e3bb6e0)



## Clasificador_Imagenes.ipynb

Notebook donde explaramos e iteramos varias veces para entrenar un modelo clasificador basado en el conjunto etiquetado que hemos obtenido anteriormente. Al final de este notebook exportamos el clasificador base.

## StyleGAN2_Model.ipynb

Aquí hacemos uso del respositorio de styleGAN2-ada para entrenar nuestro modelo, en este caso hasta las 1200kimg. Una vez entrenado usamos el mismo notebook para generar las imágenes sinteticas con distintos valores de truncación. Las imágenes aquí generadas formaran el conjunto de datos para el entrenamiento semi-supervisado.

![muestra_fakes000800](https://github.com/isakez/TFG/assets/42270381/04ef7cf8-19bb-49a1-a05e-c9551b2720ac)

![muestra_fakes000400](https://github.com/isakez/TFG/assets/42270381/1030676e-a4df-42aa-844e-d62f648ebb5e)

## Entrenamiento_Semisupervisado.ipynb

En este notebook iteramos de la siguiente forma, entrenamos un clasificador base con solo un porcentaje (20,50 y 70 ) del conjunto etiquetado original, aplicamos las pseudoetiquetas para un sesgo especificado previamente, añadimos esas imágenes al conjunto de datos anterior y volvemos a entrenar el clasficador esperando mejorar nuestro valores de accuracy y loss. Este proceso lo podemos iterar hasta que el conjunto de datos artificiales este completamente pseudo etiquetado o obtengamos mejoras en el rendimiento de clasificador.

## Probar_Modelo.ipynb

Aquí  ponemos a prueba nuetros distintos modelos clasificadores con un conjunto de datos que no han visto durante su entrenamiento.

![Tabla_resultados](https://github.com/isakez/TFG/assets/42270381/41638522-ef0a-4699-9483-5b5cfbb9e077)




