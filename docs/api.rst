API
===
.. autosummary::
   :toctree: generated

   mmpackage

Functions
------

.. code-block:: console

   mmpackage.greetings()
   
After that call program will say Hello to us.

-----

.. code-block:: console

   mmpackage.get_location(city)
   
The argument in this function is city name and it returns ``latitude`` and  ``longitude`` of specified city.

-----

.. code-block:: console

   mmpackage.get_meteo_data(latitude, longitude)
   
This function gives us ``weather`` in the city of the given latitude and longitude.

-----

.. code-block:: console

   mmpackage.weather(time, cities)
   
In this function we give two arguments. The ``time`` when we want to check the weather and the ``city`` or a ``list of cities`` for which it will be checked.
After execution, it will return the ``temperature`` and ``atmospheric pressure`` of the given city or cities and a ``graph`` showing this.
