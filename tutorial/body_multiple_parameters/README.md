## Body - Multiple Parameters

Now that we have seen how to use Path and Query, let's see more advanced uses of request body declarations.

## Recap

You can add multiple body parameters to your path operation function, even though a request can only have a single body.

But FastAPI will handle it, give you the correct data in your function, and validate and document the correct schema in the path operation.

You can also declare singular values to be received as part of the body.

And you can instruct FastAPI to embed the body in a key even when there is only a single parameter declared.