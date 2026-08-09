FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN groupadd --system office && useradd --system --gid office --create-home office

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN python -m pip install .

COPY data ./data
RUN mkdir -p /output && chown office:office /output

USER office

ENTRYPOINT ["agentic-office", "run", "--products", "data/sample_products.csv", "--sales", "data/sample_sales.csv", "--output", "/output"]
