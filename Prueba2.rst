========================
    Recurso carros
========================

Recurso POST
------------
    .. http:post:: /api/cars

    Crea un carro

    * **Campos obligatorios**

        :number_plate: **(string)** Placa del carro
        :model: **(string)** Modelo del carro
        :branch: **(string)** Marca del carro
        :usuario: **(int)** Id del propietario del carro

    * **Ejemplo de petición**

        ..host:: http

            POST /api/cars
            Content-Type: json

            {
                "number_plate": "NPE112",
                "model": "2002",
                "branch": "Chevrolet",
                "usuario": 5
            }

    * **Ejemplos de respuestas**

        ..host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json
            {
                "Success": "Carro creado"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json
            {
                "errors": {
                    "branch": [
                        "required field"
                    ],
                    "model": [
                        "required field"
                    ],
                    "number_plate": [
                        "required field"
                    ],
                    "usuario": [
                        "required field"
                    ]
                }
            }

Recurso GET
-----------

    ..http:get:: /api/cars

    Recibe los carros que hay registrados

    * **Ejemplo de petición**

        .. host:: http

            GET /api/cars HTTP/1.1 
            Content-Type: None

    * **Ejemplos de respuestas**

        .. host:: http

             HTTP/1.1 200 OK
             Content-Type: json
             {
                "data": [
                            {
                                "id": 7,
                                "number_plate": "NPE112",
                                "model": "2002",
                                "branch": "Chevrolet",
                                "usuario": 5
                            }
                    ]
            }

Recurso DELETE
--------------

    ..http:delete:: /api/cars?id=<pk>

    Elimina un carro

    * **Ejemplo de petición**
        .. **Campos Obligatorios**

            :id: **(int)** Id del carro

    * **Ejemplo de petición**

        .. host:: http

            DELETE /api/cars?id=1 HTTP/1.1
            Params

            id: 2

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            {
                "Success": "Carro eliminado"
            }

            HTTP/1.1 400 BAD_REQUEST
            {
                "Error": "Id no válida"
            }

Recurso PATCH
------------
    .. http:patch:: /api/cars

    Actualiza un carro

    * **Campos obligatorios**

        :id: **(id)** Placa del carro

    * **Campos opcionales** 
        :model: **(string)** Modelo del carro
        :branch: **(string)** Marca del carro
        :usuario: **(int)** Id del propietario del carro

    * **Ejemplo de petición**

        ..host:: http

            POST /api/cars
            Params id:5
            Content-Type: json

            {
                "number_plate": "NPE112",
                "model": "2022",
                "branch": "Chevrolet",
                "usuario": 5
            }

    * **Ejemplos de respuestas**

        ..host:: http

            HTTP/1.1 202 CREATED
            Content-Type: None

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json
            {
                "errors": {
                    "number_plate": [
                        "required field"
                    ],
                    "model": [
                        "required field"
                    ],
                    "branch": [
                        "required field"
                    ],
                    "usuario": [
                        "required field"
                    ]
                }
            }


:status 200: Petición completada
:status 201: Usuario creado
:status 202: Petición de actualización aceptada
:status 400: Valores inválidos
