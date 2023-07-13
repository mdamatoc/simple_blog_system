# Simple Blog System

This is a simple blog system that allows users to create and manage blog posts and comments.

## Architecture

The application follows a clean architecture design, with the following components:

- `entities`: Contains the entity classes representing the core domain objects such as `Blog` and `Comment`.
- `interfaces`: Contains the interface definitions for the repositories.
- `infrastructure`: Contains the implementation of the repositories, providing the data storage and retrieval logic.

## Dependencies

The application requires the following dependencies:

- Python 3.x
- `unittest` module (for running the tests - does not require to be installed because it's built-in.)

## Installation

1. Clone the repository:

git clone https://github.com/mdamatoc/simple_blog_system.git

There is no need to install any requirements because all the libraries used in the application are built-in.


2. Navigate to the project directory:

cd simple-blog-system


3. (Optional) Create a virtual environment:

`python3 -m venv venv`
`source venv/bin/activate`



## Usage

To run the application, execute the `main.py` file:

`python main.py`


The `main.py` file provides an example of creating and retrieving blog posts and comments using the provided repositories.

## Tests

The application includes unit tests to ensure the functionality of the repositories. The tests are implemented using the `unittest` framework.

To run the tests, use the following command:

`python -m unittest tests/*`


The test cases cover various scenarios, including saving and retrieving blogs/comments, retrieving non-existent entities, and deleting entities.

## License

This project is not licensed.
