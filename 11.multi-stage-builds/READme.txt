Build-only Images
    The images that don't spin up their own server.
    Such images create the optimised build and then serves it on a server through Multi_stage Build

Multi-Stage build
    Dockerfile with 2 or more FROM instructions.
    Latest FROM overwrites the previous base image.
    (Refer to the 2 Dockerfiles in the ./frontend/)
    Normal one creates the development server and run the code without optimizing and compressing it.
    Dockerfile.prod creates a build (optimized and compressed) of code and setups a server that executes that build.