FROM osgeo/gdal

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip

COPY requirements.txt requirements.txt

RUN ["pip3", "install", "-r", "requirements.txt", "--no-cache-dir"]

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]