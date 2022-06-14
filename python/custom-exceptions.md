# Custom exceptions

Exceptions are a way to deal with errors in your code.

For example imagine that you have a function that saves some data to the disk. And when the program executes, the disk happens to be full. In that case, an exception is "raised" (or "thrown"). Imagine it like an alternative result-value from your function.

In areas where the function is called, you can "catch" those exceptions and do something sensible. For example, in the case of a disk full, show an error to the user that says: "Error: Disk is full" or something similar.

**Any exception that is not caught will cause the program to crash and exit**.

So clearly, handling (catching) them and doing something other than crashing is nicer for the end-user.

Python comes with [some standard/builtin exceptions](https://docs.python.org/3/library/exceptions.html#exception-hierarchy). Each exception has a well defined reason why it might be thrown.

If those "builtin" exceptions are not appropriate for your own program, you can define your own. This is done by creating a new class inheriting from "Exception".

For example, let's say your program that creates files on disk only gives a user the permission to store 1GB of data. Everything above "exceeds the quota". The disk is still not full, so that error is not appropriate. So we need something else.

In that case we can create such a subclass:

```python
class QuotaExceeded(Exception):
    pass
```

And then use it:

```python
def store_file(user, file):
    quota = get_quota(user)
    used_diskspace = get_used_diskspace(user)
    filesieze = get_filesize(file)
    if (used_diskspace + filesize) > quota:
        raise QuotaExceeed(
            f"The file {file} would exceed the disk quota for {user}. "
            f"Currently {used_diskspace} out of {quota} is used. "
            f"Filesize: {filesize}"
        )
    store_file_to_disk(user, file)
```

The `raise` line in the if-block will immediately stop executing that function and "throw" that custom `QuotaExceeded` error. It can then be caught using the `try/except` block:

```python
try:
    store_file(john_doe, uploaded_file)
except QuotaExceeded as exc:
    print(exc)
```

If that `try/except` block would not exist, the program would crash. 

Sometimes you want your program to crash out instead of being in an "unknown/unpredictable" state. That's when exceptions come in handy.

To add to the example above, you can make custom exceptions more useful by adding a docstring and by storing useful context-values in the exception itself. For example:

```python
class QuotaExceeded(Exception):
    """
    This exception is raised if an operation would cause more disk-space
    to be used than is allowed for a given user.
    """
    def __init__(self, file, user, used_diskspace, quota, filesize):
        super().__init__(
            f"The file {file} would exceed the disk quota for {user}. "
            f"Currently {used_diskspace} out of {quota} is used. "
            f"Filesize: {filesize}"
        )
        self.file = file
        self.user = user
        self.used_diskspace = used_diskspace
        self.quota = quota
        self.filesize = filesize

def store_file(user, file):
    quota = get_quota(user)
    used_diskspace = get_used_diskspace(user)
    filesieze = get_filesize(file)
    if (used_diskspace + filesize) > quota:
        raise QuotaExceeed(file, user, used_diskspace, quota, filesize)
    store_file_to_disk(user, file)
```

And finally, exceptions are one of those topics where people like to argue about whether or not they are good. There are valid arguments for both ways. To avoid unnecessary digression and complexity, all I will say is that you could rewrite the code above with `if` statements to something like this:

```python
def store_file(user, file):
    quota = get_quota(user)
    used_diskspace = get_used_diskspace(user)
    filesieze = get_filesize(file)
    if (used_diskspace + filesize) > quota:
        return (
            f"The file {file} would exceed the disk quota for {user}. "
            f"Currently {used_diskspace} out of {quota} is used. "
            f"Filesize: {filesize}"
        )
    store_file_to_disk(user, file)
    return ""

error_message = store_file(john_doe, uploaded_file)
if error_message:
    print(error_message)
```
