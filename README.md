# Django practice nº 3

### Setup Instructions

```bash
$ mkvirtualenv -p $(which python3) django_practice_3
$ pip install -r requirements.txt
$ make migrate
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```


### Your Tasks

The structure of the whole Django project is already built for you. Your job will be divided in two parts and multiple tasks for each part.

If you run the development server with `$ make runserver`, you'll be able to test your views in the browser pointing to `http://localhost:8080/<some-path>`.


#### Part 1 - Working with HTML Forms

The main goal of this part is to learn how to work with HTML Forms and handle inside the views the data that you send via the POST HTTP method.

The very first thing that we'll ask you to do, is to connect the `Song` and `Artist` models to each other. If you remember from last practice, the `Song` model was "linked" to the `Artist` by an `artist_id`, which was an `IntegerField`. Now we want you to link both models by a `ForeignKey` so you can use all the advantages that Django provides with that type of association.

Once the `Song` model is connected to the `Artist` by a `ForeignKey`, you'll need to create a new Migration and apply it, by doing:

```bash
$ make makemigrations
$ make migrate
```

There's a script provided for you that loads some initial data, so you can start with some objects stored in the database. You can run it by doing:

```bash
$ make load_initial_data
```

There's also an example done for you that you can check under `http://localhost:8080/artists/`. You will find a list of artists with their songs, and a form to create a new Song for an Artist. It will look like this:

<img src="https://user-images.githubusercontent.com/2788551/39730245-de2b83aa-5236-11e8-9a2b-059961c5a16c.png" width="50%" height="50%">

Your task is building a Form for adding a new Artist to the list, and another one for deleting it. Both of those actions must have their views and URLs associated.

After adding the `artist` ForeignKey field to the `Song` model, implementing the views with their URLs and completing the `templates/index.html` template with the extra two forms, the result must look something like this:

<img src="https://user-images.githubusercontent.com/2788551/39729145-b244d94a-5230-11e8-9f05-32876120cd30.png" width="50%" height="50%">

Remember to validate inside the view that all the model's required fields have been sent from the form.
Just as a hint, notice that all data sent by a POST method from a form is type 'string'. So for example in the view, you will have the convert the `popularity` that you receive in `request.POST` from a string to an integer, which is the type that the model is asking for when you try to save it.


#### Part 2 - ORM exercises

For this part of the practice you will work inside the `artists/orm_exercises.py` file. You'll find there a couple of functions that are the tasks you have to implement, using the different ORM methods that are provided by the Django `objects` manager.
Each of the task has its instructions as a docstring, so use them as a guide to know what you have to do.

In order to check if you implemented them correctly, there are tests associated to each task inside the `artists/tests.py`. You can run the tests like this:

```bash
$ make test
```
