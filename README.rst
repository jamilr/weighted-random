``choices.py`` - a Numpy-compatible implementation of weighted random number generator.

``Choices(population, weights)``

Choice class takes the population and the weights array as input arguments.
The ``weights`` argument is an array of weights assigned to each element in the population array
If the weights is omitted, the uniform weights are used - each element has an equal likelihood of being generated.

