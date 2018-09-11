# Gaze intelligent video cloud service
The Gaze Real-Time Video Analytics Service Platform integrates the computing power of private clouds with data from IoT devices such as cameras, providing scalable, scalable video analytics on the Edge.

# Overview
Today's society is full of cameras. According to statistics, 85% of the data on the Internet is video data, and it is still growing rapidly. When people talk about big data and IoT devices, big data mainly refers to video data, and IoT devices mainly refer to cameras. But has massive data been fully exploited and utilized? The answer is limited by video analysis capabilities, which are like dark matter and far from being used effectively.

According to a low-definition camera, the amount of video accumulated per day is 1.5G, and in HD, it is 15G. If a mall has a hundred cameras installed, the amount of data is T-level. If you pass this data to the public cloud, it is an attack, not a use. Therefore, video analysis on the public cloud will not be worth the candle, but it is a perfect combination with the private cloud.

With this in mind, we propose Gaze to integrate the computing power of private clouds with data from IoT devices such as cameras. Provides scalable, scalable video analysis capabilities at the Edge. For developers, if there is a need for video analysis, we can convert some video streams into event streams based on our pre-built "building blocks" by simple statements, and pass them through event hub and Kafka. Downstream.

# Architecture

![image](https://github.com/foamliu/Gaze/raw/master/images/architecture.svg?sanitize=true)

# Dataflow

![image](https://github.com/foamliu/Gaze/raw/master/images/dataflow.svg?sanitize=true)

# Quick start

## Dev environment
```bash
$ python demo.py
```

## Docker container
In Linux VM:
```bash
$ git clone https://github.com/foamliu/Gaze.git
$ sudo docker build -t="gaze0.0.1" . 
$ sudo docker run --name=gaze0.0.1 -p 5000:5000/udp -it -v <mount-dir>:/usr/src/gaze/output gaze0.0.1 /bin/bash
$ python app.py
```

You can send video stream to the VM via UDP at port 5000 and then you can see output.avi in mount-dir.

## K8s cluster
In master node:
```bash
$ kubectl run gazepod --image=wenhuorongbing/gaze0.0.6 --port=5000
$ kubectl expose deployment gazepod --port=5000 --target-port=5000 --protocol=UDP --type=LoadBalancer
```

Or you can use the yaml file in the source code:
```bash
$ kubectl apply -f gaze.yaml
```

Then get the external IP by kubectl get svc and send video stream to that IP.
You can use kubectl exec -it <pod-name>  --/bin/bash to access the pod to see if it works.

# Portal 

We can easily deploy a gaze project by uploading the source code and clicking “deploy” button.

![image](https://github.com/foamliu/Gaze/raw/master/images/upload.PNG)

It could automatically package the gaze project to docker image and push the image to the docker hub.
Finally, it could generate a yaml file and deploy it on azure stack.

![image](https://github.com/foamliu/Gaze/raw/master/images/homepage.PNG)


