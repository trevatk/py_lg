# PY LG

example project using fastapi to serve a health check with unit test

## Commands

### init

you can use the `make init` command to install all requirements for this project
```bash
    make init
```

### build

This command will build a docker image using the application source code and expose port 9091 of the container. The container will be tagged `trevatk/py_lg:latest`
```
    make build
```

### lint

This project uses python black to enforce code style and be run quickly using
```bash
    make lint
```

### Test

performing unit tests is an important part of every application. This shows your code does work should be used as much as possible. You can perform a unit test for the server using
```bash
    make test
```