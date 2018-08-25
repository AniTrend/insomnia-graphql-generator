# Insomnia Collection GraphQL Generator &nbsp; &nbsp; [![Waffle.io - Columns and their card count](https://badge.waffle.io/AniTrend/insomnia-graphql-generator.svg?columns=all)](https://waffle.io/AniTrend/insomnia-graphql-generator) &nbsp; [![license](https://img.shields.io/badge/license-GPL-green.svg?style=flat-square)](https://github.com/AniTrend/insomnia-graphql-generator/blob/master/LICENSE)

Small application to help you generate .graphql files from a GraphQL export workspace in insomnia so you can use it in projects like [Apollo](https://www.apollographql.com/]) or [retrofit-graphql](https://github.com/AniTrend/retrofit-graphql) for android.

## How To Use

Obviously firstly you must have [Insomnia](https://insomnia.rest/) installed and preferably isolate your GraphQL queries into their own separate Work Space which you will export. As shown in the image below:

![Work Space Example](https://insomnia.rest/static/drag-ab3bee8a8fe203bb66cd1143dd89e6d3-a7281.webp)
____

![Folder or Collection Example](https://insomnia.rest/static/main-ac0a1732afac19acce5ad6825595c3bb-9a259.webp)

__N.B.__ The utility can work with up to 3 nested folders _Tested_ in a given workspace. Which means in the image above To-Dos can have upto 3 levels of directories with requests

## Usage

For all available options you can run the following command:
```commandline
python manage.py --help
```

All generated files will be saved in the `./app/io/output`
