# Instructions to Use the Video Creation Scripts

## Project: La escuela donde volví a soñar

This document provides step-by-step instructions on how to utilize the video creation scripts for the "La escuela donde volví a soñar" project.

### 1. Prerequisites
Before running the scripts, ensure you have the following software installed:
- Python 3.7 or higher
- FFmpeg
- Required Python packages (See Installation section)

### 2. Installation
To set up the project, follow these steps:
- Clone the repository:
  ```bash
  git clone https://github.com/cronothopos-glitch/PTA.git
  cd PTA
  ```
- Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Using the Scripts
To create videos:
- Navigate to the script directory:
  ```bash
  cd scripts
  ```
- Run the desired script with the following command:
  ```bash
  python create_video.py [options]
  ```
- Options include:
  - `--input`: Specify the input directory of assets.
  - `--output`: Specify the output directory for the generated videos.
  - `--template`: Choose the video template to use.

### 4. Sample Command
An example command to create a video might look like this:
```bash
python create_video.py --input ./assets --output ./videos --template template1
```

### 5. Troubleshooting
If you encounter issues, consider the following:
- Ensure all path directories are correctly set.
- Check for any missing dependencies and install them.
- Review error messages for guidance.

### 6. Contact
For further assistance, please reach out to the project maintainer at cronothopos@gmail.com.

### 7. License
This project is licensed under the MIT License - see the LICENSE file for details.