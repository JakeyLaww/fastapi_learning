See information at:

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

## Advantages of Annotated

Using Annotated is recommended instead of the default value in function parameters, it is better for multiple reasons. 🤓


The default value of the function parameter is the actual default value, that's more intuitive with Python in general. 😌


You could call that same function in other places without FastAPI, and it would work as expected. If there's a required parameter (without a default value), your editor will let you know with an error, Python will also complain if you run it without passing the required parameter.


When you don't use Annotated and instead use the (old) default value style, if you call that function without FastAPI in other places, you have to remember to pass the arguments to the function for it to work correctly, otherwise the values will be different from what you expect (e.g. QueryInfo or something similar instead of str). And your editor won't complain, and Python won't complain running that function, only when the operations inside error out.


Because Annotated can have more than one metadata annotation, you could now even use the same function with other tools, like Typer. 🚀

## Custom Validation

If you need to do any type of validation that requires communicating with any external component, like a database or another API, you should instead use FastAPI Dependencies, you will learn about them later.

These custom validators are for things that can be checked with only the same data provided in the request.

## Recap

You can declare additional validations and metadata for your parameters.


Generic validations and metadata:

* alias
* title
* description
* deprecated


Validations specific for strings:

* min_length
* max_length
* pattern
* Custom validations using AfterValidator.


In these examples you saw how to declare validations for str values.

See the next chapters to learn how to declare validations for other types, like numbers.