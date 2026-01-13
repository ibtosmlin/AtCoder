FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/local/bin:/root/.cargo/bin:${PATH}"

# =========================
# 基本ツール + ロケール
# =========================
RUN apt update && apt install -y --no-install-recommends \
    locales \
    build-essential \
    g++ \
    clang \
    git \
    curl \
    wget \
    unzip \
    ca-certificates \
    vim \
    libbz2-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev \
    liblzma-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# 日本語ロケール
RUN locale-gen ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8
ENV LANGUAGE=ja_JP:ja
ENV LC_ALL=ja_JP.UTF-8

# =========================
# Python 3.13.7（公式ビルド）
# =========================
RUN wget https://www.python.org/ftp/python/3.13.7/Python-3.13.7.tgz && \
    tar xzf Python-3.13.7.tgz && \
    cd Python-3.13.7 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make install && \
    cd / && rm -rf Python-3.13.7*

# python3 を 3.13 に切り替え
RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.13 1

RUN python3 -m ensurepip && \
    python3 -m pip install --upgrade pip setuptools wheel

# =========================
# PyPy 3.11（公式バイナリ・固定）
# =========================
RUN wget https://downloads.python.org/pypy/pypy3.11-v7.3.19-linux64.tar.bz2 && \
    tar -xjf pypy3.11-v7.3.19-linux64.tar.bz2 && \
    mv pypy3.11-v7.3.19-linux64 /opt/pypy3.11 && \
    ln -s /opt/pypy3.11/bin/pypy3 /usr/local/bin/pypy3 && \
    ln -s /opt/pypy3.11/bin/pypy3 /usr/local/bin/pypy3.11 && \
    rm pypy3.11-v7.3.19-linux64.tar.bz2

RUN pypy3 -m ensurepip && \
    pypy3 -m pip install --upgrade pip setuptools wheel

# =========================
# CPython 用ライブラリ（競プロ的に意味あるもの）
# =========================
RUN python3.13 -m pip install --no-cache-dir \
    bitarray==3.6.1 \
    gmpy2==2.2.1 \
    more-itertools==10.7.0 \
    numpy==2.2.6 \
    sortedcontainers==2.4.0 \
    Jinja2==3.1.6 \
    git+https://github.com/not522/ac-library-python@27fdbb71cd0d566bdeb12746db59c9d908c6b5d5

# =========================
# PyPy 用ライブラリ（提出向け・軽量）
# =========================
RUN pypy3 -m pip install --no-cache-dir \
    sortedcontainers==2.4.0 \
    more-itertools==10.7.0 \
    bitarray==3.6.0 \
    acl-cpp-python==0.6.2 \
    git+https://github.com/not522/ac-library-python@27fdbb71cd0d566bdeb12746db59c9d908c6b5d5

# =========================
# Rust 1.89.0（固定）
# =========================
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain 1.89.0
RUN rustup component add rustfmt clippy

# ACL（Rust）事前ビルドで初回高速化
RUN cargo new atcoder && cd atcoder && \
    echo 'proconio = "0.4"' >> Cargo.toml && \
    cargo build && \
    rm -rf /atcoder


# =========================
# CPython 用ライブラリ（環境構築用）
# =========================
RUN python3.13 -m pip install --no-cache-dir \
    Jinja2==3.1.6 \
    online-judge-tools \
    aclogin \
    tomlkit==0.13.3

# =========================
# 便利 alias
# =========================
RUN echo 'alias py="python3.13"' >> /root/.bashrc && \
    echo 'alias pypy="pypy3"' >> /root/.bashrc

# =========================
# 作業ディレクトリ
# =========================
WORKDIR /workspace
ENV PATH="/workspaces/AtCoder/scripts/bin:${PATH}"
