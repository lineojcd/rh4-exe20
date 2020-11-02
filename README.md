# Duckietown RH4 Exe20


### Instructions to reproduce results

### 1. Clone this repository and go to its directory
```bash
git clone https://github.com/lineojcd/rh4-exe20.git
cd rh4-exe20
```
### 2. Build docker image
```bash
dts devel build -f --arch amd64 
```

### 3. Run docker image with the following options
```bash
docker run -it --rm --net host -v [PATH_TO_BAG_FOLDER]:/code/catkin_ws/src/exercise20/mounted_volume duckietown/exercise20:v1-amd64 /bin/bash
```

### 4. After going inside the docker shell, run the python script using the command below
```bash
python3 packages/process_image.py mounted_volume/[BAG_FILE_NAME]
```
The processed image bag file will be saved inside the mounted volume.
