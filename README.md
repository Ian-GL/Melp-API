# Melp-API
REST API in Python using Flask and SQLAlchemy

This API lets you make CRUD operations with HTTP verbs.

The libraries that are used are Flask and SQLAlchemy. Both of them can be installed through pip.

The API connects to a local database that in this case is in .sqlite format. The file should be in the same folder for it to work (or you could store it in another part as long as you update the path).

In this case the example database is restaurants.sqlite (which is also in the repository). The functions that are implemented now are the reading of the full database, the creation of a row and the individual read, update or deletion of a row based on its id.

What each part of the code does is explained as comments.
