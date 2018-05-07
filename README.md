# Django practice nº 2

### Setup Instruction

```bash
$ mkvirtualenv -p $(which python3) django_practice_2
$ pip install -r requirements.txt
$ make migrate
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```


### Your Tasks

The structure of the whole Django project is built for you. Your job will be divided into three parts and multiple tasks for each part. You have to focus on implementing models inside `models.py`, a couple of views inside `views.py`, some URLs inside `urls.py` and templates in the `templates` folder.

If you run the development server with `$ make runserver`, you'll be able to test your views in the browser pointing to `http://localhost:8080/<some-path>`.


#### Part 1

Once you have your virtualenv setup with all the requirements installed and the Django migrations migrated, there is one more step that you need to do. We will run a command that loads some testing data into our database. You can run it by doing:

```bash
$ make load_initial_data_1
```

You should see an `Imported!` message when the command execution finishes. That mean all initial data was imported successfully. You'll now have a superuser created with username `admin` and password `admin`, so you can access the admin site via `http://localhost:8080/admin/`.

##### - Task 1:

A Django model called `Artist` is provided to you as an example inside `artists/models.py`. For this task you'll have to implement a view inside `artists/views.py` that matches with `/artists` URL located in `django_practice_2/urls.py`.
This view will be in charged of fetching all `Artist`'s objects stored in the database (previously loaded with the given script) and render the `artists.html` template sending all `artists` as context.

You can test the response of the view in your browser, pointing to `http://localhost:8080/artists/`. This is the expected result:

<img src="https://user-images.githubusercontent.com/2788551/39497571-5071116c-4d7a-11e8-9659-3edcc9a4ee20.png" width="50%" height="50%">


##### - Task 2:

In this task you'll extend the previous view with some functionality. The idea is to filter the list of artists by name sending GET parameters in the URL (i.e: `/artists?first_name=stev`).
For this, check if a `first_name` GET parameter is sent inside `request.GET` dictionary. If so, filter the previous artists queryset that had ALL artists, in order to filter only the ones that contains the given pattern in their first_name.
The context while rendering the template will be the same as before, but now the artists queryset might have less artists than before, if a `first_name` parameter is given. The following image shows the expected result:

<img src="https://user-images.githubusercontent.com/2788551/39497588-65a6b6e0-4d7a-11e8-8f3b-4c5bbfb9cbfc.png" width="50%" height="50%">


##### - Task 3:

In a similar way as done before, check if a `popularity` GET parameter is given in the URL and if so, filter the artists queryset by artists that have a popularity greater or equal to the one given.
It should work like this:

<img src="https://user-images.githubusercontent.com/2788551/39497601-7892d2b6-4d7a-11e8-8dfd-b658262a7146.png" width="50%" height="50%">


##### - Task 4:

For this task you'll implement a brand new view under `/artist/<artist_id>` URL. This view will take the given `artist_id`, get the proper Artist object from the database and render the `artist.html` template sending the artist object as context.
If you want to check what id is associated with each artist, you can do it in the admin page at `/admin/` URL.

<img src="https://user-images.githubusercontent.com/2788551/39497626-9f1ee55a-4d7a-11e8-94fe-b0f81c0e6c14.png" width="50%" height="50%">


#### Part 2

##### - Task 1:

Add a new `genre` field to the `Artist` model inside `/artists/models.py`. The field's type has to be CharField and in this case it will have some `choices` options ([read docs here](https://docs.djangoproject.com/en/2.0/ref/models/fields/#choices)) with different music genres.

After adding the new field, a migration must be created and applied so the changes are reflected in the database. Run this commands in order to do that:

```bash
$ make makemigrations
```

This will create a new Migration file, which will include the creation of the `genre` field we've just created in the `Artist` model. When you run this command, it's expected to get a message like this:

```bash
You are trying to add a non-nullable field 'genre' to artist without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:
```

Let me explain what that means. If you remember from previous steps, we've already loaded some data into our database. That means we already have a few instances (3 to be more precise) of the `Artist` model saved in our database. All those 3 instances **don't have** a set value for the new `genre` field we've just added. What Django is asking here is: "What should I use as `genre` value for all those 3 instances that we already have in the DB?". Option 1) will set the value you specify as `genre` for all current instances in the db, and Option 2) will exit and let you do changes manually or specify a default value in the Model field. For this project, it's enough to specify a one-off value, like `"rock"` (it must be a valid values included in the choices).

So, type `1` and hit `Enter` to select Option 1, then type `"rock"` and hit `Enter` again to set the default value for all db rows. That's it! Our new migration should be in place. 🎉

Finally, run the new migration so all changes are applied to the database.

```bash
$ make migrate
```

As some changes have been made to the `Artist` model, there's a second script that loads initial data again with the changes applied. Run then like this:

```bash
$ make load_initial_data_2
```

##### - Task 2:

Just as done before, add a new `genre` filter to the `artists()` view when a genre is given as GET parameter. When a genre is given, filter the artists queryset by those who match with that genre and send the queryset as context in the same way as before.

<img src="https://user-images.githubusercontent.com/2788551/39499701-05a50cc2-4d86-11e8-8f99-d31772856b41.png" width="50%" height="50%">

NOTE: Notice that you can send multiple GET parameters like this: `/artists?genre=rock&popularity=80`


#### Part 3

##### - Task 1:

In this task you will implement a brand new `Song` model with three fields:
  - artist_id (type: integer)
  - title (type: char)
  - album_name (type: char)
As every time any change is made in a model, a migration must be created. Run this commands as before:

```bash
$ make makemigrations
$ make migrate
```

In order to have initial data for the new model, another script is provided to you. Run it like this:

```bash
$ make load_initial_data_3
```

##### - Task 2:

Implement a view under `/songs` URL that display ALL the songs stored in the database. In order to do this, fetch all the Song objects and render the `songs.html` sending the 'songs' queryset as context.
Before rendering the template, loop through the songs queryset and for each song, fetch the proper Artist object from the database that matches with the artist_id in the song. Once you have the song's artist object, bind it to the song object like 'song.artist = artist'.

<img src="https://user-images.githubusercontent.com/2788551/39501114-572f33d4-4d8f-11e8-8c2c-e6316512e8da.png" width="50%" height="50%">

##### - Task 3:

Add a `title` filter to the `songs()` view that takes 'title' GET parameter (if given) and filters the 'songs' queryset for songs that contains that pattern, in a similar way that the tasks before.

<img src="https://user-images.githubusercontent.com/2788551/39501513-be973218-4d91-11e8-96c9-f43836cc1b42.png" width="50%" height="50%">


##### - Task 4:

Add a new `/songs/<artist_id>` URL that points to the same `songs()` view. Filter the songs queryset for songs that match with given artist_id and render the same `songs.html` template.
Notice that this is NOT a GET parameter, but a parameter that comes in the URL path. So now the `songs()` view takes a new artist_id parameter which by default is set to None.
Remember that you can check which `id` is associated with each artist object in the Django admin page.

<img src="https://user-images.githubusercontent.com/2788551/39501602-401e5eb0-4d92-11e8-92a8-9fd1d5e3e1cb.png" width="50%" height="50%">
