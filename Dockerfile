FROM python:3.10-slim
ARG BASE_DIR
ARG RESOURCES_DIR
ADD . ${BASE_DIR}/path_test
ENV PYTHONPATH=$PYTHONPATH:${BASE_DIR}/path_test
RUN mv ${BASE_DIR}/path_test/path_test/resources ${RESOURCES_DIR}
WORKDIR ${BASE_DIR}/path_test/path_test/
CMD python app/test.py
