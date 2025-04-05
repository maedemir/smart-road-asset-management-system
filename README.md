# Smart Road Asset Management System

This repository contains the code for my B.Sc. Final Project in Computer Engineering at Amirkabir University of Technology. The project focuses on developing a smart system for managing road assets using advanced computer vision and machine learning techniques. The aim is to automate the detection and evaluation of road conditions to assist in efficient maintenance and planning.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Results](#results)
- [Dataset](#Dataset)

## Overview

**Smart Road Asset Management System** is designed to:
- Automatically detect and classify road assets (e.g., traffic signs, potholes, barriers) from images.
- Integrate geospatial data with detection results for a comprehensive asset management solution.
- Utilize ZoeDepth for monocular depth estimation, providing depth cues from single images.
- Store and visualize detected assets using QGIS and PostGIS for detailed spatial analysis.
- Provide a user-friendly visualization interface for stakeholders to review asset conditions and plan maintenance activities.

This project leverages state-of-the-art techniques such as deep learning-based object detection, image processing, GIS integration, and advanced depth estimation to address real-world challenges in infrastructure management.

## Features

- **Automated Detection:** Uses advanced object detection algorithms to identify various road assets.
- **Monocular Depth Estimation:** Integrates ZoeDepth to estimate depth from single images.
- **Geospatial Integration:** Combines detection results with geographic data and stores them in PostGIS, enabling robust spatial queries.
- **Visualization:** Uses QGIS for visualizing detected assets and detailed geospatial analysis.
- **User-friendly Interface:** Provides clear visualizations and reports for quick decision-making.
- **Scalable Architecture:** Designed to process large datasets and adaptable to various environments.

## project-structure
- For the object detection model fine-tuning, check the [YOLOv5 training notebook](https://github.com/maedemir/smart-road-asset-management-system/blob/main/yolov5s6%20(1).ipynb)
- For ZoeDepth + YOLOv5 integration, check the [ZoeDepth&Yolov5s notebook](https://github.com/maedemir/smart-road-asset-management-system/blob/main/ZoeDepth%26Yolov5s%20(1).ipynb)
- For storing the info in postGIS database, check the [postgis.py](https://github.com/maedemir/smart-road-asset-management-system/blob/main/postgis.py)
- For conversion of pixel coordinate to real-world coordinate check [camera-pose.py](https://github.com/maedemir/smart-road-asset-management-system/blob/main/camera-pose.py)

## Results

<img width="592" alt="image" src="https://github.com/maedemir/smart-road-asset-management-system/assets/72692826/a557429b-3021-4fec-8663-42eb87e7a050">

## Depth Estimation Using ZoeDepth
<img width="610" alt="image" src="https://github.com/maedemir/smart-road-asset-management-system/assets/72692826/951e88f0-2bb8-454a-be11-609918fb515f">
<img width="440" alt="image" src="https://github.com/maedemir/smart-road-asset-management-system/assets/72692826/db105ba8-f618-4720-9395-934cfd187cd8">

## QGIS Visualization of Assets
<img width="596" alt="image" src="https://github.com/maedemir/smart-road-asset-management-system/assets/72692826/0b46ba0d-6c51-4f30-93b0-e15e322fb5ba">


## Dataset

For accessing the dataset, please contact me: maedemir@student.ubc.ca
