# ROYALE-ETL
En el presente proyecto se busca consolidar todos los conocimientos asimilados, necesarios para construir una ETL. Es decir, se elaborará un **pipeline** que realice el proceso en el cual. Se **extrae (E)** información de una fuente predeterminada. Una vez extraída esta información se **transforma (T)** en datos y se le da el formato adecuado. Finalmente, se cargan los datos, o en inglés **load (L)**, en el lugar correspondiente para ser usados.

## Resumen del proyecto 

En particular, en esta ETL emplearemos como escusa el juego de cartas Clash Royale. Ya que, la información en los juegos es más fácil de manejar gracias a sus reglas bien definidas. Presuponemos entonces que el resultado final de esta ETL podrá ser utilizado para elaborar estrategias en el juego, basándose en los datos de las cartas.

Para obtener la información emplearemos **web scraping** en la wiki del juego donde se documenta toda lo relacionado con Clash Royale. Posteriormente, organizaremos toda la información en un archivo .csv, el cual se empleara para la transformación de la información con la ayuda de **Pandas**. Como paso final, emplearemos la librería **Psycopg2** para cargar la información en un **data base** que emplea el motor **PostgreSQL** para funcionar.

## Tecnologías usadas 
* Python

 ![Logo python](https://raw.githubusercontent.com/CristianPrietoAvella/error/ROYALE-ETL/logo_python.png)
 
 * Scrapy
 
 ![Logo  scrapy](https://raw.githubusercontent.com/CristianPrietoAvella/error/ROYALE-ETL/scrapy_logo.png)
 
 * Pandas
 
 ![Logo python](https://raw.githubusercontent.com/CristianPrietoAvella/error/ROYALE-ETL/Pandas_logo.png)
 
 * PostgreSQL
 
 ![Logo python](https://raw.githubusercontent.com/CristianPrietoAvella/error/ROYALE-ETL/postgresql-logo.png)
