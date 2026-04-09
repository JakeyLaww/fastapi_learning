## Technical Details

Actually, Query, Path and others you'll see next create objects of subclasses of a common Param class, which is itself a subclass of Pydantic's FieldInfo class.

And Pydantic's Field returns an instance of FieldInfo as well.

Body also returns objects of a subclass of FieldInfo directly. And there are others you will see later that are subclasses of the Body class.

Remember that when you import Query, Path, and others from fastapi, those are actually functions that return special classes.

## Add extra information

You can declare extra information in Field, Query, Body, etc. And it will be included in the generated JSON Schema.

You will learn more about adding extra information later in the docs, when learning to declare examples.

## Recap

You can use Pydantic's Field to declare extra validations and metadata for model attributes.

You can also use the extra keyword arguments to pass additional JSON Schema metadata.