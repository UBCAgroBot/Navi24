FROM nvcr.io/nvidia/l4t-base:r36.2.0

# Install dependencies for Conda
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda for Python environment management
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh

ENV PATH="/opt/conda/bin:$PATH"

COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml && conda clean -a

RUN echo "source activate base" > ~/.bashrc
ENV PATH /opt/conda/envs/base/bin:$PATH

COPY main.py /workspace/main.py
WORKDIR /workspace

CMD ["python", "main.py"]
