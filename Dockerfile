FROM python:3.13-slim@sha256:ffb752e139c0a19692a43af8d8523b274222dd68eebad5d583b45c2201c6e30a

LABEL org.opencontainers.image.title="Multi-Agent AI Analytics Office" \
      org.opencontainers.image.description="Deterministic offline evaluation harness for a role-based analytics workflow" \
      org.opencontainers.image.source="https://github.com/Lee2379/multi-agent-ai-analytics-office" \
      org.opencontainers.image.licenses="MIT"

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
VOLUME ["/output"]

USER office

ENTRYPOINT ["agentic-office", "run", "--products", "data/sample_products.csv", "--sales", "data/sample_sales.csv", "--output", "/output"]
