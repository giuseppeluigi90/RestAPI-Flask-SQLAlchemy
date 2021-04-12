Panel de Control
================
 

Menús y Tablas
--------------

* Información del cliente
  
    Correo, nombre, clave, etc.    

* Objetivos
  
    Nombres de las webs, comercios o URLs a extraer    

* Scrapers
  
    URLs y su meta data (JSON)

* Programación (a qué hora?)
  
    Asignación de horario para ejecución de scrapers

* Registros

    Información de ejecución de scraper: fecha y hora, scraper, cantidad de elementos
    extraídos y peticiones (requests), también posibles errores

* Facturas
  
    Documentos comerciales emitidos, listos para su descarga

* Pagos
  
    Información de pagos y operaciones realizadas

* Terminos de Servicio

    Contrato de servicios


Vista Principal
---------------

* Scrapers y Registros

    Lista de scrapers, sus registros y un botón para ejecución inmediata de los mismos



Consideraciones
---------------

* Debe manejar sesiones y autentificación

* Comunicación segura mediante CORS

* La tabla registros se actualiza directamente desde los microservicios, construir un hub simple que lo procese
