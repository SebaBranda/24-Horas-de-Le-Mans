# 24-Horas-de-Le-Mans

![LeMans](LeMans.jpg)

Dadas las condiciónes actuales de Pandemia a nivel mundial, los organizadores de las famosas 24 horas de Le Mans, nos piden desarrollar un programa en el que se evidencie el estricto comportamiento de la gente de los Boxes, no quieren que ingresen en simultaneo mas de cierta cantidad de autos para evitar aglomeración de gente en los pits y de esta forma mantener el distanciamiento social. Es por eso que se ve limitada de antemano el ingreso a la zona de Boxes y los competidores deberán seguir corriendo una vuelta mas en la pista, hasta tanto no se les habilite el ingreso a los mismos.

Si bien en una carrera de Le Mans los pits estan abiertos siempre, puesto que es una carrera de 24 horas continuas, en esta versión decidí acotar esa cantidad, aunque si bien el ejercicio se podría resolver utilizando colas, esto no representaría fehacientemente el hecho de que los "autos" compitan, ademas de en la pista, para ingresar a los pits, puesto que no todos lo podrán hacer. 

La ventaja y necesidad de utilizar concurrencia en este caso, se da en que los diferentes procesos se mantienen constantemente corriendo y en cualquier momento podrán acceder a la otra parte del programahaciendolo mas dinámico, a diferencia de una cola que relantizaria este proceso por el orden de llegada y ya no sería una competencia, sino un ordenamiento.
