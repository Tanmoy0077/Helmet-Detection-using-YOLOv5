
# Helmet detection Using YOLOv5

This project centers on the development of a robust Helmet Detection System designed to enhance road safety by identifying instances of riders not wearing helmets from live traffic footage. The system leverages the cutting-edge YoloV5 model, which has been meticulously trained on a comprehensive dataset comprising 14 thousand images.



## Dataset Description
The HELMET dataset contains 910 videoclips of motorcycle traffic, recorded at 12 observation sites in Myanmar in 2016. Each videoclip has a duration of 10 seconds, recorded with a framerate of 10fps and a resolution of 1920x1080. The dataset contains 10,006 individual motorcycles, surpassing the number of motorcycles available in existing datasets. Each motorcycle in the 91,000 annotated frames of the dataset is annotated with a bounding box, and rider number per motorcycle as well as position specific helmet use data is available.

The HELMET dataset contains:
- “image" folder: contains 910 annotated video clips, each video clip has 100 frames (10 second x 10 fps) with 1920 x 1080 resolution.
- “data_split.csv”: contains indices of data splitting for training, validation and testing. 
- “annotation.zip”: contains annotation for each video clips, where the name of each annotation file (.csv) corresponds to the video clip in the “image” folder. In each annotation file, track_id corresponds to the unique tracking id of a motorcycle, frame_id correspond to the frame number (1 to 100) it appears, and with a bounding box (x, y, width, height) and annotated helmet use class. 
- “F-measure.zip”: contains the matlab scripts and an example about how to evaluate weighted F-measure of a proposed model.

