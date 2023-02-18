# DevSearch

## About Us

DevSearch is the place you can connect with excellent developers around the world and have a chance to know about their outstanding projects. This platform aims the create a strong community where you can show your work with the world and have chances to have jobs.

If you are an employer, DevSearch will recommends to you the most outstanding developers in the field you need. This tool provides the most handful features which makes your searching become easier!

## Get Started

* Create a virtual environment and activate

```
pip install virtualenv
virtualenv envname
source envname/bin/activate
```

* Install required modules

```
pip install -r requirements.txt
```

## Environment variables

The `.env.dist` file describes the mandatory variables for the application, and it can be committed to version control. This provides a useful reference and speeds up the on-boarding process for new team members, since the time to dig through the codebase to find out what has to be set up is reduced. 

> **_NOTE:_** Please make sure that you have enough required variables in the `.env.dist` file and create your `.env` file before running the application.

## Amazon S3

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere.

> **_NOTE:_** Please make sure that you have your own Amazon S3 access key and secret key. For more information, please follow the instruction about using S3 from AWS [here](https://aws.amazon.com/s3/getting-started/).

DevSearch uses [django-storages](https://django-storages.readthedocs.io/en/latest/) library to connect with Amazon S3. This library is a collection of custom storage backends for Django.

## Database

DevSearch uses [Psycopg](https://www.psycopg.org/docs/) as PostgreSQL adapter to ensure the performance. Documentation is included in the doc directory and is [available online](https://www.psycopg.org/docs/).

> **_NOTE:_** For any other resource (source code repository, bug tracker, mailing list) please check the [project homepage](https://www.psycopg.org/).

## Bugs and Issues

Have a bug or an issue with this template? [Open a new issue](https://github.com/minhtran241/devsearch/issues) here on GitHub.

## Copyright and License

Code released under the [MIT](https://github.com/minhtran241/devsearch/blob/main/LICENSE) license.
