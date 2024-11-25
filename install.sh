apt-get update && \
    apt-get install -y ros-humble-rosbridge-suite python3-opencv python3-serial python3-rosdep ros-humble-cv-bridge && \
    rm -rf /var/lib/apt/lists/*

rosdep init && rosdep update

pip install omegaconf
