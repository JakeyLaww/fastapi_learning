## Recap

With Query, Path (and others you haven't seen yet) you can declare metadata and string validations in the same ways as with Query Parameters and String Validations.

And you can also declare numeric validations:

* gt: greater than
* ge: greater than or equal
* lt: less than
* le: less than or equal

## Info 

Query, Path, and other classes you will see later are subclasses of a common Param class.

All of them share the same parameters for additional validation and metadata you have seen.

## Technical Details

When you import Query, Path and others from fastapi, they are actually functions.

That when called, return instances of classes of the same name.

So, you import Query, which is a function. And when you call it, it returns an instance of a class also named Query.

These functions are there (instead of just using the classes directly) so that your editor doesn't mark errors about their types.

That way you can use your normal editor and coding tools without having to add custom configurations to disregard those errors.