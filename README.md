# BioComp site

This is a develop branch.

To start contributing, first checkout main repository:
```console
$ git clone git@github.com:BioComp-USP/biocomp-usp.github.io.git
```

After that, enter master branch and checkout `source` branch:
```console
$ cd biocomp-usp.github.io.git
$ git checkout -b source
```

Change your stuff. If you have commit authorization to master, just do:
```console
$ make publish && make github
```

Otherwise please create a push request. Do not forget to commit and push your changes on source to the `source` branch.
