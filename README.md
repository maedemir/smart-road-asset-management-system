# Smart Road Asset Management System

This repository contains the code for my B.Sc. Final Project in Computer Engineering at Amirkabir University of Technology. The project focuses on developing a smart system for managing road assets using advanced computer vision and machine learning techniques. The aim is to automate the detection and evaluation of road conditions to assist in efficient maintenance and planning.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Future Work](#future-work)
- [Credits](#credits)
- [License](#license)

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

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Smart-Road-Asset-Management-System.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Smart-Road-Asset-Management-System
    ```

3. **Install dependencies:**

    Ensure you have Python 3.8+ installed. Then run:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment:**

    Modify the configuration files (if any) to set paths for your datasets, models, and output directories. Make sure to configure the connection to your PostGIS database.

## Usage

Run the main script to start the system:

```bash
python src/main.py
