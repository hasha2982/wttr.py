1. CLI tool usage
=================

Since 1.1.0-beta.0 (1.1.0b0) there's a CLI tool available as a beta feature.

Here's how you can call it:

.. code-block:: bash

    $ python -m wttrpy

The CLI tool is a "wrapper" for the ``wttrpy`` module that you can import:

.. code-block:: python

    #!/usr/bin/env python3
    import wttrpy

If you call the CLI tool without any options, it will send a GET request to ``https://wttr.in/``,
but wttr.in will auto-detect your location depending on your IP address, but locale will still be English.

1.1. CLI arguments
------------------------------

1.1.1. Optional arguments ``-h`` and ``--help``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``-h`` or ``--help`` will print auto-generated help message by ``argparse``.

.. code-block:: none

    $ python -m wttrpy -h
    usage: __main__.py [-h] [--location LOCATION] [--locale LOCALE]

    optional arguments:
      -h, --help            show this help message and exit
      --location LOCATION, -w LOCATION
                            Set location
      --locale LOCALE, -l LOCALE
                            Set locale
    
    $ python -m wttrpy --help
    usage: __main__.py [-h] [--location LOCATION] [--locale LOCALE]

    optional arguments:
      -h, --help            show this help message and exit
      --location LOCATION, -w LOCATION
                            Set location
      --locale LOCALE, -l LOCALE
                            Set locale

1.1.2. Optional arguments ``-w`` and ``--location``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These arguments are used to change the location of the forecast.

``-w`` and ``--location`` should have a value.

``-w`` and ``--location`` can be values, that you can pass to API function ``getWttr`` (see API docs) as a first parameter (``where``)

.. code-block:: none

    $ python -m wttrpy -w Amsterdam
    Weather report: Amsterdam

         \  /       Partly cloudy
       _ /"".-.     19 °C          
         \_(   ).   ↘ 22 km/h      
         /(___(__)  10 km          
                    0.3 mm         
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤  Thu 16 Jul ├───────────────────────┬──────────────────────────────┐
    │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │      .-.      Light drizzle  │      .-.      Light drizzle  │  _`/"".-.     Light rain sho…│  _`/"".-.     Light rain sho…│
    │     (   ).    16 °C          │     (   ).    17 °C          │   ,\_(   ).   18 °C          │   ,\_(   ).   16 °C          │
    │    (___(__)   ↗ 6-9 km/h     │    (___(__)   → 8-11 km/h    │    /(___(__)  ↘ 14-19 km/h   │    /(___(__)  ↘ 10-16 km/h   │
    │     ‘ ‘ ‘ ‘   2 km           │     ‘ ‘ ‘ ‘   2 km           │      ‘ ‘ ‘ ‘  10 km          │      ‘ ‘ ‘ ‘  10 km          │
    │    ‘ ‘ ‘ ‘    0.3 mm | 97%   │    ‘ ‘ ‘ ‘    0.3 mm | 96%   │     ‘ ‘ ‘ ‘   1.0 mm | 72%   │     ‘ ‘ ‘ ‘   0.5 mm | 61%   │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤  Fri 17 Jul ├───────────────────────┬──────────────────────────────┐
    │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │               Cloudy         │  _`/"".-.     Patchy rain po…│               Cloudy         │    \  /       Partly cloudy  │
    │      .--.     19 °C          │   ,\_(   ).   21 °C          │      .--.     21 °C          │  _ /"".-.     18 °C          │
    │   .-(    ).   ↘ 4-5 km/h     │    /(___(__)  ↘ 5 km/h       │   .-(    ).   ↘ 9-10 km/h    │    \_(   ).   ↖ 4-5 km/h     │
    │  (___.__)__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │  (___.__)__)  10 km          │    /(___(__)  10 km          │
    │               0.1 mm | 51%   │     ‘ ‘ ‘ ‘   0.1 mm | 79%   │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤  Sat 18 Jul ├───────────────────────┬──────────────────────────────┐
    │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │    \  /       Partly cloudy  │               Cloudy         │               Cloudy         │    \  /       Partly cloudy  │
    │  _ /"".-.     20 °C          │      .--.     23..25 °C      │      .--.     21 °C          │  _ /"".-.     19 °C          │
    │    \_(   ).   ↑ 13-16 km/h   │   .-(    ).   ↗ 13-15 km/h   │   .-(    ).   → 11-14 km/h   │    \_(   ).   → 6-9 km/h     │
    │    /(___(__)  10 km          │  (___.__)__)  10 km          │  (___.__)__)  10 km          │    /(___(__)  10 km          │
    │               0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
    Location: Amsterdam, Centrum, Amsterdam, MRA, Stadsregio Amsterdam, Noord-Holland, Nederland [52.3745403,4.89797550561798]

    $ python -m wttrpy --location Amsterdam
    Weather report: Amsterdam

         \  /       Partly cloudy
       _ /"".-.     19 °C          
         \_(   ).   ↘ 22 km/h      
         /(___(__)  10 km          
                    0.3 mm         
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤  Thu 16 Jul ├───────────────────────┬──────────────────────────────┐
    │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │      .-.      Light drizzle  │      .-.      Light drizzle  │  _`/"".-.     Light rain sho…│  _`/"".-.     Light rain sho…│
    │     (   ).    16 °C          │     (   ).    17 °C          │   ,\_(   ).   18 °C          │   ,\_(   ).   16 °C          │
    │    (___(__)   ↗ 6-9 km/h     │    (___(__)   → 8-11 km/h    │    /(___(__)  ↘ 14-19 km/h   │    /(___(__)  ↘ 10-16 km/h   │
    │     ‘ ‘ ‘ ‘   2 km           │     ‘ ‘ ‘ ‘   2 km           │      ‘ ‘ ‘ ‘  10 km          │      ‘ ‘ ‘ ‘  10 km          │
    │    ‘ ‘ ‘ ‘    0.3 mm | 97%   │    ‘ ‘ ‘ ‘    0.3 mm | 96%   │     ‘ ‘ ‘ ‘   1.0 mm | 72%   │     ‘ ‘ ‘ ‘   0.5 mm | 61%   │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤  Fri 17 Jul ├───────────────────────┬──────────────────────────────┐
    │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │               Cloudy         │  _`/"".-.     Patchy rain po…│               Cloudy         │    \  /       Partly cloudy  │
    │      .--.     19 °C          │   ,\_(   ).   21 °C          │      .--.     21 °C          │  _ /"".-.     18 °C          │
    │   .-(    ).   ↘ 4-5 km/h     │    /(___(__)  ↘ 5 km/h       │   .-(    ).   ↘ 9-10 km/h    │    \_(   ).   ↖ 4-5 km/h     │
    │  (___.__)__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │  (___.__)__)  10 km          │    /(___(__)  10 km          │
    │               0.1 mm | 51%   │     ‘ ‘ ‘ ‘   0.1 mm | 79%   │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤  Sat 18 Jul ├───────────────────────┬──────────────────────────────┐
    │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │    \  /       Partly cloudy  │               Cloudy         │               Cloudy         │    \  /       Partly cloudy  │
    │  _ /"".-.     20 °C          │      .--.     23..25 °C      │      .--.     21 °C          │  _ /"".-.     19 °C          │
    │    \_(   ).   ↑ 13-16 km/h   │   .-(    ).   ↗ 13-15 km/h   │   .-(    ).   → 11-14 km/h   │    \_(   ).   → 6-9 km/h     │
    │    /(___(__)  10 km          │  (___.__)__)  10 km          │  (___.__)__)  10 km          │    /(___(__)  10 km          │
    │               0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
    Location: Amsterdam, Centrum, Amsterdam, MRA, Stadsregio Amsterdam, Noord-Holland, Nederland [52.3745403,4.89797550561798]

1.1.3. Optional arguments ``-l`` and ``--locale``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``-l`` and ``--locale`` should have a value.

``-l`` and ``--locale`` can be values, that you can pass to API function ``getWttr`` (see API docs) as a second parameter (``loc``).
That means it can be ``en``, ``fr``, etc.

.. code-block:: none

    $ python -m wttrpy -w Amsterdam -l fr
    Prévisions météo pour: Amsterdam

         \  /       Partiellement couvert
       _ /"".-.     18 °C          
         \_(   ).   ↘ 24 km/h      
         /(___(__)  10 km          
                    0.6 mm         
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤jeu. 16 juil.├───────────────────────┬──────────────────────────────┐
    │             Matin            │          Après-midi   └──────┬──────┘       Soir            │             Nuit             │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │      .-.      Bruine légère  │      .-.      Bruine légère  │  _`/"".-.     Averses légère…│  _`/"".-.     Averses légère…│
    │     (   ).    16 °C          │     (   ).    17 °C          │   ,\_(   ).   18 °C          │   ,\_(   ).   16 °C          │
    │    (___(__)   ↗ 6-9 km/h     │    (___(__)   → 8-11 km/h    │    /(___(__)  ↘ 14-19 km/h   │    /(___(__)  ↘ 10-16 km/h   │
    │     ‘ ‘ ‘ ‘   2 km           │     ‘ ‘ ‘ ‘   2 km           │      ‘ ‘ ‘ ‘  10 km          │      ‘ ‘ ‘ ‘  10 km          │
    │    ‘ ‘ ‘ ‘    0.3 mm | 97%   │    ‘ ‘ ‘ ‘    0.3 mm | 96%   │     ‘ ‘ ‘ ‘   1.0 mm | 72%   │     ‘ ‘ ‘ ‘   0.5 mm | 61%   │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤ven. 17 juil.├───────────────────────┬──────────────────────────────┐
    │             Matin            │          Après-midi   └──────┬──────┘       Soir            │             Nuit             │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │               Nuageux        │  _`/"".-.     Pluies éparses │               Nuageux        │    \  /       Partiellement …│
    │      .--.     19 °C          │   ,\_(   ).   21 °C          │      .--.     21 °C          │  _ /"".-.     18 °C          │
    │   .-(    ).   ↘ 4-5 km/h     │    /(___(__)  ↘ 5 km/h       │   .-(    ).   ↘ 9-10 km/h    │    \_(   ).   ↖ 4-5 km/h     │
    │  (___.__)__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │  (___.__)__)  10 km          │    /(___(__)  10 km          │
    │               0.1 mm | 51%   │     ‘ ‘ ‘ ‘   0.1 mm | 79%   │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤sam. 18 juil.├───────────────────────┬──────────────────────────────┐
    │             Matin            │          Après-midi   └──────┬──────┘       Soir            │             Nuit             │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │    \  /       Partiellement …│               Nuageux        │               Nuageux        │    \  /       Partiellement …│
    │  _ /"".-.     20 °C          │      .--.     23..25 °C      │      .--.     21 °C          │  _ /"".-.     19 °C          │
    │    \_(   ).   ↑ 13-16 km/h   │   .-(    ).   ↗ 13-15 km/h   │   .-(    ).   → 11-14 km/h   │    \_(   ).   → 6-9 km/h     │
    │    /(___(__)  10 km          │  (___.__)__)  10 km          │  (___.__)__)  10 km          │    /(___(__)  10 km          │
    │               0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
    Emplacement: Amsterdam, Centrum, Amsterdam, MRA, Stadsregio Amsterdam, Noord-Holland, Nederland [52.3745403,4.89797550561798]

    $ python -m wttrpy -w Amsterdam --locale fr
    Prévisions météo pour: Amsterdam
    
         \  /       Partiellement couvert
       _ /"".-.     18 °C          
         \_(   ).   ↘ 24 km/h      
         /(___(__)  10 km          
                    0.6 mm         
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤jeu. 16 juil.├───────────────────────┬──────────────────────────────┐
    │             Matin            │          Après-midi   └──────┬──────┘       Soir            │             Nuit             │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │      .-.      Bruine légère  │      .-.      Bruine légère  │  _`/"".-.     Averses légère…│  _`/"".-.     Averses légère…│
    │     (   ).    16 °C          │     (   ).    17 °C          │   ,\_(   ).   18 °C          │   ,\_(   ).   16 °C          │
    │    (___(__)   ↗ 6-9 km/h     │    (___(__)   → 8-11 km/h    │    /(___(__)  ↘ 14-19 km/h   │    /(___(__)  ↘ 10-16 km/h   │
    │     ‘ ‘ ‘ ‘   2 km           │     ‘ ‘ ‘ ‘   2 km           │      ‘ ‘ ‘ ‘  10 km          │      ‘ ‘ ‘ ‘  10 km          │
    │    ‘ ‘ ‘ ‘    0.3 mm | 97%   │    ‘ ‘ ‘ ‘    0.3 mm | 96%   │     ‘ ‘ ‘ ‘   1.0 mm | 72%   │     ‘ ‘ ‘ ‘   0.5 mm | 61%   │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤ven. 17 juil.├───────────────────────┬──────────────────────────────┐
    │             Matin            │          Après-midi   └──────┬──────┘       Soir            │             Nuit             │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │               Nuageux        │  _`/"".-.     Pluies éparses │               Nuageux        │    \  /       Partiellement …│
    │      .--.     19 °C          │   ,\_(   ).   21 °C          │      .--.     21 °C          │  _ /"".-.     18 °C          │
    │   .-(    ).   ↘ 4-5 km/h     │    /(___(__)  ↘ 5 km/h       │   .-(    ).   ↘ 9-10 km/h    │    \_(   ).   ↖ 4-5 km/h     │
    │  (___.__)__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │  (___.__)__)  10 km          │    /(___(__)  10 km          │
    │               0.1 mm | 51%   │     ‘ ‘ ‘ ‘   0.1 mm | 79%   │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                           ┌─────────────┐                                                       
    ┌──────────────────────────────┬───────────────────────┤sam. 18 juil.├───────────────────────┬──────────────────────────────┐
    │             Matin            │          Après-midi   └──────┬──────┘       Soir            │             Nuit             │
    ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
    │    \  /       Partiellement …│               Nuageux        │               Nuageux        │    \  /       Partiellement …│
    │  _ /"".-.     20 °C          │      .--.     23..25 °C      │      .--.     21 °C          │  _ /"".-.     19 °C          │
    │    \_(   ).   ↑ 13-16 km/h   │   .-(    ).   ↗ 13-15 km/h   │   .-(    ).   → 11-14 km/h   │    \_(   ).   → 6-9 km/h     │
    │    /(___(__)  10 km          │  (___.__)__)  10 km          │  (___.__)__)  10 km          │    /(___(__)  10 km          │
    │               0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
    Emplacement: Amsterdam, Centrum, Amsterdam, MRA, Stadsregio Amsterdam, Noord-Holland, Nederland [52.3745403,4.89797550561798]